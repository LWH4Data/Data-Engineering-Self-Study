import os
import pickle
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from dataset.mnist import load_mnist

def get_data():
    (x_train, t_train), (x_test, t_test) =\
        load_mnist(normalize=True, flatten=True, one_hot_label=False)

    return x_test, t_test

def init_network():
    weight_path = os.path.join(os.path.dirname(__file__), 'sample_weight.pkl')
    with open(weight_path, 'rb') as f:
        network = pickle.load(f)

    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    x = x - np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

x, t = get_data()
network = init_network()

batch_size = 100  # 배치 크기.
accuracy_cnt = 0

# for loop 내부의 range를 통해 배치 처리를 구현.
for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)

    # 각 행을 기준으로 가장 높은 값(높은 확률)을 예측 결과로 한다.
    # (axis=1은 행 방향).
    #   - argmax()도 마찬가지로 bool 배열을 만들고 활용하는 방법이다.
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))