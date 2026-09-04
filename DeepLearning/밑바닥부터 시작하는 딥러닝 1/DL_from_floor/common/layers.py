import numpy as np
from functions import softmax
from functions import cross_entropy_error

class Relu:
    def __init__(self):
        # mask는 True/False로 구성되는 넘파이 배열로
        # 순전파의 입력인 x의 운소 값이 0 이하인 인덱스는 True,
        # 그 외는 False로 유지한다.
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return 0

    def backward(self, dout):
        # 역전파 때에는 순전파 때의 입력이 0 이하면(True)
        # 역젖ㄴ파 때의 값을 0으로 한다.
        dout[self.mask] = 0
        dx = dout

        return dx

class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.x = None
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b

        return out

    def backward(self, dout):
        # dX = dout · Wᵀ
        dx = np.dot(dout, self.W.T)

        # dW = Xᵀ · dout
        self.dW = np.dot(self.x.T, dout)

        # 덧셈의 미분은 1이므로 dout이 그대로 전달된다.
        # 같은 편향을 모든 데이터가 공유하므로 배치 방향으로 합산한다.
        self.db = np.sum(dout, axis=0)

        return dx

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None  # 손실함수
        self.y = None  # softmax의 출력
        self.t = None  # 정답 레이블(원-핫 벡터)

    def forward(self, x, t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        
        # Softmax와 교차 엔트로피 손실을 결합해서 미분하면
        # 입력 점수 x에 대한 기울기는 (y - t) / batch_size가 된다.
        dx = (self.y - self.t) / batch_size

        return dx