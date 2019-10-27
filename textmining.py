import urllib.request
import random
import string
url='http://www.gutenberg.org/files/1342/1342-0.txt'
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

#text similarity using sklearn 
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
#text files variable stores the two texts I want to analyze
text_files=['Beowulf.txt' and 'Pride and Prejudice.txt']
#documents reads all the texts
documents=[open(f) for f in text_files]
print(type(documents))
#compute tfidf vectors from the texts
tfidf=TfidfVectorizer().fit_transform(documents)
pairwise_similarity=tfidf*tfidf.T 
print(pairwise_similarity)



