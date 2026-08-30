<h1>1. 파이썬이란?</h1>
<ul>
  <li>
    생략
  </li>
</ul>

<br><br>

<h1>2. 파이썬 설치하기</h1>
<ul>
  <li>
    생략
  </li>
</ul>

<br><br>

<h1>3. 파이썬 인터프리터</h1>
<ul>
  <li>
    생략
  </li>
</ul>

<br><br>

<h1>4. 파이썬 스크립트 파일</h1>
<ul>
  <li>
    생략(실습만 진행).
  </li>
</ul>

<br><br>

<h1>5. 넘파이</h1>
<h2>5-1. 넘파이 가져오기</h2>
<ul>
  <li>
    numpy는 외부 라이브러리이기 때문에 라이브러리를 읽기 위해 import 문으로 가져온다.
  </li>
</ul>

```python
import numpy as np
```

<br>

<h2>5-2. 넘파이 배열 생성하기</h2>
<ul>
  <li>
    넘파이 배열을 만들 때는 <strong>np.array() 메서드</strong>를 이용한다.
  </li>
</ul>

```python
x = np.array([1.0, 2.0, 3.0])
print(x)
type(x)
```

<br>

<h2>5-3. 넘파이의 산술 연산</h2>
<ul>
  <li>
    넘파이는 산술 연산을 할 때에 각 객체의 <strong>원소 수가 동일</strong>해야한다.
  </li>
    <ul>
      <li>
        원소 수가 다르다면 오류를 발생한다.
      </li>
      <li>
        원소별이라는 말은 <strong>element-wise</strong>를 의미하며 원소별 곱셉은 element-wise product라고 한다.
      </li>
    </ul>
  <li>
    스칼라와의 연산을 할 때에는 스칼라와의 연산이 각 원소별로 수행이 되는데 이 기능을 <strong>브로드캐스트</strong>라고 한다.
  </li>
</ul>

```python
# 1. 원소별 연산 예.
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

# element-wise
x + y
x - y
x * y
x / y
```

```python
# 2. 스칼라 연산(브로드캐스트) 예.
x = np.array([1.0, 2.0, 3.0])
x / 2.0
```

<br>

<h2>5-4. 넘파이의 N차원 배열</h2>
<ul>
  <li>
    넘파이는 1차원 배열 뿐만 아니라 <strong>다차원 배열</strong>에서도 사용이 가능하다.
  </li>
    <ul>
      <li>
        행렬의 형상(각 차원의 크기(원소 수))은 <strong>shape<strong>으로, 행렬에 담긴 원소의 자료형은 <strong>dtype</strong>으로 알 수 있다.
      </li>
    </ul>
  <li>
    행렬의 연산도 배열의 연산과 동일하게 <strong>원소별</strong>로 수행되며 스칼라값의 산술 연산은 <strong>브로드캐스트 기능</strong>이 작동한다.
  </li>
  <li>
    넘파이 배열의 1차원 배열은 <strong>벡터(vector)</strong>, 2차원 배열은 <strong>행렬(matrix)</strong>라고 부른다.
  </li>
    <ul>
      <li>
        벡터와 행렬을 일반화한 것을 <strong>텐서(tensor)</strong>라고 한다.
      </li>
    </ul>
</ul>

```python
# 1. 2차원 배열(행렬)
A = np.array([[1, 2], [3, 4]])
print(A)

# 행렬의 형상
A.shape

# 행렬 원소의 자료형
A.dtype
```

```python
# 2. 행렬의 산술 연산
B = np.array([[3, 0], [0, 6]])
A + B
A * B
```

```python
# 3. 스칼라 연산.
print(A)
A * 10
```

<br>

<h2>5-5. 브로드캐스트</h2>
<ul>
  <li>
    넘파이에서는 형상이 다른 배열끼리도 계산이 가능한데 이 경우 <strong>형상이 작은 객체가 확장</strong>되어 연산을 수행하며 이 기능을 <strong>브로드캐스트(broadcast)</strong>라 한다.
  </li>
</ul>

```python
# 1. 브로드캐스트 연산의 예.
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])

# B가 A에 맞추어 2차원으로 확장되어 연산이 수행된다.
A * B
```

<br>

<h2>5-6. 원소 접근</h2>
<ul>
  <li>
    원소의 인덱스틑 <strong>0부터 시작</strong>하며 각 원소에 접근하기 위해서는 <strong>[]</strong>를 활용한다.
  </li>
  <li>
    넘파이의 주된 처리는 C와 C++로 구현되어 있어 성능을 해치지 않으면서 파이썬의 편리한 문법을 사용할 수 있다.
  </li>
</ul>

```python
# 1. 넘파이 배열의 원소에 접근.
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)

# 0행에 접근.
X[0]

# (0, 1) 위치의 원소에 접근.
X[0][1]
```

```python
# 2. for loop을 활용한 접근.
for row in X:
    print(row)
```

```python
# 3. 인덱스를 배열로 지정한 접근.
# X를 1차원 배열로 변환(평탄화)
X = X.flatten()
print(X)

# 인덱스가 0, 2, 4인 원소 얻기.
X[np.array([0, 2, 4])]
```

```python
# 4. 평탄화 후 조건에 맞는 값 얻기.
X > 15
# array([True, True, False, True, False, False])

# True인 경우만 출력한다.
X[X > 15]
```

<br><br>

<h1>6. 맷플롯립</h1>
<ul>
  <li>
    맷플롯립(Matplotlib)은 <strong>그래프</strong>를 그려주기 위한 라이브러리이다.
  </li>
</ul>

<br>

<h2>6-1. 단순한 그래프 그리기</h2>
<ul>
  <li>
    그래프를 그리기 위해서는 pyplot 모듈을 이용한다.
  </li>
  <li>
    실습은 DL_from_floor/ch01에 수록.
  </li>
</ul>

<br>

<h2>6-2. pyplot의 기능</h2>
<ul>
  <li>
    cos 함수 또한 DL_from_floor/ch01에 수록.
  </li>
</ul>

<br>

<h2>6-3. 이미지 표시하기</h2>
<ul>
  <li>
    pyplot에는 <strong>이미지를 표시</strong>해주는 메서드인 <strong>imshow()</strong>도 있다.
  </li>
    <ul>
      <li>
        이미지를 읽어 들일 때는 matplotlib.image 모듈의 <strong>imread() 메서드</strong>를 이용한다.
      </li>
    </ul>
  <li>
    실습은 DL_from_floor/ch01 수록.
  </li>
</ul>