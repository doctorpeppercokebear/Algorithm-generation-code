# 학습용 데이터
from sklearn import datasets

# 학습, 테스트 분리 함수
from sklearn.model_selection import train_test_split

# 데이터 표준화
from sklearn.preprocessing import StandardScaler

# 로지스틱 알고리즘
from sklearn.linear_model import LogisticRegression

# 정확도 계산 함수
from sklearn.metrics import accuracy_score

# 파일 저장
import pickle
import numpy as np

names = None


def step1_get_data():
    iris = datasets.load_iris()
    X = iris.data[:100, [2, 3]]
    y = iris.target[:100]
    names = iris.target_names[:100]
    return X, y


def step2_learning():
    X, y = step1_get_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    ml = LogisticRegression(C=1000.0, random_state=0, max_iter=10)
    ml.fit(X_train_std, y_train)
    X_test_std = sc.transform(X_test)
    y_pred = ml.predict(X_test_std)
    print("학습된 정도: %.2f" % (accuracy_score(y_test, y_pred)))
    with open("5.LogisticRegression/model.pkl", "wb") as fp:
        pickle.dump(sc, fp)
        pickle.dump(ml, fp)


def setp3_using():
    with open("5.LogisticRegression/model.pkl", "rb") as fp:
        sc = pickle.load(fp)
        ml = pickle.load(fp)
    X = [[1.4, 0.2], [1.5, 0.3], [1.6, 0.4], [1.7, 0.5], [1.8, 0.6]]
    X_std = sc.transform(X)
    y_pred = ml.predict(X_std)
    # print(y_pred)
    for v in y_pred:
        if v == 0:
            print("Iris-setosa")
        else:
            print("Iris-versicolor")


if __name__ == "__main__":
    # step2_learning()
    setp3_using()
