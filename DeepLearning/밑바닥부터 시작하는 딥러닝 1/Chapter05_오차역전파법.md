# 0. 개요
- 앞선 장에서는 신경망의 가중치 매개변수 기울기를 수치 미분을 통해 구했다.
- 하지만 수치 미분은 단순하지만 시간이 오래 걸린다는 단점이 있으며 따라서 매개변수 기울기를 효과적으로 계산하는 **오차역전파법(backpropagation)**에 대해 배운다.
- 오차역전파법을 이해하는 방법은 크게 **수식**을 통한 방법과 **계산 그래프**를 통한 방법이 있다.
  - 도서에서는 먼저 계산 그래프를 통해 설명하고 수식은 코드를 통해 구현한다.

<br><br>

# 1. 계산 그래프
- 계산 그래프(computational graph)는 계산 과정을 표현한 그래프로 우리가 잘 아는 그래프 자료구조이며 복수의 **노드(node)**와 **에지(edge)**로 표현된다.

## 1-1. 계산 그래프로 풀다
- 계산 그래프는 계산 과정을 노드와 화살표로 표현한다.
  - 노드는 **원**으로 표기하고 원 안에 **연산 내용**을 적는다.
  - 계산 결과를 **화살표 위**에 적으며 각 노드의 계산 결과가 **왼쪽에서 오른쪽**으로 전해진다.
- 결국 계산 그래프는 아래 두 단계로 이루어 진다.
  1. 계산 그래프를 구성한다.
  2. 그래프에서 계산을 왼쪽에서 오른쪽으로 진행한다.
- 순전파(forward propagation)는 계산 그래프의 **출발점부터 종착**점으로 전파된다. 반대로 역전파(backward propagation)는 **순전파의 반대 방향**으로 전파되며 이후 미분을 계산할 때 중요한 역할을 한다.

## 1-2. 국소적 계산
- 계산 그래프는 **국소적 계산**을 전파함으로써 최종 결과를 얻는다.
  - 국소적 계산이란 **자신과 직접 관계된 작은 범위**를 의미한다.
  - 즉 자기자신과 관계된 정보만 결과로 출력하는 것이다.
  - 각 노드는 자신과 관련된 계산 외에는 아무것도 신경 쓸 필요가 없다.
- 결과적으로 국소적 계산은 **단순**하지만 결과를 전달함으로써 전체를 구성하는 **복잡한 계산**을 해낼 수 있다.

## 1-3. 왜 계산 그래프로 푸는가?
- 계산 그래프에는 다음과 같은 두 가지 이점이 있다.
  - 첫 번째는 앞서 살펴본 것과 같이 **국소적 계산**으로 전체 문제가 복잡하여도 각 노드에서는 단순한 계산에 집중하여 **문제를 단순화** 할 수 있다.
  - 두 번째는 계산 그래프는 **중간 계산 결과를 모두 보관**할 수 있다.
- 두 가지 이점 외에 가장 중요한 점은 **역전파**를 통해 **미분을 효율적으로 계산**할 수 있기 때문이다.
- 역전파는 국소적 미분을 순전파와 반대 방향으로 전달한다.
  - 입력으로 사용된 feature들 각자에 역전파로 극소적 비분을 전달할 수 있다.
  - 또한 중간까지 구한 미분 결과를 공유할 수 있어 다수의 미분을 효율적으로 계산할 수 있다.


<br><br>

# 2. 연쇄법칙
- 역전파를 통해 국소적 미분을 전달하는 방식은 <strong>연쇄법칙(chain rule)</strong>에 따른 원리이다.
- 즉 계산 그래프의 이점은 순전파와 역전파를 활용해서 각 변수의 미분을 효율적으로 구할 수 있다.

## 2-1. 계산 그래프의 역전파
- $ f(x) $라는 계산의 역전파를 이전 노드에 전달하는 과정을 예로 든다.
- 기준이 되는 노드의 순서상 뒤쪽 노드에서 전달받는 신호를 $ E $라하면 현재 노드의 미분값인 $ \frac{\partial y}{\partial x} $를 곱한 $ E\frac{\partial y}{\partial x} $을 순서상 앞쪽 노드에 전달한다.
- 이 역전파의 계산 순서를 가능하게 하는 것이 연쇄법칙이다.

## 2-2. 연쇄법칙이란?
- 연쇄법칙을 설명하기 위해서는 우선 합성 함수에 대해 설명해야 하며 **합성 함수**는 **여러 함수로 구성된 함수**를 의미한다.
  - 예를 들어 $ z=(x+y)^2 $는 $ z=t^2 $와 $ t = x + y $ 두 개의 식으로 구성된다.
- 연쇄법칙은 합성 함수의 미분에 대한 성질로 <strong>합성 함수를 구성하는 각 함수의 미분의 곱</strong>으로 나타낼 수 있다는 성질이다.
  - 각 식을 미분하면 다음과 같이 표현할 수 있다.

$$
\frac{\partial z}{\partial x}=\frac{\partial z}{\partial t}\frac{\partial t}{\partial x}
$$

- 각각의 식의 편미분을 구하고 위의 식을 정리하면 아래와 같이 정리할 수 있다.

$$
\frac{\partial z}{\partial x}=2t \quad \frac{\partial t}{\partial x}=1 
$$

$$
\frac{\partial z}{\partial x}=\frac{\partial z}{\partial t}\frac{\partial t}{\partial x}=2t \cdot1=2(x+y)
$$

## 2-3. 연쇄법칙과 계산 그래프
- 연쇄법칙을 응용하면 마지막 층에서부터 계속 국소적 미분을 곱하여 전달하면 결국 <strong>목표로하는 노드의 미분값</strong>을 구하는 식이 된다.
  - 즉 연쇄법측으로 중간 과정의 미분이 축적되며 <strong>목표로하는 노드의 변화량에 따른 최종 노드의 변화량(미분값)</strong>을 구할 수 있게 된다.
- 수식으로 표현하면 다음과 같다. 결국 연쇄법칙에 의해 해당하는 레이어와 최종 출력만 남는다.

$$
역전파의 \space 시작 = \frac{\partial z}{\partial z}
$$

$$
첫 \space 번째 \space 역전파 = \frac{\partial z}{\partial z} \frac{\partial z}{\partial t} = \frac{\partial z}{\partial t} 
$$

$$
두 \space 번째 \space 역전파= \frac{\partial z}{\partial z} \frac{\partial z}{\partial t} \frac{\partial t}{\partial x} = \frac{\partial z}{\partial x} 
$$

<br><br>

# 3. 역전파
## 3-1. 덧셈 노드의 역전파
- 덧셈 노드의 역전파는 전해진 미분값에 <strong>1을 곱하기만할 뿐</strong> 입력된 값을 <strong>그대로 다음 노드</strong>로 보낸다.
- 예를 들어 $ z = x + y $라면 다음이 성립한다.

$$
\frac{\partial z}{\partial x}=1 \quad \frac{\partial z}{\partial y} = 1
$$

## 3-2. 곱셈 노드의 역전파
- 곱셈 노드의 역전파는 상류의 값에 순전파 때의 입력 신호들을 <strong>서로 바꾼 값</strong>을 곱해서 하류로 보낸다.
  - 예를 들어 순전파 때 $ x $라면 역전파 때는 $ y $로, 반대로 순전파 때 $ y $였다면 역전파 때 $ x $로 바꾼다.
  - 직관적인 설명이 어렵기 때문에 p158 참고.
- 곱셈의 역전파는 <strong>순방향 입력 신호의 값</strong>이 필요하며 따라서 노드를 구현할 때 <strong>순전파의 입력 신호를 변수에 저장</strong>해 둔다.

## 3-3. 사과 쇼핑의 예
- 직관적인 설명이기 때문에 p159를 보며 이해.

<br><br>

# 4. 단순한 계층 구현하기
- 계산 그래프의 곱셈 노드를 MulLayer, 덧셈 노드를 AddLayer로 구현한다.
- 신경망을 구성하는 각 계층 각각을 하나의 클래스로 구현한다.
- 모든 계층은 순전파인 forward()와 역전파인 backward()라는 공톹 메서드(인터페이스)를 갖도록 구현한다.

## 4-1. 곱셈 계층
- DL_from_floor/ch05/layer_naive.py
  - MulLayer 클래스
- DL_from_floor_ch05/buy_apple.py
  - 신경망의 연산 수행

## 4-2. 덧셈 계층
- DL_from_floor/ch05/layer_naive.py
  - AddLayer 클래스
- DL_from_floor/ch05/buy_apple_orange.py

<br><br>

# 5. 활성화 함수 계층 구현하기
## 5-1. ReLU 계층
- 활성화 함수로 사용되는 ReLU의 수식은 다음과 같다.

$$
y = \begin{cases}
x & (x > 0) \\
0 & (x \le 0)
\end{cases}
$$

- $ x $에 대한 $ y $의 미분은 다음과 같이 구한다.

$$
\frac{\partial y}{\partial x} =
\begin{cases}
1 & (x > 0) \\
0 & (x \le 0)
\end{cases}
$$

- 미분식을 기준으로 역전파를 보면 다음과 같다.
  - 순전파 때의 입력 $ x $가 $ 0 $보다 크면 역전파는 상류의 값을 그대로 하류로 흘린다.
  - 순전파 때의 입력 $ x $가 $ 0 $ 이하면 역전파 때는 하류로 신호를 보내지 않는다. (0을 보냄).
- DL_from_floor/common/layers.py

## 5-2. Sigmoid 계층
- 시그모이드 함수는 다음과 같다.
- 시그모이드 함수에는 $ \exp $ 노드와 $ / $ 노드가 새롭게 등장한다.
  - $ \exp $ 노드는 $ y = exp(x) $ 연산을 수행한다.
  - $ / $ 노드는 $ y = {1 \over x} $ 연산을 수행한다.

$$
y = {1 \over {1+\exp(-x)}}
$$

- 역전파의 흐름은 다음과 같다.
  1. $ y = {1 \over x} $을 미분하면 다음과 같다.

  $$
  \frac{\partial y}{\partial x} =-{1 \over x^2} = -y^2
  $$

  2. '+' 노드는 상류의 값을 그대로 하류로 내보낸다.
  3. $ \exp $ 노드는 $ y=\exp(x) $ 연산을 수행하며 미분은 다음과 같다.
    - 따라서 계산 그래프에서는 <strong>순전파 때의 출력</strong>을 곱해 하류로 전파한다.

  $$
  \frac{\partial y}{\partial x} = \exp(x)
  $$

  4. 'x'노드는 순전파 때의 값을 '서로 바꿔' 곱한다.'
    - 역전파의 전체 연산을 합친 Sigmoid의 식은 다음과 같으며 입력 $ x $와 출력 $ y $만으로 표현이 가능하다.
    - 이로인해 Sigmoid의 세세한 내용을 제외하고 입력과 출력에만 집중할 수 있다.

  $$
  \frac{\partial L}{\partial y} \to \frac{\partial L}{\partial y}y^2\exp(-x)
  $$
    - 식은 다음과 같이 정리해서 쓸 수도 있다. 결과적으로는 Sigmoid 계층의 역전파는 순전파의 출력($ y $)만으로 계산할 수 있다.
  
  $$
  \begin{align}
  \frac{\partial L}{\partial y}y^2\exp(-x)&=\frac{\partial L}{\partial y}{1 \over (1 + \exp(-x))^2}\exp(-x)
  \\ & =\frac{\partial L}{\partial y}{1 \over {1+\exp(-x)}}{\exp(-x) \over{1+\exp(-x)}}
  \\ & = \frac{\partial L}{\partial y}(1-y)
  \end{align}
  $$

- 코드는 DL_from_floor/common/layers.py에 있다.

<br><br>

# 6. Affine/Softmax 계층 구현하기
## 6-1. Affine 계층
- 행렬의 곱 계산은 <strong>대응하는 차원의 원소 수</strong>를 일치시키는 것이 핵심이다.
- 신경망의 순전파 때 수행하는 행렬의 곱은 기하학에서는 <strong>어파인 변환(affine transformation)</strong>이라고 한다.
  - 도서에서 또한 Affine 계층이라는 용어를 사용한다.
- 앞서는 스칼라값을 이용하였으나 실제로는 행렬을 사용한 역전파도 행렬의 원소마다 전개하면 스칼라값을 통한 역전파와 차이가 없다. 식은 다음과 같다.
  - $ W^T $의 $ T $는 전체행렬을 의미한다. 전치행렬이란 $ W $의 $ (i, \space j) $ 위치의 원소를 $ (j, \space i) $ 위치로 바꾼 것을 의미한다.

$$
\frac{\partial L}{\partial X}=\frac{\partial L}{\partial Y}\cdot W^T
$$

$$
\frac{\partial L}{\partial W}=X^T \cdot \frac{\partial L}{\partial Y}
$$

$$
전치: W=
\begin{pmatrix} 
w_{11} & w_{12} & w_{13} \\
w_{21} & w_{22} & w_{23}
\end{pmatrix}
$$