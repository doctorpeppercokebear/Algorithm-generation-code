import pandas as pd
import numpy as np
import os
import codecs
import re

def step1_get_data():
    # 데이터 파일 위치
    path = '9.Sentiment/aclImdb/'
    # 긍정 부정 값
    labels = {'pos': 1, 'neg': 0}
    df = pd.DataFrame()
    # 디렉토리 수 만큼 반복
    for s in ('test', 'train'):
        for name in ('pos', 'neg'):
            subpath = '%s/%s' % (s, name)
            # print(path + subpath)
            # 현재 디렉토리의 파일 목록
            file_list = os.listdir(path + subpath)
            # print(file_list)
            for file in file_list:
                # print(path + subpath + '/' + file)
                # print(os.path.join(path+subpath, file))
                file_name = os.path.join(path+subpath, file)
                with codecs.open(file_name, 'r', 'utf-8') as fp:
                    txt = fp.read()
                    # print(labels[name], txt)
                df = df.append([[txt, labels[name]]], ignore_index=True)
    df.columns = ['review', 'sentiment']
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    df.to_csv('9.Sentiment/aclImdb/movie_review.csv', index=False)

def preprocessor(text):
    #HTML 태그 삭제
    text = re.sub('<[^>]*>', '', text)
    # 이모티콘 찾기 정규식
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)|\^.?\^', text)
    # 특수문자 제거
    # 소문자 변환
    # 이모티콘 제거
    text = re.sub('[\W]+', ' ', 
                  text.lower() + ' '.join(emoticons).replace('-', ''))
    return text

def step2_preprocessing():
    # print(preprocessor('<brrrr />ha<a>hah</a>ah :-( ;-) ADFSDFdfdfdfd'))
    df = pd.read_csv('9.Sentiment/aclImdb/movie_review.csv')
    # print(df.shape)
    df['review'] = df['review'].apply(preprocessor)
    df.to_csv('9.Sentiment/aclImdb/setp2_movie_review.csv', index=False)

from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
# stopwords 사전 다운로드
nltk.download('stopwords')
stop = stopwords.words('english')
porter = PorterStemmer()

# 공백 기준 단어 분리
def tokenizer(text):
    return text.split()

# 단어의 원형 변환
def tokenizer_porter(text):
    word_list = tokenizer(text)
    # 단어 원형
    word_list2 = [porter.stem(word) for word in word_list]
    return word_list2

def step3_word_tokenizer():
    print(tokenizer_porter('runners like running and thus they run'))

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def step4_learning():
    pass

if __name__ == '__main__':
    # step1_get_data()
    # step2_preprocessing()
    step3_word_tokenizer()
    # step4_learning()