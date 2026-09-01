# 오차제곱합 구현.
def sum_squares_error(y, t):
    return 0.5 * np.sum((y-t)**2)

# 데이터 불러와서 형식을 잡는 부분.
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = \
    load_mnist(normalize=True, one_hot_label=True)

print(x_train.shape)  # (60000, 784)
print(t_train.shape)  # (60000, 10)