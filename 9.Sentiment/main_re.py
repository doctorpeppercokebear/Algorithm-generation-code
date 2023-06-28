import pandas as pd
import numpy as np
import os
import codecs
import re
from step1_get_data import step1_get_data
from step2_preprocessing import step2_preprocessing
from step3_word_tokenizer import step3_word_tokenizer

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def step4_learning():
    pass

if __name__ == '__main__':
    step1_get_data()
    # step2_preprocessing()
    # step3_word_tokenizer()
    # step4_learning()