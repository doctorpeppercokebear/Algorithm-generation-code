import pandas as pd
import numpy as np

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


if __name__ == '__main__':
    step3_word_tokenizer()