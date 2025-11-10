<h1>1. Starlette</h1>
<ul>
  <li>
    FastAPI의 웹 코드 대부분은 톰 크리스티가 제작한 <strong>Starlette 패키지</strong>를 기반으로 한다.
  </li>
  <li>
    Starlette은 여러 곳에 사용이 되는데 <strong>최신 파이썬 비동기 웹인 ASGI</strong>를 지원하면서 Go 혹은 Node.js를 사용하는 앱과도 견줄 수 있게 됐다.
  </li>
</ul>

<br><br>

<h1>2. 동시성 유형</h1>
<ul>
  <li>
    동시성을 구현하는 방법에는 다음 두 가지가 있다.
  </li>
    <ul>
      <li>
        <strong>병렬 컴퓨팅 (parallel computing)</strong>
      </li>
        <ul>
          <li>
            하나의 작업을 <strong>여러 개의 전용 CPU</strong>에 동시에 분산한다.
          </li>
          <li>
            화면 구현이나 ML 같은 <strong>숫자 처리 앱</strong>에서 보편적으로 사용한다.
          </li>
        </ul>
      <li>
        <strong>동시 컴퓨팅(concurrent computing)</strong>
      </li>
        <ul>
          <li>
            각 CPU가 여러 작업을 <strong>전환</strong>한다.
          </li>
          <li>
            작업 시간이 비교적 느린 파일 읽기, 네트워크 등의 작업을 전환하며 처리하며 <strong>총시간의 감소</strong>를 목표로 한다.
          </li>
        </ul>
    </ul>
</ul>

<br>

<h2>2-1. 분산과 병렬 컴퓨팅</h2>
<ul>
  <li>
    단일 CPU에서 더디게 실행되는 앱이 있다면 <strong>여러 조각으로 나누어</strong> 단일 혹은 여러 머신의 개별 CPU에서 실행하도록 할 수 있다. 단, 단일 서버보다 <strong>비용</strong>이 많이 든다.
  </li>
  <li>
    나누어서 실행되는 앱에는 대개 <strong>동기 코드</strong>와 <strong>비동기 코드</strong>가 섞여 있으며 FastAPI 에서는 이런 코드를 처리할 수 있다.
  </li>
</ul>

<br>

<h2>2-2. 운영 체제 프로세스</h2>
<ul>
  <li>
    <strong>운영 체제(Operating system, OS)</strong>는 메모리, CPU, 장치, 네트워크 등의 <strong>자원 사용을 조율</strong>한다.
  </li>
  <li>
    모든 프로그램은 코드를 <strong>하나 이상의 프로세스</strong>에서 실행하며 OS는 각 프로세스의 <strong>자원에 접근을 제한</strong>해 관리한다.
  </li>
  <li>
    시스템은 대부분 <strong>선점형(preemptive) 프로세스 스케줄링</strong>을 사용해 특정 프로세스가 CPU, 메모리 및 기타 자원을 독점하지 못하게 한다. 이때 OS는 주어진 설계와 설정에 따라 <strong>프로세스를 중지</strong>하거나 <strong>재시작</strong>한다.
  </li>
    <ul>
      <li>
        선점형이란 실행 중인 프로세스를 <strong>강제로 멈추고 다른 프로세스에게 CPU를 넘길 수 있는 방식</strong>이다.
      </li>
    </ul>
  <li>
    개발자는 직접 이를 관여할 수 없기에 CPU 집약적인 파이썬 앱에서의 흔한 해결책은 <strong>여러 프로세스를 실행하고 OS가 관리</strong>하도록 하는 것이다. 파이썬은 이를 위해 <strong>multiprocessing 모듈</strong>을 제공한다.
  </li>
</ul>

<br>

<h2>2-3. 운영 체제 스레드</h2>
<ul>
  <li>
    단일 프로세스에서 <strong>여러 개의 스레드</strong>를 제어할 수 있으며 파이썬의 <strong>threading 모듈</strong>이 이를 관리한다.
  </li>
    <ul>
      <li>
        프로그램이 <strong>I/O에 바인딩</strong>되는 경우 <strong>스레드</strong>를, <strong>CPU에 바인딩</strong>되는 경우 <strong>다중 프로세스</strong>를 사용하길 권장한다.
      </li>
    </ul>
  <li>
    파이썬은 프로세스 기반 라이브러리와 스레드 기반 라이브러리를 분리했다. 그러나 <strong>최신 비동기 함수</strong>로 스레드의 이점을 손쉽게 취할 수 있다.
  </li>
    <ul>
      <li>
        FastAPI는 스레드풀을 통해 async def가 아닌 <strong>def로 시작하는 일반 동기 함수에 대한 스레드도 관리</strong>한다.
      </li>
    </ul>
</ul>

<br>

<h2>2-4. 그린스레드</h2>
<ul>
  <li>
    <strong>그린스레드</strong>는 <strong>협력적(cooperative, 비선점형)</strong>이며 greenlet, gevent, Eventlet으로 구현한다.
  </li>
  <li>
    OS 스레드와 유사하지만 <strong>유저 스페이스에서 동작</strong>한다.
  </li>
  <li>
    그린스레드 방식은 표준 파이썬 함수들을 <strong>몽키 패칭(monkey patching)</strong>하여 동작하며 I/O 대기 작업이 블로킹할 것 같으면 <strong>제어권을 포기</strong>한다.
  </li>
    <ul>
      <li>
        몽키 패칭이란 <strong>프로그램이 실행 중(runtime)</strong>에 기존 클래스나 모듈, 함수의 행동을 <strong>바꿔치기(수정)</strong>하는 것을 의미한다.
      </li>
    </ul>
  <li>
    OS 프로세스 > OS 스레드 > 그린스레드 순서대로 무겁다. 즉, 그린스레드가 가장 가볍다.
  </li>
</ul>

<br>

<h2>2-5. 콜백</h2>
<ul>
  <li>
    함수를 작성해 특정 이벤트에 연결한다.
  </li>
</ul>

<br>

<h2>2-6. 파이썬 제너레이터</h2>
<ul>
  <li>
    파이썬 또한 배부분의 프로그래밍 언어와 같이 <strong>순차적으로 코드를 실행</strong>한다.
  </li>
  <li>
    그러나 파이썬의 <strong>제너레이터 함수</strong>는 원하는 곳에서 실행을 멈추고 <strong>return</strong>을 하거나 <strong>yield 키워드</strong>를 사용해 다시 해당 지점으로 돌아갈 수 있다.
  </li>
  <li>
    <strong>return</strong>은 <strong>메모리에 모든 값을 저장</strong>한 뒤 <strong>한 번에 반환</strong>하지만, <strong>yield</strong>는 값을 <strong>하나씩 생성해 반환</strong>하며, 이때마다 함수 실행이 <strong>일시 정지</strong>되었다가 다음 호출 시 <strong>다시 이어서 진행</strong>된다.
  </li>
  <li>
    <strong>yield 키워드</strong>를 갖는 함수는 모두 <strong>제너레이터 함수</strong>이다.
  </li>
</ul>

```python
# 1. return 사용
def doh():
    # 전체를 한 번에 메모리에 저장.
    return ["Homer: D'oh!", "Lisa: A deer!", "Marge: A female deer!"]

for line in doh():
    print(line)

# Homer: D'oh!
# Lisa: A deer!
# Marge: A female deer!
```

```python
# 2. yield 사용
def doh2():
    # 그때그때 소모하고 중지, 이후 이어나감.
    yield "Homer: D'oh!"
    yield "Lisa: A deer!"
    yield "Marge: A female deer!"

for line in doh2():
    print(line)

# Homer: D'oh
# Lisa: A deer!
# Marge: A female deer!
```

<br>

<h2>2-7. 파이썬의 async, await, asyncio</h2>
<ul>
  <li>
    대부분의 시간을 대기하는 데 <strong>소비해야 하는 함수 앞에 await</strong>를 추가하고 <strong>함수는 def 앞에 async</strong>가 있어야 한다.
  </li>
    <ul>
      <li>
        함수를 선언할 때 <strong>async def를 사용</strong>하면 호출할 때 <strong>await을 추가</strong>해야 한다.
      </li>
      <li>
        호출 코드가 포함된 함수 자체도 async def로 선언해야 하며 이를 호출하는 쪽 또한 await을 추가한다.
      </li>
    </ul>
</ul>

```python
# 1. time을 통한 동기 수행.
import time

def q():
    print("시트웰: 답이 하나도 안 맞잖아?")
    time.sleep(3)

def a():
    print("로저스: 하지만 빨랐죠.")

def main():
    q()
    a()

main

# < 동기식이기에 time.sleep을 기다린뒤 3초후 대답한다. >
# 시트웰: 답이 하나도 안 맞잖아?
# ... 3초 후
# 로저스: 하지만 빨랐죠?
```

```python
# 2. asyncio를 활용한 비동기 수행
import asyncio

async def q():
    print("시트웰: 답이 하나도 안 맞잖아?")
    await asyncio.sleep(3)

async def a():
    print("로저스: 하지만 빨라죠.")

async def main():
    await asyncio.gather(q(), a())

asyncio.run(main())

# < 비동기식 이기에 q()의 asyncio.sleep(3)을 건너뛰어 값을 반환하고 3초가 지난다. >
# 시트웰: 답이 하나도 안 맞잖아?
# 로저스: 하지만 빨랐죠.
# ... 3초 정적
```

<br><br>

<h1>3. FastAPI와 Async</h1>
<ul>
  <li>
    웹 서버는 대기에 소모하는 시간이 길어 이를 해결하는 것이 중요한데 <strong>FastAPI</strong>는 Starlette 패키지가 ASGI를 지원하기에 <strong>비동기 코드</strong>를 사용할 수 있다.
  </li>
    <ul>
      <li>
        비동기는 주로 <strong>I/O</strong>를 오래 기다리지 않기 위해 사용한다.
      </li>
    </ul>
  <li>
    <strong>URL을 코드에 대응시키는 함수</strong>를 FastAPI 문서에서 <strong>경로 함수(path functions)</strong>라 한다. 저자는 이를 웹 엔드포인트(web endpoint)라고도 한다.
  </li>
</ul>

```python
# 1. 실습 코드를 비동기로 변환.
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/hi")
async def greet():
    # sleep(1)을 통해 I/O 시간을 대체 구현
    await asyncio.sleep(1)
    return "Hello? World?"
```

<br><br>

<h1>4. 직접 사용하기</h1>
<ul>
  <li>
    FastAPI는 API를 만들 때 Starlette 보다 <strong>Pydantic</strong>을 더 사용한다.
  </li>
</ul>

```python
# 1. 직접 Starlette을 사용하는 예
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def greeting(request):
    return JSONResponse('Hello? World?')

app = Starlette(debug=True, routes=[
    Route('/hi', greeting),
])
```