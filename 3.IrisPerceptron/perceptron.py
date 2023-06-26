import numpy as np

class Perceptron:
    def __init__(self, thresholds=0.0, eta=0.01, n_iter=10):
        self.thresholds = thresholds
        self.eta = eta
        self.n_iter = n_iter
    # thresholds: 임계값, 계산된 예측값을 비교하는 값
    # eta: 학습률
    # n_iter: 학습 횟수
    
    #학습 함수
    # x: 입력 데이터, 독립변수, 특징, 퓨처, 설명면수
    # y: 결과데이터, 정답, 종속변수, 라벨, 클래스

    def fit(self, X,y):
        # 가중치를 담을 행렬을 생성
        self.w_ = np.zeros(1 + X.shape[1])
        # 에측값과 실제값을 비교하여 다른 예측 값의 개수를 담음
        self.erros_ = []  # _ : 외부에서 접근 하지 말라고 작성
        #지정된 학습 횟수만큼 반복
        for _ in range(self.n_iter):
            # 예측값 실제값이 다른 개수를 담을 변수
            erros = 0 
            # 입력데이터와 결과 데이터를 묶어줌
            temp1 = zip(X, y)
            for Xi, target in temp1:
                # 예측값과 실제값이 달면 가중치를 업데이트
                a1 = self.predict(Xi)
                if target != a1: 
                    update = self.eta * (target - a1)
                    #가중치(기울기)
                    self.w_[1:] += update * Xi
                    # 절편(바이어스)
                    self.w_[0] += update 
                    erros += int(update!= 0.0)
        self.erros_.append(erros)            
        print(self.w_)

    def predict(self, X):
        # step function
        a2 = np.where(self.net_input(X) > self.thresholds, 1, -1)
        return a2
    
    def net_input(self, X):
        a3 = np.dot(X, self.w_[1:]) + self.w_[0]
        return a3


    def test(self):
        print(self.thresholds)


if __name__ == '__main__':
    p1 = Perceptron(thresholds=2)
    print('test ok', p1.test())
