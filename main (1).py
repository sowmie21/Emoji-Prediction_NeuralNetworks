import nltk
nltk.download('all-nltk')
print("\n")

# Creating token of words
print("Creating token of words:")
from nltk.tokenize import word_tokenize
text="My name is Adithya Challa I wrote this shot!"
tokenize_word=word_tokenize(text)
print(tokenize_word)
print("\n")

# Stemming
print("Stemming:")
from nltk.stem import PorterStemmer
words=["light","lighting","lights"]
ps=PorterStemmer()
for w in words:
    rootword=ps.stem(w)
    print(rootword)
print("\n")

#Lemmatiztion:Converts allverb forms into root word
print("Lemmatiztion:Converts allverb forms into root word:")
from nltk.stem import WordNetLemmatizer
lem=WordNetLemmatizer()
print(lem.lemmatize("playing"))
print("\n")

#POS Tag
print("POS Tag:")
from nltk import word_tokenize,pos_tag
text="My name is Adithya Challa I wrote this shot!"
print(pos_tag(word_tokenize(text)))    
