#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install nltk


# In[4]:


import nltk

# Download all NLTK resources
nltk.download('all')


# In[5]:


import nltk

# Download specific resources
nltk.download('punkt')  # For tokenizers
nltk.download('stopwords')  # For stopwords
nltk.download('averaged_perceptron_tagger')  # For POS tagging


# In[6]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

# Download the NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Sample text for NLP processing
text = "Natural Language Processing (NLP) is a subfield of artificial intelligence. It focuses on the interaction " \
       "between computers and human language. NLP tasks include text processing, sentiment analysis, machine " \
       "translation, and more."

# Tokenization: Break text into words (tokens)
words = word_tokenize(text)

# Stopword Removal: Remove common words that do not carry much meaning
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Sentence Tokenization: Break text into sentences
sentences = sent_tokenize(text)

# POS Tagging: Assign grammatical parts-of-speech to each word
pos_tags = nltk.pos_tag(words)

# Stemming: Reduce words to their base form (stem)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

# Frequency Distribution: Count word occurrences
freq_dist = FreqDist(filtered_words)

# Print the results
print("Original Text:")
print(text)
print("\nTokenized Words:")
print(words)
print("\nFiltered Words after Stopword Removal:")
print(filtered_words)
print("\nSentences:")
print(sentences)
print("\nPOS Tags:")
print(pos_tags)
print("\nStemmed Words:")
print(stemmed_words)
print("\nWord Frequency Distribution:")
print(freq_dist.most_common(5))  # Print the 5 most common words and their counts


# In[ ]:




