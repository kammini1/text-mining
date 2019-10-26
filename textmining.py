import urllib.request
import random
import string
url='http://www.gutenberg.org/cache/epub/16328/pg16328.txt'
response=urllib.request.urlopen(url)
data=response.read()
text=data.decode('utf-8')
words=text.split()
#words is a list of all words in the Gutenberg text
d=dict()
#determining the most frequently used words in the text (excluding stop words)
for word in words:
    strippables=string.punctuation+string.whitespace
    word=word.strip(strippables)
    word=word.lower()
    word=word.replace('-','')
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
#d stores words (keys) and frequencies (outputs)
t=[]
e=dict()
#e will store the stop words 
excluding_stopwords=True
stopwords_list=open('stopwords.txt')
for line in stopwords_list:
    stopwords=line.strip()
    if stopwords not in e:
        e[stopwords]=stopwords
for word, frequency in d.items():
    if word in e:
        continue
    else:
        t.append((frequency,word))
t.sort(reverse=True)
#returns the top x most frequent words (excluding words in the stopword list), based on what integer you enter. 
number=int(input('Enter an integer.'))
print('The',number, 'most frequent words in this text are:')
for frequency,word in t[:number]:
    print(word, '\t', frequency)

#sentiment analysis using nltk
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
score=SentimentIntensityAnalyzer().polarity_scores(text)
print(score)

#hist={}
#filename='Beowulf.txt'
#fp=filename.decode('utf-8')
#print(fp)

#def skip_gutenberg_header(fp):
        #for line in fp:
            #if line.startswith('*** START OF THIS PROJECT'):
                #break
#skip_gutenberg_header(fp)

#def process_file(filename,skip_header):
    #if skip_header:
        #skip_gutenberg_header(fp)
    #for line in fp:
        #if line.startswith('*** END OF THIS PROJECT'):
            #break
        #for word in line.split():
        #if word not in hist:
            #hist[word]=1
        #else:
            #hist[word]+=1
#print(hist)

#process_file(filename,skip_header=True)

#def most_common(hist,excluding_stopwords=True):
    #t=[]
    #stopwords=process_file('stopwords.txt',False)
    #stopwords=list(stopwords.keys())
    #print(stopwords)
    #for letter,freq in hist.items():
        #if excluding_stopwords:
            #if word in stopwords:
                #continue 
        #t.append((freq,word))

#most_common(hist,excluding_stopwords=True)


