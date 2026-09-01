import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4  # 0.0001
    return (f(x + h) - f(x - h)) / (2 * h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

# 구현한 함수 확인.
# 0에서 20까지 0.1 간격의 배열 x. (20은 미포함).
x = np.arange(0.0, 20.0, 0.1) 
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()

# 미분 결과 확인.
x = np.arange(0.0, 20.0, 0.1) 
y = numerical_diff(function_1, x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()