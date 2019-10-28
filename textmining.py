import urllib.request
import random
import string
#download text from Gutenberg project, decoding
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
#I have modified stopwords.txt to add in words commonly used in the Gutenberg header and footer. 
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
text_files=['Beowulf.txt', 'Pride and Prejudice.txt','Frankenstein.txt','A Modest Proposal.txt','poe.txt']
#documents reads all the texts
documents=[open(f, encoding='utf8').read() for f in text_files]
#compute tfidf vectors from the texts
tfidf=TfidfVectorizer().fit_transform(documents)
pairwise_similarity=tfidf*tfidf.T 
print(pairwise_similarity.toarray())

#text clustering
import numpy as np 
from sklearn.manifold import MDS
import matplotlib.pyplot as plt 

# s variable stores the similarities calculated in previous text similarity section
s=np.asarray([[1.,         0.75435797, 0.84884674, 0.7946772,  0.73382239],
[0.75435797, 1.,         0.87361434, 0.79423915, 0.50519677],
[0.84884674, 0.87361434, 1.,         0.84815379, 0.63301119],
[0.7946772,  0.79423915, 0.84815379, 1.,         0.61001115],
[0.73382239, 0.50519677, 0.63301119, 0.61001115, 1.        ]])
dissimilarities=1-s

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))
plt.show()