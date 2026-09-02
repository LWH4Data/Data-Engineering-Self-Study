import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)  # 정규분포로 초기화

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

# 실행부
net = simpleNet()

# 가중치 매개변수
print("net.W \n", net.W)
print('')

x = np.array([0.6, 0.9])
p = net.predict(x)

# 입력 x에 대해 예측 수행
print("p \n", p)
print(np.argmax(p))

# 정답과의 loss 연산
t = np.array([0, 0, 1])  # 정답 레이블
print("net.loss \n", net.loss(x, t))

# 기울기 연산
# numerical_gradient(f, x)는 내부에서 f(x)를 실행하기에 f(W)로
# 형식을 맞춰준다.
def f(W):
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print("dW \n", dW)