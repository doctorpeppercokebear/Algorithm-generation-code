# Iris 데이터를 활용한 퍼셉트론
# 붓꽃 종류 3가지 종(setosa, versicolor, virginica)에 대헤 꽃받침(sepla). 꽃잎(petal)의 길이를 정리한 데이터이다
# 퍼셉트론 알고리즘을 이용해 꽃 받침 길이와 너비, 꽃 잎의 길이와 너비를 이용해 아이리스 품종을 구분할 수 있는 머신러닝을 수행
# 퍼셉트론은 바이너리 결과를 가지므로 3개의 품종을 동시에 구분할 수 없다.
# EOFError: Ran out of input -> 파일이름에 띄어쓰기 넣으면 저장경로 불어오거나 저장할 때 오류가 생긴다

import numpy as np
import pandas as pd
from perceptron import Perceptron  # perceptron.py를 복사해서 경로를 같게 해서 불어왔다
import pickle

def step1_get_data():
    # iris data를 파일에서 읽어옴
    df = pd.read_csv('./3.IrisPerceptron/iris.data', header= None)
    print(df.head())

# def step2_learning():
#     pass

# def step3_using():
#     pass


    # 꽃잎 데이터 추출
    X = df.iloc[:100, [2, 3]].values
    # print(X)
    
    # 꽃 종류 (종속데이터)
    y = df.iloc[:100, 4]
    y = np.where(y == 'Iris-setosa', 1, -1)
    # print(y)
    return X, y

def step2_learning():
    ppn = Perceptron(eta=0.1)
    X, y = step1_get_data()
    # 학습
    ppn.fit(X, y)
    print(ppn.w_)
    # 학습된  데이터 저장
    with open('./3.IrisPerceptron/perceptron.iris', 'wb') as fp:
        pickle.dump(ppn, fp)
    print('학습완료')

def step3_using():
    # 저장된 모델 불러오기
    with open('./3.IrisPerceptron/perceptron.iris', 'rb') as fp:
        ppn = pickle.load(fp)
    while True:
        a1 = input('꽃잎의 길이를 입력하세요:')
        a2 = input('꽃잎의 너비를 입력하세요:')
        X = np.array([float(a1), float(a2)])
        # print(X)
        result = ppn.predict(X)
        if result == 1:
            print('Iris-setoda')
        else:
            print('Iris-versicolor')


if __name__ == '__main__':
    # step1_get_data()
    # step2_learning()
    step3_using()