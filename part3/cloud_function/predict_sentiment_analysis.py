#!/usr/bin/env python

import nltk

nltk.data.path = ['nltk_data']

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

import pickle

stopwords_eng = stopwords.words('english')

def extract_features(words):
    return [w.lower() for w in words if w.lower() not in stopwords_eng and w not in punctuation]

def bag_of_words(words):
    bag = {}
    for w in words:
        bag[w] = True
    return bag

model_file = open('sa_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()

def get_sentiment(review):
    words = word_tokenize(review)
    words = extract_features(words)
    words = bag_of_words(words)
    return model.classify(words)

def get_sentiment_batch(reviews):
    return [get_sentiment(review) for review in reviews]
