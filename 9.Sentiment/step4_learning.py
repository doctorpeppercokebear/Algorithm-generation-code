import pandas as pd
import numpy as np
import os
import codecs
import re

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import time

from step3_word_tokenizer import tokenizer
from step3_word_tokenizer import tokenizer_porter


def step4_learning():
    df = pd.read_csv("9.Sentiment/aclImdb/setp2_movie_review.csv")
    # print(df)
    # 학습데이터 테스트 데이터 분리
    X_train = df.loc[: 3500 - 1, "review"].values
    y_train = df.loc[: 3500 - 1, "sentiment"].values
    X_test = df.loc[3500:, "review"].values
    y_test = df.loc[3500:, "sentiment"].values
    # print(type(X_train), X_train.shape, y_train.shape)  # 제대로 나눠졌는지 확인 하는 작업 반드시 확인 해야함
    # print(type(X_test), X_test.shape, y_test.shape)

    # 단어장 만들어 주는 객체 생성
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer_porter)

    # ml 객체 생성
    logistic = LogisticRegression(C=10.0, penalty="l2", random_state=0)

    # pipeline 객체 생성
    pipeline = Pipeline([("tfidf", tfidf), ("logistic", logistic)])

    # 학습
    stime = time.time()
    print("학습시작")
    pipeline.fit(X_train, y_train)
    print("학습완료")
    print("학습시간: %.d" % (time.time() - stime))

    # 테스트
    y_perd = pipeline.predict(X_test)
    print("정확도: %.2f" % accuracy_score(y_test, y_perd))

    # 모델 저장
    with open("9.Sentiment/model.pkl", "wb") as fp:
        pickle.dump(pipeline, fp)
    print("저장완료")


if __name__ == "__main__":
    step4_learning()
