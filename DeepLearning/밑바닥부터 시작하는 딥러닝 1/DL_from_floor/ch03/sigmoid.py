import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)  # sigmoid() 함수로 변경
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y축 범위 지정
plt.show()