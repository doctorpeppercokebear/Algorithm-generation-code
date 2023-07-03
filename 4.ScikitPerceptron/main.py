# 학습용 데이터
from sklearn import datasets

# 학습, 테스트 분리 함수
from sklearn.model_selection import train_test_split

# 데이터 표준화, 데이터 분포를 가운데로 올 수 있도록
from sklearn.preprocessing import StandardScaler

# 퍼셉트론 알고리즘
from sklearn.linear_model import Perceptron

# 정확도 계산 함수
from sklearn.metrics import accuracy_score

# 파일 저장
import pickle
import numpy as np

# Scikit-learn: 파이썬으로 구현한 머신러닝을 위한 확장 라이브러리
# pip install scikit-learn

names = None


def step1_get_data():
    # data 가져오기
    iris = datasets.load_iris()
    # print(iris) # 딕셔너리 타입
    X = iris.data[:100, [2, 3]]
    y = iris.target[:100]
    names = iris.target_names[:100]
    # print(X)
    # print(y)
    # print(names)
    return X, y


def step2_learning():
    X, y = step1_get_data()
    # 학습, 데스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )  # random_state=0 난수 고정
    # data 표준화 작업
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    # 학습
    ml = Perceptron(
        eta0=0.01, max_iter=10, random_state=0
    )  # random_state=0 난수 고정하는게 좋다 -> 값이 계속 바뀌기 때문에
    ml.fit(X_train_std, y_train)  # X_train_std, y_train / X_test, y_test 반드시 짝 맞춰서 사용
    return sc, ml

    # 테스트 데이타 정확도 확인
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print("학습정확도:", accuracy_score(y_test, y_pred))
    with open("4.ScikitPerceptron/iris.ml", "wb") as fp:
        pickle.dump(sc, fp)
        pickle.dump(ml, fp)
    print("학습완료")


def step3_using():
    with open("4.ScikitPerceptron/iris.ml", "rb") as fp:
        ppn = pickle.load(fp)

    while True:
        a1 = input("꽃잎의 길이를 입력하세요: ")
        a2 = input("꽃잎의 너비를 입력하세요: ")
        X = np.array([[float(a1), float(a2)]])
        X_std = sc.transform(X)
        y = ml.predict(X_std)
        # print(y)
        if y[0] == 0:
            print("Iris_setoda")
        else:
            print("Iris-versicolor")


if __name__ == "__main__":
    # step1_get_data()
    # step2_learning()
    step3_using()
