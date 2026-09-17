# 0. 개요
- 가중치 매개변수의 최적값을 탐색하는 최적화 방법, 가중치 매개변수 초깃값, 하이퍼파라미터 설정 방법 등.
- 과대적합의 대응책인 가중치 감소, 드롭아웃 등의 정규화 방법.
- 배치 정규화

<br><br>

# 1. 매개변수 갱신
- 신경망 학습의 목적은 손실 함수의 값을 가능한 낮추는 매개변수를 찾는 것이며 이러한 작업을 <strong>최적화(optimization)</strong>라 한다.
  - 심층 신경망에서는 매개변수의 수가 엄청나게 많아지는 등 생각보다 어려운 문제이다.
- 지금까지는 매개변수의 기울기(미분)를 활용하는 확률적 경사 하강법(SGD)에 대해 학습하였다. 이번 장에서는 SGD의 단점과 다른 최적화기법들에대해서도 학습한다.

## 1-1. 모험가 이야기
- 모험가 이야기의 예시를 들어 SGD에 대해 설명한다.
- SGD는 지금 서 있는 위치에서 가장 크게 기울어진 방향으로 이동하는 전략이다.

## 1-2. 확률적 경사 하강법(SGD)
- SGD는 수식으로 다음과 같이 표현할 수 있다.
  - $ W $: 갱신할 가중치 매개변수.
  - $ \frac{\partial L}{\partial W} $: 손실 함수의 기울기
  - $ \eta $: 학습률을 의미하며 일반적으로 0.01이나 0.001과 같은 값을 미리 정해 사용한다.
  - $ \leftarrow $: 우변의 값으로 좌변을 갱신함을 의미한다.
- 구현한 코드는 DL_from_floor/common/optimizer.py에 있다.
- 대부분의 딥러닝 프레임워크는 다양한 최적화 기법을 구현해 제공하며, 원하는 기법으로 쉽게 바꿀 수 있는(선언형) 구조로 되었다.

$$
W \leftarrow W-\eta \frac{\partial L}{\partial W}
$$

```python
# 1. SGD 클래스를 활용한 신경망 예.
network = TwoLayerNet(...)
optimizer = SGD()

for i in range(10000):
    """
    x_batch, t_batch = get_mini_batch(...)  # 미니배치
    grads = network.gradient(x_batch, t_batch)
    params = network.params
    optimizer.update(params, grads)
    """
```

## 1-3. SGD의 단점 (p192)
- SGD는 방향에 따라 기울기가 달라지는 <strong>비등방성(anisotropy) 함수</strong>라는 단점이 있다.
  - 결국 방향에 따라 기울기가 달라지기 때문에 <strong>탐색 경로가 비효율적</strong>이된다.
  - SGD가 지그제그로 탐색하는 근본 원인 또한 마찬가지로 <strong>기울어진 방향이 본래의 최솟값과 다른 방향</strong>을 가리켜서라는 점도 생각해볼 필요가 있다.

## 1-4. 모멘텀
- <strong>모멘텀(Momentum)</strong>은 운동량을 뜻하는 단어로 물리와 관계가 있으며 다음과 같이 수식으로 쓸 수 있다.
  - $ W $: 갱신할 가중치 매개변수
  - $ \frac{\partial L}{\partial W} $: $ W $에 대한 손실 함수의 기울기
  - $ \eta $: 학습률
  - $ \bold v $: 물리에서 말하는 속도(velocity)
- 의미적으로 기울기 방향으로 힘을 받아 물체가 가속된다는 물리 법칙을 나타낸다.
- $ a\bold v $는 물체가 아무런 힘을 받지 않을 때 서서히 하강시키는 역할을 한다.
  - 물리에서는 지면 마찰이나 공기 저항에 해당한다.
- 모멘텀을 구현한 코드는 DL_from_floor/common/optimizer.py에 있다.

$$
\bold v \leftarrow a\bold v-\eta\frac{\partial L}{\partial W}
$$

$$
W \leftarrow W + \bold v
$$

- 모멘텀은 $ \bold v $에 이때까지 기울기 정보의 방향성을 누적하기 때문에 SGD보다 지그재그 모양으로 튀는 것을 방지할 수 있다.

## 1-5. AdaGrad
- 그림은 p198.
- 신경망 학습에서 학습률($ \eta $)이 중요한데 학습을 진행하면서 학습률을 점차 줄이는 방법을 학습률 <strong>감소(learning rate decay)</strong>라 한다.
  - 처음에는 크게 학습하다가 나중에는 작게 학습한다는 의미로 실제 신경망 학습에 자주 사용된다.
- 학습률을 서서히 낮추는 가장 간단한 방법은 전체의 학습률 값을 일괄적으로 낮추는 것이며 이를 더욱 발전시킨 기법이 AdaGrad이다.
- AdaGrad는 개별 매개변수에 <strong>적응적으로(adaptive)</strong> 학습률을 조정하면서 학습을 진행하며 갱신 수식은 다음과 같다.
  - $ \bold h $: 기존 기울기 값을 제곱하여 계속 더해주는 변수이다.
  - $ \odot $: 행렬의 원소별 곱셈을 의미한다.
  - $ {1 \over {\sqrt \bold h}} $: 매개변수를 갱신할 때 학습률을 조정한다.
    - 매개변수의 원소 중 많이 움직인 원소는 학습률이 낮아짐을 의미한다.
    - 즉, 학습률 감소가 매개변수의 원소마다 다르게 적용됨을 뜻한다.

$$
\bold h = \bold h+\frac{\partial L}{\partial \bold W} \odot \frac{\partial L}{\partial \bold W}
$$

$$
\bold W \leftarrow \bold W-\eta{1\over \sqrt \bold h}\frac{\partial L}{\partial \bold W}
$$

- AdaGrad는 과거의 기울기를 제곱하여 더해하기 때문에 갱신 강도는 점차 약해지며 마지막에는 순간 <strong>갱신량이 0</strong>이되어 갱신이 되지 않는다.
  - 갱신량이 0이 되는 문제를 개선한 방법으로 <strong>RMSProp</strong>이 있으며 먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영한다.
    - RMSProp의 방식을 <strong>지수이동평균(Exponential Moving Average)</strong>이라 하며 기술기의 반영 규모를 기하급수적으로 감소 시킨다.
- 코드 구현은 DL_from_floor/common/optimizer.py에 있다.

## 1-6. Adam
- Momentum과 AdaGrad를 융합하는 아이디어에서 출발한 기법이 Adam이다.
- 모멘텀과 동일하게 방향성을 유지하면서 지그재그로 움직이지만 AdaGrad의 학습률 조정이 들어가 기울이 변경 폭이 줄어든다.
- 관련 코드는 DL_from_floor/common/optimizer.py에 있다.

## 1-7. 어느 갱신 방법을 이용할 것인가?
- DL_from_floor/ch06/optimizer_compare_naive.py에 비교 시각화 코드존재.
- 정답은 존재하지 않는다. 각자 장단점이 있기 때문에 주어진 문제에 적합한 방법을 비교 실험하는 것이 좋다.

## 1-8. MNIST 데이터셋으로 본 갱신 방법 비교
- MNIST 데이터셋에 대한 네 가지 기법의 비교 시각화는 DL_from_floor/ch06/optimizer_compare_mnist.py에 존재.
- 학습률과 신경망의 구조(층 깊이 등)에 따라 결과가 달라지며 비교 결과만 확인하면 된다.

<br><br>

# 2. 가중치의 초깃값
- 신경망 학습에서 가중치의 초깃값은 신경망 학습의 성패를 가를 정도로 중요하다.

## 2-1. 초깃값을 0으로 하면?
- <strong>가중치 감소(weight decay)</strong> 기법은 과대적합이 일어나지 않도록 매개변수가 작아지도록 학습하는 방법이다.
- 가중치의 초깃값은 작게 시작하는 것이 정공법이나 0을 초깃값으로 하면 안 된다.
  - 초깃값을 0으로 설정하면 순전파 때에 입력층의 가중치가 0이기 때문에 두 번째 층의 모든 뉴런에 모두 값은 값이 전달된다.
  - 즉 가중치들이 모두 똑같이 갱신되기 때문에 갱신을 하여도 여전히 같은 값을 유지하게 된다.
  - 따라서 초깃값은 <strong>무작위로 설정</strong>하는 것이 적합하다.

## 2-2. 은닉층의 활성화값 분포
- 은닉층의 활성화값(활성화 함수의 출략 데이터)의 분포를 관찰하면 중요한 정볼르 얻을 수 있으며 이번 주제에서는 가중치의 초깃값에 따라 은닉층 활성화값들이 어떻게 변화하는지 살펴본다.
- 관련된 코드는 DL_from_floor/ch06/weight_init_activation_histogram.py에 있다.
- 결과를 확인해보면 시그모이드 함수(활성화 함수)는 출력이 0 혹은 1에 가까워지면 그 미분은 0에 근사해진다.
  - 이렇게 기울이 값이 점점 작아지다 사라지는 문제를 <strong>기울기 소실(gradient vanishing)</strong>이라 한다.
- 표준편차를 0.01로 수정하면 활성화값 분포는 0.5 부근에 치우치게 된다.
  - 기울기 소실문제는 발생하지 않으나 활성화값들의 분포가 치우치게되어 <strong>표현력 측면</strong>에서 문제가 발생한다.
- 일반적인 딥러닝 프레임워크에서 표준적으로 사용되는 Xavier 초깃값을 사용한다.
  - 활성화값들을 광범위하게 분포시킬 목적으로 가중치의 적절한 분포를 찾고자 하여 앞 계층의 노드가 $n$개라면 $\sqrt{1 \over n}$인 분포를 사용한다. 
  - 층이 깊어지면 분포의 형태가 다소 일그러지지만 확실히 다른 방식에 비해 분포가 넓게 분포하는 것을 알 수 있다.
- 각 층의 활성화값은 <strong>적당히 고루 분포</strong>되어야 한다. 그래야 층과 층 사이에 <strong>다양한 데이터</strong>가 흘러 신경망 학습이 효율적으로 이루어지기 때문이다.

## 2-3. ReLU를 사용할 때의 가중치 초깃값
- Xavier 초깃값은 활성화 함수가 <strong>선형</strong>이라는 전제로 이끈 결과이다. sigmoid와 tanh는 좌우 대칭이라 <strong>중앙 부근을 선형</strong>인 함수로 볼 수 있다.
- 그러나 ReLU를 사용할 경우 ReLU에 특화된 초깃값을 이용할 것을 권장한다. 이 초깃값은 카이밍 히(Kaimming He)의 이름을 따 <strong>He 초깃값</strong> 이라 한다.
  - He 초깃값은 앞 계층의 노드가 $n$개일 때, 표준편차가 $\sqrt {2 \over n}$인 정규분포를 사용한다.
  - ReLU는 <strong>음의 영역이 0</strong>이라서 <strong>더넓게 분포</strong>를 시키기위해 2배의 계수가 필요하다고 해석할 수 있다.
- 시각화를 확인하여도 ReLU의 경우 균일하게 분포하는 것을 볼 수 있다.

## 2-4. MNIST 데이터셋으로 본 가중치 초깃값 비교
- 초깃값 비교 시각화는 DL_from_floor/ch06/weight_init_compare.py에 있다.