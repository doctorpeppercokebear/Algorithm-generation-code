import numpy as np
from perceptron import Perceptron
from time import time
import pickle

def step1_learning():
    # 학습과 테스트를 위해 사용할 데이터 정의
    X = np.array([[1, 1], [1, 0], [0,1], [0,0]])  #열 백터
    y = np.array([1, -1, -1, -1])  # end  #행 백터
    # 퍼셉트론 객체 선언
    ppn = Perceptron(eta=0.1)
    #학습
    s_time = time()
    ppn.fit(X, y)
    e_time = time()
    print('학습에 걸린 시간:', (e_time - s_time))
    print('학습 중 오차가 난 수:', ppn.erros_)
    #학습된 모델 저장
    with open('2.perceptron.model', 'wb') as f:   #perceptron.model 이름으로 저장
        ppn = pickle.dump(ppn, f)

def step2_using():
    with open('2.perceptron.model', 'rb') as f:
        ppn = pickle.load(f)

    while True:
        a1 = input('첫번쨰 2진수를 입력하세요:')
        a2 = input('두번쨰 2진수를 입력하세요:')
        X = np.array([[int(a1), int(a2)]])
        result = ppn.predict(X)
        if result == 1:
            print('결과: 1')
        else:
            print('결과: 0')
        
if __name__ == '__main__':
    # p1 = Perceptron()
    # p1.test()
    # step1_learning()
    step2_using()


