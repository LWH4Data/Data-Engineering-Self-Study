import numpy as np

def relu(x):
    
    # x와 0중 큰 값을 반환한다.
    return np.maximum(0, x)