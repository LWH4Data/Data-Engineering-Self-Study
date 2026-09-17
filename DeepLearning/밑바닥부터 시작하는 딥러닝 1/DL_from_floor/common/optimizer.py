class SGD:

    def __init__(self, lr=0.01):

        # 학습률 변수.
        self.lr = lr

    # update 메서드는 SGD 과정에서 반복적으로 호출됨.
    #   - 인수 params와 grads는 딕셔너리 변수이다 (지금까지와 같음).
    #   - params['W1'], grads['W1'] 등과 같이 각각 가중치 매개변수와 기울기 저장.
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]

class Momentum:
    def __init__(self, lr=0.011, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        # v는 초기화 때에는 아무 값도 담지 않는다.
        self.v = None

    def update(self, params, grads):
        if self.v is None:

            # update()가 호출되는 시점에 매개변수와 같은 구조의 데이터를 
            # v에 딕셔너리 변수로 저장한다.
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum*self.v[key] - self.lr*grads[key]
            params[key] += self.v[key]

class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]

            # self.h[key]의 값에 0이 담겨있을 수 있어 1e-7을 더한다.
            #   - 딥러닝 프레임워크에서는 인수로 설정할 수 있다.
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)

class Adam:

    def __init__(self, lr=0.01, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key, val in params.items():
                self.m[key] = np.zeros_like(val)
                self.v[key] = np.zeros_like(val)

        self.iter += 1
        lr_t = self.lr * np.sqrt(1.0 - self.beta2**self.iter) / (1.0 - self.beta1**self.iter)

        for key in params.key():
            #self.m[key] = self.beta1*self.m[key] + (1-self.beta1)*grads[key]
            #self.v[key] = self.beta2*self.v[key] + (1-self.beta2)*(greads[key]**2)
            self.m[key] += (1 - self.beta1) * (grads[key] - self.m[key])
            self.v[key] += (1 - self.beta2) * (grads[key]**2 - self.v[key])

            params -= lr_t * self.m[key] / (np.sqrt(self.v[key]) + 1e-7)

            #unbias_m += (1 - self.beta1) * (grads[key] - self.m[key])  # correct bias
            #unbias_b += (1 - self.beta2) * (grads[key]*grads[key] - self.v[key])  # correct bias
            #params[key] += self.lr * unbias_m / (np.sqrt(unbias_b) + 1e-7)