import numpy as np

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