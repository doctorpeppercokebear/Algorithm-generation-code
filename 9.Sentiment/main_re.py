import pandas as pd
import numpy as np
import os
import codecs
import re

# 모듈화 불러오기
from step1_get_data import step1_get_data
from step2_preprocessing import step2_preprocessing
from step3_word_tokenizer import step3_word_tokenizer

from step3_word_tokenizer import tokenizer
from step3_word_tokenizer import tokenizer_porter
from step4_learning import step4_learning

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import time


def step5_using():
    with open("9.Sentiment/model.pkl", "rb") as fp:
        pipeline = pickle.load(fp)
    while True:
        text = input("영문 리뷰를 입력하세요:")
        y = pipeline.predict([text])
        rate = pipeline.predict_proba([text]) * 100
        # print('y:', y)
        # print('rate:', rate)
        rate = np.max(rate)
        if y == 1:
            print("긍정리뷰")
        else:
            print("부정리뷰")
        print("정확도: ", round(rate, 2))


if __name__ == "__main__":
    # step1_get_data()
    # step2_preprocessing()
    # step3_word_tokenizer()
    # step4_learning()
    step5_using()
