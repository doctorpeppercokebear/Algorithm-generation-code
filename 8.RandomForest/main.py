# 학습용 데이터
from sklearn import datasets
# 학습, 테스트 분리 함수
from sklearn.model_selection import train_test_split
# 데이터 표준화, 데이터 분포를 가운데로 올 수 있도록
from sklearn.preprocessing import StandardScaler
# RandomForest 알고리즘
from sklearn.ensemble import RandomForestClassifier
# 정확도 계산 함수
from sklearn.metrics import accuracy_score
# 파일 저장
import pickle
import numpy as np

def step1_get_data():
    iris  = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target[:]
    # print(len(X))
    # print(len(y))
    return X, y 

def step2_learning():
    X, y = step1_get_data()
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.3, random_state=0)
    sc = StandardScaler()  # () 안 붙히면 TransformerMixin.fit_transform() missing 1 required positional argument: 'X' 오류 나옴
    X_train_std = sc.fit_transform(X_train)
    # n_estimatorss: 포레스트 내의 나무 개수
    # n_jobs : 병렬처리에서 사용할 코어 수, 머신러닝은 cpu만 사용
    # criterion : 불손도 측정 방식(entropy, gini)
    # max_depth : 트리의 최대깊이
    ml = RandomForestClassifier(n_estimators=10, n_jobs=2, criterion='entropy', max_depth=3, random_state=0)
    ml.fit(X_train_std, y_train)
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print('학습정확도: ', accuracy_score(y_test, y_pred))  # y_test 로 해야하는데 y_train으로 작성해서 샘플 수 안 맞는다고 오류

if __name__ == '__main__':
    step2_learning()
    