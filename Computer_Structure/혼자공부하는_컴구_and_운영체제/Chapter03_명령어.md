<h1>1. 소스 코드와 명령어</h1>
<ul>
  <li>
    C, C++, Java, Python과 같은 다양한 언어가 있지만 결국 모든 언어의 소스 코드는 <strong>컴퓨터 내부</strong>에서 <strong>명령어로 변환</strong>횐다.
  </li>
</ul>

<br>

<h2>1-1. 고급 언어와 저급 언어</h2>
<ul>
  <li>
    사람이 이해하고 작성하기 쉽게 만들어진 <strong>사람</strong>을 위한 언어를 <strong>고급 언어(high-level programming language)</strong>라 한다.
  </li>
  <li>
    반대로 <strong>컴퓨터</strong>가 직접 이해하고 실행할 수 있는 언어를 <strong>저급 언어(low-level programming language)</strong>라 한다.
  </li>
  <li>
    컴퓨터가 이해하고 실행할 수 있는 언어는 오직 저급 언어이기 때문에 고급 언어로 작성된 소스 코드가 실행되려면 반드시 <strong>저급 언어(명령어)</strong>로 변환되어야 한다.
  </li>
  <li>
    저급 언어에는 두 가지 종류가 있다. 하나는 <strong>기계어</strong>이고 다른 하나는 <strong>어셈블리어</strong>이다.
  </li>
    <ul>
      <li>
        <strong>기계어(machine code)</strong>란 <strong>0과 1의 명령어 비트</strong>로 이루어진 언어이다.
      </li>
      <li>
        <strong>어셈블리어(assembly language)</strong>는 0과 1(기계어)로 표현된 읽기힘든 명령어를 <strong>읽기 편한 형태</strong>로 번역한 언어이다.
      </li>
    </ul>
  <li>
    어셈블리어는 기계어보다는 비교적 보기 편해졌지만, 사람이 이를 사용하여 프로그래밍을하기에는 쉽지 않다. 따라서 <strong>고급 언어</strong>가 필요하다.
  </li>
  <li>
    하지만 하드웨어와 밀접하게 개발을 하는 <strong>임베디드 개발자, 게임 개발자, 정보 보안 분야 등의 개발자</strong>는 어셈블리어를 많이 이용한다.
  </li>
    <ul>
      <li>
        또한 어셈블리어는 작성의 대상이면서 관찰의 대상이 된다. 즉 프로그램이 어떤 절차로 작동하는지를 가장 근본적인 단계부터 추적할고 관찰할 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 컴파일 언어와 인터프리터 언어</h2>
<ul>
  <li>
    고급 언어가 저급 언어로 변환되는 방식에는 두 가지가 있다. 하나는 <strong>컴파일 방식</strong>이고 다른 하나는 <strong>인터프리트 방식</strong>이다.
  </li>
  <li>
    컴파일 방식으로 작동하는 프로그래밍 언어를 <strong>컴파일 언어</strong>, 인터프리트 방식으로 작동하는 프로그래밍 언어를 <strong>인터프리터 언어</strong>라고 한다.
  </li>
</ul>

<h3>1-2-1. 컴파일 언어</h3>
<ul>
  <li>
    컴파일 언어는 컴파일러에 의해 소스 코드 전체가 저급 언어로 변환되어 실행되는 고급 언어이다.
  </li>
  <li>
    컴파일 언어가 저급 언어로 변환되는 과정을 <strong>컴파일(compile)</strong>이라 한다.
  </li>
  <li>
    컴파일을 수행해 주는 도구를 <strong>컴파일러(compiler)</strong>라고 한다.
  </li>
    <ul>
      <li>
        컴파일러는 개발자가 작성한 소스 코드 전체를 훑어보며 소스 코드에 <strong>문법적 오류, 실행 가능성, 불필요한 코드</strong>를 점검하며 저급 언어로 컴파일 한다.
      </li>
      <li>
        컴파일러가 소스 코드 내에서 오류를 하나라도 발견한다면 해당 소스 코드는 <strong>컴파일에 실패</strong>한다.
      </li>
    </ul>
  <li>
    컴파일이 성공적으로 완료되어 저급 언어로 변환된 코드를 <strong>목적 코드(object code)</strong>라 한다.
  </li>
</ul>

<h3>1-2-2. 인터프리터 언어</h3>
<ul>
  <li>
    인터프리터 언어는 인터프리터에 의해 소스 코드가 <strong>한 줄씩 실행</strong>되는 고급 언어이다. 대표적으로 Python이 있다.
  </li>
  <li>
    소스 코드를 한 줄씩 저급 언어로 변환하여 실행해 주는 도구를 <strong>인터프리터(interpreter)</strong>라 한다.
  </li>
    <ul>
      <li>
        인터프리터 언어는 컴퓨터와 대화하듯 소스 코드를 한 줄씩 실행하기 때문에 소스 코드 전체를 <strong>저급 언어로 변환하는 시간</strong>을 기다릴 필요가 없다.
      </li>
    </ul>
  <li>
    소스 코드 내에 오류가 있는 경우 컴파일이 불가능한 컴파일 언어와 달리 인터프리터 언어는 소스 코드를 한 줄씩 실행하기 때문에 N번째 줄에 문법 오류가 있어도 <strong>N-1번째 줄까지는 올바르게 수행</strong>된다.
  </li>
  <li>
    일반적으로 컴파일 언어는 미리 기계어로 변환해 두어 한 줄씩 변환하며 실행하는 인터프리터 언어보다 빠르다.
  </li>
  <li>
    정확히는 컴파일 언어와 인터프리터 언어를 명확히 구분하기에는 <strong>모호</strong>하다.
  </li>
    <ul>
      <li>
        C와 C++은 비교적 명확하다. 그러나 Python은 컴파일을 아예 하지 않는 것은 아니고 Java 또한 저급 언어로 변환되는 과정에서 컴파일과 인터프리트를 동시에 수행한다.
      </li>
      <li>
        즉 프로그래밍 언어가 반드시 하나의 방식으로 작동한다 생각하는 것은 오개념이다.
      </li>
      <li>
        핵심은 고급 언어가 저급 언어로 변환되는 대표적인 방법에 <strong>컴파일 방식</strong>과 <strong>인터프리트 방식</strong>이 있음 정도로 이해하는 것이다.
      </li>
    </ul>
</ul>

<h4>1-2-2-1. 목적 파일 vs 실행 파일</h4>
<ul>
  <li>
    목적 코드로 이루어진 파일을 <strong>목적 파일</strong>이라 부르고, 실행 코드로 이루어진 파일을 <strong>실행 파일</strong>이라 부른다.
  </li>
    <ul>
      <li>
        윈도우의 .exe 확장자를 가진 파일이 대표적인 실행 파일이다.
      </li>
    </ul>
  <li>
    목적 코드는 저급 언어이지만 실행 파일이 되기 위해서는 <strong>링킹</strong>이라는 작업을 거쳐야 한다.
  </li>
    <ul>
      <li>
        컴파일 언어로 파일을 작성한 뒤 목적 파일로 변환 후에는 실행되기 위해 다른 파일들을 연결해야하는 작업이 필요할 수 있다. 이렇게 연결하는 작업을 <strong>링킹(linking)</strong>이라 한다.
      </li>
        <ul>
          <li>
            넓은 의미에서 의존성을 연결한다고 볼 수 있다.
          </li>
        </ul>
      <li>
        컴파일 언어 -> 목적 코드 -> 링킹 -> 실행 파일
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 명령어 구조</h1>
<h2>2-1. 연산 코드와 오퍼랜드</h2>
<ul>
  <li>
    명령어는 <strong>무엇을 대상</strong>으로 <strong>어떤 작동을 수행</strong>하라는 구조로 되어있다.
  </li>
  <li>
    명령어는 <strong>연산 코드</strong>와 <strong>오퍼랜드</strong>로 구성되어 있다.
  </li>
    <ul>
      <li>
        연산 코드(operation code)는 <strong>명령어가 수행할 연산</strong>이며 <strong>연산자</strong>라고도 부른다.
      </li>
      <li>
        오퍼랜드(operand)는 연산엔 사용할 <strong>데이터가 저장된 위치</strong>이며 <strong>피연산자</strong>라고도 부른다.
      </li>
    </ul>
  <li>
    명령어에서 연산 코드가 담기는 영역을 <strong>연산 코드 필드</strong>, 오퍼랜드가 담기는 영역을 <strong>오퍼랜드 필드</strong>라고 한다.
  </li>
</ul>

```asm
; '연산 코드 + 오퍼랜드' 구조이다.
push    rbp
mov     rbp, rsp
mov     DWORD PTR [rbp-4], 1
mov     DWORD PTR [rbp-8], 2
mov     edx, DWORD PTR [rbp-4]
mov     eax, DWORD PTR [rbp-8]
add     eax, edx
mov     DWORD PTR [rbp-12], eax
```

<h3>2-1-1. 오퍼랜드</h3>
<ul>
  <li>
    오퍼랜드는 연산에 사용할 <strong>데이터</strong> 혹은 연산에 사용할 <strong>데이터가 저장된 위치</strong>를 의미한다.
  </li>
    <ul>
      <li>
        따라서 숫자와 문자 등을 나타내는 <strong>데이터</strong>나 <strong>레지스터 주소</strong>가 올 수 있다.
      </li>
    </ul>
  <li>
    일반적으로는 데이터를 직접 명시하기보다 <strong>메모리 주소</strong>나 <strong>레지스터 이름</strong>이 담긴다.
  </li>
    <ul>
      <li>
        따라서 오퍼랜드의 필드를 <strong>주소 필드</strong>라고 부른다.
      </li>
    </ul>
  <li>
    오퍼랜드는 명령어 안에 하나도 없을 수도 있고, 한 개 이상 존재할 수도 있다.
  </li>
    <ul>
      <li>
        오퍼랜드가 하나도 없는 명령어를 <strong>0-주소 명령어</strong>라 한다.
      </li>
      <li>
        오퍼랜드가 하나인 명령어를 <strong>1-주소 명령어</strong>, 두 개인 명령어를 <strong>2-주소 명령어</strong>, 세 개인 명령어를 <strong>3-주소 명령어</strong>라 한다.
      </li>
    </ul>
</ul>

```asm
; 1. 오퍼랜드가 두 개인 경우.
mov    eax, 0

; 2. 오퍼랜드가 한 개인 경우.
pop    rbp

; 3. 오퍼랜드가 없는 경우.
ret
```

<h3>2-1-2. 연산 코드</h3>
<ul>
  <li>
    연산 코드의 종류는 많지만 크게 다음의 네 가지로 나눌 수 있다.
  </li>
    <ul>
      <li>
        <strong>데이터 전송</strong>
      </li>
        <ul>
          <li>
            <strong>MOVE</strong>: 데이터를 옮겨라.
          </li>
          <li>
            <strong>STORE</strong>: 메모리에 저장하라.
          </li>
          <li>
            <strong>LOAD(FETCH)</strong>: 메모리에서 CPU로 데이터를 가져와라.
          </li>
          <li>
            <strong>PUSH</strong>: 스택에 데이터를 저장하라.
          </li>
          <li>
            <strong>POP</strong>: 스택의 최상단 데이터를 가져와라.
          </li>
        </ul>
      <li>
        <strong>산술/논리 연산</strong>
      </li>
        <ul>
          <li>
            <strong>ADD / SUBTRACT / MULTIPLY / DIVIDE</strong>: 덧셈 / 뺄셈 / 곱셈 / 나눗셈을 수행하라.
          </li>
          <li>
            <strong>INCREMENT / DECREMENT</strong>: 오퍼랜드에 1을 더하라 / 오퍼랜드에 1을 빼라.
          </li>
          <li>
            <strong>AND / OR / NOT</strong>: AND / OR / NOT 연산을 수행하라.
          </li>
          <li>
            <strong>COMPARE</strong>: 두 개의 숫자 또는 TRUE / FALSE 값을 비교하라.
          </li>
        </ul>
      <li>
        <strong>제어 흐름 변경</strong>
      </li>
        <ul>
          <li>
            <strong>JUMP</strong>: 특정 주소로 실행 순서를 옮겨라.
          </li>
          <li>
            <strong>CONDITIONAL JUMP</strong>: 조건에 부합할 때 특정 주소로 실행 순서를 옮겨라.
          </li>
          <li>
            <strong>HALF</strong>: 프로그램의 실행을 멈춰라.
          </li>
          <li>
            <strong>CALL</strong>: 되돌아올 주소를 저장한 채 특정 주소로 실행 순서를 옮겨라.
          </li>
          <li>
            <strong>RETURN</strong>: CALL을 호출할 때 저장했던 주소로 돌아가라.
          </li>
        </ul>
      <li>
        <strong>입출력 제어</strong>
      </li>
        <ul>
          <li>
            <strong>READ(INPUT)</strong>: 특정 입출력 장치로부터 데이터를 읽어라.
          </li>
          <li>
            <strong>WRITE(OUTPUT)</strong>: 특정 입출력 장치로 데이터를 써라.
          </li>
          <li>
            <strong>START IO</strong>: 입출력 장치를 시작하라.
          </li>
          <li>
            <strong>TEST IO</strong>: 입출력 장치의 상태를 확인하라.
          </li>
        </ul>
    </ul>
  <li>
    명령어의 종류와 생김세는 CPU마다 다르기 때문에 연산 코드의 종류와 생김새 또한 CPU마다 다르다. 따라서 전부 암기할 필요는 없다.
  </li>
</ul>

<br>

<h2>2-2. 주소 지정 방식</h2>
<ul>
  <li>
    데이터가 아닌 메모리나 레지스터의 주소를 오퍼랜드 필드에 담는 것은 <strong>명령어 길이</strong> 때문이다. (비트의 크기).
  </li>
    <ul>
      <li>
        하나의 명령어가 n비트로 구성되고 이중 연산 코드 필드가 m비트라면 오퍼랜드 필드의 최대 크기는 <strong>n-m비트</strong>가 된다.
      </li>
      <li>
        심지어 3-주소 명령어의 경우 각 오퍼랜드 필드가 가질 수 있는 <strong>크기는 더욱 작아진다</strong>.
      </li>
      <li>
        오퍼랜드 필드의 크기(비트)가 작아진다는 것은 결국 <strong>표현할 수 있는 정보의 수</strong>가 적어진다는 것이고, 따라서 데이터를 직접적으로 표현하기 보다 <strong>주소로 연결</strong>하는 것이다.
      </li>
    </ul>
  <li>
    오퍼랜드 필드에 메모리 주소나 레지스터 주소를 명시하면 표현할 수 있는 정보는 <strong>해당 메모리 주소</strong> 혹은 <strong>레지스터 주소의 크기</strong>만큼이 된다.
  </li>
  <li>
    연산 코드가 사용할 데이터가 저장되는 위치를 <strong>유효 주소(effective address)</strong>라 한다.
  </li>
  <li>
    오퍼랜드 필드에 데이터가 저장된 위치를 명시할 때 연산에 사용할 <strong>데이터 위치를 찾는 방법</strong>을 <strong>주소 지정 방식(addressing mode)</strong>이라고 한다.
  </li>
    <ul>
      <li>
        즉 주소 지정 방식은 유효 주소를 찾는 방법이다.
      </li>
    </ul>
  <li>
    현대 CPU는 다양한 주소 지정 방식을 사용한다.
  </li>
</ul>

<h3>2-2-1. 즉시 주소 지정 방식</h3>
<ul>
  <li>
    <strong>즉시 주소 지정 방식(immediate addressing mode)</strong>은 연산에 사용할 데이터를 오퍼랜드 필드에 <strong>직접 명시</strong>하는 방법이다.
  </li>
    <ul>
      <li>
        주소가 아닌 데이터를 명시하기에 주소라 하는 게 맞나 생각된다.
      </li>
    </ul>
  <li>
    <strong>데이터를 직접 명시</strong>하기 때문에 메모리나 레지스터로 찾는 과정이 없고 그만큼 다른 방식들보다 <strong>빠르다는 장점</strong>이 있다.
  </li>
</ul>

<h3>2-2-2. 직접 주소 지정 방식</h3>
<ul>
  <li>
    <strong>직접 주소 지정 방식(direct addressing mode)</strong>은 오퍼랜드 필드에 <strong>유효 주소</strong>를 직접적으로 명시하는 방식이다.
  </li>
  <li>
    데이터가 있는 곳의 주소를 명시하기 때문에 직접 데이터를 명시하는 것보다 <strong>오퍼랜드 필드의 크기 압박은 줄어들지만</strong> 주소 또한 오퍼랜드 필드 크기의 영향을 받는 것은 여전하다.
  </li>
</ul>

<h3>2-2-3. 간접 주소 지정 방식</h3>
<ul>
  <li>
    간접 주소 지정 방식(indirect addressing mode)은 <strong>유효 주소의 주소</strong>를 오퍼랜드 필드에 명시한다.
  </li>
  <li>
    주소의 주소를 명시하기 때문에 직접 주소 지정 방식 보다는 더 <strong>오퍼랜드 필드의 공간이 여유롭다</strong>는 장점이 있다.
  </li>
  <li>
    다만 <strong>두 번의 메모리 접근</strong>이 필요하기 때문에 앞서 다룬 주소 지정 방식들보다 느리다는 단점이 존재한다.
  </li>
</ul>

<h3>2-2-4. 레지스터 주소 지정 방식</h3>
<ul>
  <li>
    <strong>레지스터 주소 지정 방식(register addressing mode)</strong>은 직접 주소 지정 방식과 비슷하게 연산에 사용할 <strong>데이터를 저장한 레지스터</strong>를 오퍼랜드 필드에 직접 명시한다.
  </li>
  <li>
    일반적으로 CPU 외부에 있는 메모리에 접근하는 것보다 <strong>CPU 내부에 있는 레지스터</strong>에 접근하는 것이 더 빠르다.
  </li>
    <ul>
      <li>
        즉 직접 주소 지정 방식보다 빠름을 의미한다.
      </li>
    </ul>
  <li>
    직접 주소 지정 방식보다 빠르지만 레지스터 주소 지정 방식 또한 주소를 명시한다는 점에서 <strong>오퍼랜드 필드 크기에 영향</strong>을 받는다.
  </li>
</ul>

<h3>2-2-5. 레지스터 간접 주소 지정 방식</h3>
<ul>
  <li>
    <strong>레지스터 간접 주소 지정 방식(register indirect addressing mode)</strong>은 연산에 사용할 <strong>데이터를 메모리</strong>에 저장하고 <strong>해당 주소(유효 주소)를 저장한 레지스터</strong>를 오퍼랜드 필드에 명시하는 방법이다.
  </li>
  <li>
    유효 주소를 찾는 과저이 간접 주소 지정 방식과 비슷하지만, <strong>메모리 접근하는 횟수가 한 번</strong>으로 줄어든다는 장점이 있다.
  </li>
    <ul>
      <li>
        따라서 레지스터 간접 주소 지정 방식이 간접 주소 지정 방식보다 빠르다.
      </li>
    </ul>
</ul>

<h4>좀 더 알아보기. 스택과 큐</h4>
<ul>
  <li>
    <strong>스택(stack)</strong>이란 한쪽 끝이 막혀 있는 통과 같은 저장 공간이다.
  </li>
  <li>
    나중에 저장한 데이터를 가장 먼저 빼내는 데이터 관리 방식(후입선출)이라는 점에서 <strong>LIFO(Last In First Out)</strong> 자료 구조라고도 부른다.
  </li>
  <li>
    스택에 새로운 데이터를 저장하는 명령어는 <strong>PUSH</strong>, 스택에 저장된 데이터를 꺼내는 명령어는 <strong>POP</strong>이다.
  </li>
  <li>
    스택과 달리 양쪽이 뚫려 있는 통과 같은 저장 공간을 <strong>큐(queue)</strong>라고 한다.
  </li>
  <li>
    큐는 가장 먼저 저장된 데이터부터 빼내는 데이터 관리 방식(선입선출)이라는 점에서 <strong>FIFO(First In First Out)</strong> 자료 구조라고도 부른다.
  </li>
</ul>