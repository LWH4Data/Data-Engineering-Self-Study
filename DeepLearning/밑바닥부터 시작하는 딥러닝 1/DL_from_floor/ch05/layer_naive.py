class MulLayer:
    def __init__(self):
        # 순전파 시의 입력 값을 유지하기 위해 사용.
        self.x = None
        self.y = None

    # 순전파는 x와 y를 인수로 받아 두 값을 곱해 반환.
    def forward(self, x, y):
        self.x = x
        self.y = y
        out = x * y

        return out

    # 상류에서 넘어온 미분(dout)에 순전파 때의 값을 서로 바꿔 곱하고 하류로 넘김.
    def backward(self, dout):
        dx = dout * self.y  # x와 y를 바꾼다.
        dy = dout * self.x

        return dx, dy

class AddLayer:
    def __init__(self):
        pass
    
    def forward(self, x, y):
        out = x + y
        return out

    # 상류에서 내려온 미분(dout)을 그대로 하류로 흘릴뿐이다.
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy