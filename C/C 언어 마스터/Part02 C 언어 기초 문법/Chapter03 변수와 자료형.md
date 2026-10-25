<h1>1. 변수</h1>
<h2>1-1. 변수의 개념</h2>
<ul>
  <li>
    <strong>변수(variable)</strong>는 컴퓨터 프로그램이 실행되는 동안 <strong>데이터를 저장</strong>하고 그 데이터를 <strong>참조</strong>하거나 <strong>수정</strong>하기 위해 사용하는 <strong>식별자</strong>를 의미한다.
  </li>
    <ul>
      <li>
        데이터 입력, 연산 처리 등의 결과를 저장할 메모리이다.
      </li>
    </ul>
  <li>
    변수를 선언하면 <strong>메모리 공간에 할당</strong>되고 해당 <strong>메모리 위치에 데이터가 저장</strong>된다.
  </li>
    <ul>
      <li>
        선언된 변수는 자료형의 크기만큼 <strong>RAM(Random Access Memory)</strong>에 공간을 할당받고 변수의 값이 저장된다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 변수의 사용</h2>
<ul>
  <li>
    변수의 사용은 크게 변수의 이름과 자료형을 지정하여 변수를 생성하는 <strong>변수 선언 과정</strong>과 생성한 변수에 초깃값을 할당하는 <strong>변수 초기화 과정</strong> 두 가지로 나눌 수 있다.
  </li>
</ul>

<h3>1-2-1. 변수 선언</h3>

```C
// 1. 기본적인 변수 선언 형식
// 자료형 변수명;
int var;

// 2. 예.
int myVariable;    // 정수형 변수 선언.
myVariable = 17;   // 변수에 정수 17 대입.
```

<h3>1-2-2. 변수 초기화</h3>
<ul>
  <li>
    변수 초기화는 변수를 선언하는 동시에 <strong>초깃값을 할당</strong>하는 것을 의미한다.
  </li>
  <li>
    C 언어에서는 일반적으로 이전에 어떤 프로그램의 변수가 메모리를 사용했는지 알 수 없기 때문에 메모리 안에 쓰레깃값이 저장되어 있을 수 있다. 따라서 <strong>변수 선언 뒤에는 반드시 값을 할당</strong>하여 오류를 방지하는 것이 좋다.
  </li>
</ul>

```C
// 1. 변수 초기화 형식
// 자료형 변수명 = 값;
int xNum = 0;
double yNum = 3.3;
```

<h3>1-2-3. 변수명 작성</h3>
<ul>
  <li>
    기본적인 변수명 작성 규칙
  </li>
    <ul>
      <li>
        영문자(대, 소문자), 숫자, 언더바(_)를 사용할 수 있다.
      </li>
      <li>
        변수명의 첫 글자는 숫자로 싲가할 수 없다.
      </li>
      <li>
        대문자와 소문자를 구분한다.
      </li>
      <li>
        변수명 중간에 공백을 사용할 수 없다.
      </li>
      <li>
        C 언어의 예약어를 사용할 수 없다.
      </li>
        <ul>
          <li>
            예약어에 특수문자를 넣어 변수명을 지을 수 있지만 권장하지 않음.
          </li>
        </ul>
    </ul>
  <li>
    대표적인 변수명 관례
  </li>
    <ul>
      <li>
        <strong>카멜 표기법(camal case)</strong>: 여러 단어로 이루어진 변수명의 경우 각 단어의 첫 글자를 <strong>대문자</strong> 또는 <strong>소문자</strong>로 표기하고 <strong>언더바 없이</strong> 단어들을 연결한다.
      </li>
      <li>
        <strong>스네이크 표기법(snake case)</strong>: 여러 단어로 이루어진 변수명에서 각 단어를 <strong>언더바로 구분</strong>한다.
      </li>
      <li>
        <strong>대문자 스네이트 표기법(upper snake case)</strong>: 대문자 상수 표기법이라고도 하며, <strong>상수를 나타내는 변수명</strong>에 사용된다. <strong>모든 글자를 대문자</strong>로 표기하고 각 단어를 <strong>언더바로 구분</strong>한다.
      </li>
    </ul>
</ul>

<h3>1-2-4. 변수를 사용하는 이유</h3>
<ul>
  <li>
    값을 저장하는 메모리 공간으로 사용한다.
  </li>
  <li>
    데이터 유지와 재사용이 가능하다.
  </li>
  <li>
    효율적인 계산과 연산이 가능하다.
  </li>
  <li>
    프로그램 상태 표현에 사용한다.
  </li>
</ul>

<br><br>

<h1>2. 자료형</h1>
<h2>2-1. 자료형의 개념</h2>
<ul>
  <li>
    <strong>자료형(data type)</strong>은 변수에 데이터를 저장할 때 <strong>데이터의 종류와 크기</strong>를 정의하는 단위를 의미한다. (p100 참고).
  </li>
</ul>

<br>

<h2>2-2. 자료형의 종류</h2>
<ul>
  <li>
    자료형의 종류는 p101의 테이블을 참고.
  </li>
  <li>
    변수를 선언할 때 자료형과 저장되는 <strong>값의 범위</strong>가 맞지 않으면 메모리 공간을 할당할 때 오류가 발생한다.
  </li>
</ul>

<br>

<h2>2-3. 정수형</h2>
<h3>2-3-1. 정수형의 종류와 유효 범위</h3>
<ul>
  <li>
    <strong>정수형(integer type)</strong>은 프로그래밍에서 사용하는 변수의 유형 중 하나로 <strong>정수(양수, 0, 음수)</strong>를 표현하기 위한 자료형이다.
  </li>
  <li>
    C 언어에서 제공하는 정수형은 메모리 <strong>저장 공간의 크기</strong>와 <strong>표현할 수 있는 범위</strong>에 따라 short, int, long, long long으로 구분된다.
  </li>
    <ul>
      <li>
        메모리 저장 공간의 크기는 곧 표현할 수 있는 범위를 나타낸다. (p103 테이블 참고).
      </li>
    </ul>
  <li>
    실습 코드는 'Practice/Ch03/ex03_01.c'에 있다.
  </li>
</ul>

<h3>2-3-2. sizeof 연산자</h3>
<ul>
  <li>
    sizeof 연산자는 주어진 변수나 자료형의 크기를 <strong>바이트 단위</strong>로 알려준다.
  </li>
  <li>
    sizeof 연산자로 확인한 크기는 컴파일 시에 확정된다.
  </li>
    <ul>
      <li>
        컴파일러가 연산자를 분석하고 실행 파일을 생성할 때 이미 크기 정보를 결정하고 할당하기 때문이다.
      </li>
    </ul>
  <li>
    sizeof 연산자는 동적 메모리 할당, 자료의 크기 등을 확인할 수 있어 유용하게 사용되는 연산자이다.
  </li>
  <li>
    실습 코드는 Pratice/Ch03/ex03_02.c에 있다.
  </li>
</ul>

```text
sizeof(피연산자);  // 자료형, 변수, 상수도 사용 가능.  
sizeof 변수명;  // 자료형 사용 불가
```
<h3>2-3-3. 정수형의 부호</h3>
<ul>
  <li>
    정수형 변수를 선언할 때에는 <strong>부호</strong>를 생략할지 말지 결정해야 한다. C 언어에서는 <strong>signed</strong>와 <strong>unsigned</strong>로 부호 생략 여부를 결정한다.
  </li>
    <ul>
      <li>
        부호의 생략 여부에 따라 표현할 수 있는 <strong>정수의 범위</strong>가 달라진다.
      </li>
      <li>
        <strong>부호에 할당되는 비트</strong> 뿐만 아니라 표현되는 범위에 <strong>음수의 포함여부</strong>도 영향을 준다.
      </li>
    </ul>
</ul>

<h3>2-3-4. 부호 있는 정수 signed</h3>
<ul>
  <li>
    <strong>signed</strong> 키워드는 부호 있는 정수를 나타내며 양수, 0, 음수를 포함하는 <strong>모든 정숫값</strong>을 저장할 수 있다.
  </li>
  <li>
    signed int는 signed를 생략하고 int로 표현한다.
  </li>
  <li>
    부호 비트를 제외한 나머지 비트로 데이터를 표현하기 때문에 -2의 31승부터 2의 31승 -1까지 표현이 가능하다.
  </li>
  <li>
    signed int의 크기는 운영체제에 따라 다를 수 있지만 대개 2바이트 또는 4바이트이다.
  </li>
</ul>

<h3>2-3-5. 부호 없는 정수 unsigned</h3>
<ul>
  <li>
    <strong>unsigned</strong> 키워드는 부호 없는 정수로 <strong>0</strong>과 <strong>양수</strong>만 저장할 수 있다.
  </li>
  <li>
    부호 없이 32비트 모두 데이터를 표현하기 때문에 0부터 2의 32승 -1까지 표현이 가능하다.
  </li>
</ul>

```C
signed int myNumber = -1024;
unsigned int positiveNumber = 1024;
```

<h3>2-3-6. 오버플로</h3>
<ul>
  <li>
    <strong>오버플로(overflow)</strong>란 선언된 변수 자료형의 <strong>범위를 초과</strong>하는 값을 저장할 때 발생하는 현상이다.
  </li>
  <li>
    변수 범위에서 오버플로가 발생하면 다시 처음으로 돌아가게 되는데 이 연산을 <strong>롤오버(rollover)</strong>라 한다.
  </li>
  <li>
    실습 코드는 'Practice/Ch03/ex03_03.c'에 있다.
  </li>
</ul>

<h3>2-3-7. 언더플로</h3>
<ul>
  <li>
    언더플로(underflow)는 변수로 선언한 자료형의 유효 범위보다 <strong>더 작은 값이 대입</strong>될 때 발생하는 현상이다.
  </li>
  <li>
    마찬가지로 언더플로가 발생하면 최댓값으로 롤오버가 된다.
  </li>
  <li>
    실습 코드는 'Practice/Ch03/ex03_04.c'에 있다.
  </li>
</ul>

<br>

<h2>2-4. 실수형</h2>
<h3>2-4-1. 실수형의 종류와 유효 범위</h3>
<ul>
  <li>
    <strong>실수형(float type)</strong>은 소수점이 있는 수를 저장하기 위한 자료형으로, <strong>부동 소수점 방식</strong>으로 수를 표현한다.
  </li>
    <ul>
      <li>
        부동 소수점 방식(floating-point system)은 소수점의 위치를 고정하지 않고 <strong>가수</strong>와 <strong>지수</strong>를 이용하여 실수를 표현하는 것을 의미한다.
      </li>
      <li>
        가수는 유효 숫자를, 지수는 소수점의 위치를 나타낸다. 
      </li>
    </ul>
  <li>
    C 언어에서 실수형은 <strong>float</strong>, <strong>double</strong>, <strong>long double</strong>로 구분된다.
  </li>
    <ul>
      <li>
        <strong>float</strong>: <strong>단정밀도 부동 소수점 수</strong>를 저장하는 데 사용되는 자료형으로 일반적인 크기는 <strong>4바이트</strong>이고 약 <strong>6~7자리의 유효 숫자</strong>를 저장할 수 있다.
      </li>
      <li>
        <strong>double</strong>: 배정밀도 부동 소수점 수를 저장하는 데 사용되는 자료형으로 일반적인 크기는 <strong>8바이트</strong>이다. <strong>15~16자리의 유효 숫자</strong>를 저장할 수 있다.
      </li>
      <li>
        <strong>long double</strong>: double형보다 더 큰 범위와 정밀도의 부동 소수점 수를 저장하는 데 사용되는 자료형이다. 일반적인 크기는 <strong>8바이트 이상</strong>이며 시스템에 따라 10바이트 또는 16바이트가 될 수도 있다. <strong>정밀도는 18자리 이상</strong>이다.
      </li>
    </ul>
  <li>
    자세한 내용은 p110의 테이블을 참고.
  </li>
  <li>
    실습 코드는 'Practice/Ch03/ex03_05.c'와 'Practice/Ch03/ex03_06.c'에 있다.
  </li>
</ul>

<br>

<h2>2-5. 문자형</h2>
<ul>
  <li>
    
  </li>
</ul>