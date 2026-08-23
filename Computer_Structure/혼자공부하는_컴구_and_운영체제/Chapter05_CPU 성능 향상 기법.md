<h1>1. 빠른 CPU를 위한 설계 기법</h1>
<h2>1-1. 클럭</h2>
<ul>
  <li>
    클럭은 컴퓨터 부품들이 작업을 하는 주기이며 클럭 속도가 높으면 빠른 주기로 작업을 하는 것이기에 일반적으로 CPU의 성능이 좋다.
  </li>
    <ul>
      <li>
        클럭 속도는 CPU 속도 단위로 간주되기도 한다.
      </li>
    </ul>
  <li>
    <strong>클럭 속도</strong>는 <strong>헤르츠(Hz) 단위</strong>로 측정한다.
  </li>
    <ul>
      <li>
        헤르츠는 <strong>초당 클럭이 몇 번 반복</strong>되는지를 의미한다. 예를 들어 1초에 1회 클럭이 반복되면 1Hz이다.
      </li>
      <li>
        intel의 경우 Base 2.5GHz, Max 4.9GHz인데 이는 기본적으로 25억(2.5 * 10^9)번, 최대 49억(4.9 * 10^9)번 반복됨을 의미한다.
      </li>
    </ul>
  <li>
    오해하지 말아야 할 점은 클럭 속도는 <strong>일정하지 않다</strong>는 점이다. 따라서 보통 위와 같이 기본과 최대로 분리된다.
  </li>
    <ul>
      <li>
        고성능을 요하는 순간에는 클럭 속도를 높이는데 이때 최대 클럭 속도를 강제로 올릴 수 있는데 이 기법을 <strong>오버클럭킹(overclocking)</strong>이라 한다.
      </li>
    </ul>
  <li>
    클럭 속도를 높이면 성능이 좋아지긴 하지만 <strong>발열 문제</strong>가 심각해지며 따라서 클럭만으로 CPU 성능을 올리는 데에는 한계가 있다.
  </li>
</ul>

<br>

<h2>1-1. 코어와 멀티코어</h2>
<ul>
  <li>
    클럭 속도 외에 CPU의 성능을 높이는 방법에는 대표적으로 CPU의 <strong>코어</strong>와 <strong>스레드 수</strong>를 늘리는 방법이 있으며 이번 절에서는 <strong>코어</strong>에 대해 알아본다.
  </li>
  <li>
    전통적인 관점에서 CPU가 명령어를 실행하는 부품이라는 점은 맞으나 기술이 발전하며 CPU 내부에는 <strong>명령어를 실행하는 다수의 부품</strong>을 넣을 수 있게 되었다.
  </li>
    <ul>
      <li>
        따라서 우리가 지금까지 CPU의 정의로 알고 있던 명령어를 실행하는 부품이라는 의미는 오늘날에 <strong>코어(core)</strong>라는 용어로 사용된다.
      </li>
      <li>
        마찬가지로 오늘날 CPU는 <strong>명령어를 실행하는 부품을 여러 개 포함하는 부품</strong>으로 명칭의 범위가 확장되었다.
      </li>
        <ul>
          <li>
            <strong>ALU, 제어장치, 레지스터</strong>도 각 코어에 포함된다.
          </li>
        </ul>
    </ul>
  <li>
    코어를 여러 개 포함하고 있는 CPU를 <strong>멀티코어(multi-core) CPU</strong> 또는 <strong>멀티코어 프로세서</strong>라고 부른다.
  </li>
    <ul>
      <li>
        당연히 단일 코어의 클럭 속도가 빠르더라도 조금 속도가 낮은 멀티코어 CPU의 속도가 더 빠르다.
      </li>
      <li>
        CPU 종류는 CPU 안에 코어가 몇 개 포함되어 있는지에 따라 다르다. (p147 참고).
      </li>
    </ul>
  <li>
    CPU의 코어를 무작정 늘린다해도 성능이 선형적으로 증가하는 것은 아니다.
  </li>
    <ul>
      <li>
        각 코어에 처리해야할 <strong>연산이 적절히 분배</strong>되지 않는다면 코어 수에 비례해 연산 속도가 증가하지 않는다.
      </li>
      <li>
        또한 처리하고자 하는 적업량보다 코어 수가 지나치게 많은 경우에도 <strong>노는 코어</strong>가 발생하기 때문에 적합하지 않다.
      </li>
    </ul>
  <li>
    중요한 것은 코어마다 <strong>처리할 명령어들을 얼마나 적덜하게 분배</strong>하느냐이다.
  </li>
</ul>

<br>

<h2>1-2. 스레드와 멀티스레드</h2>
<ul>
  <li>
    스레드(thread)의 사전적 의미는 <strong>실행 흐름 단위</strong>이다.
  </li>
  <li>
    CPU에서 사용되는 스레드와 프로그래밍에서 사용되는 스레드는 용례가 다르기 때문에 도서에서는 <strong>CPU</strong>에 사용되는 스레드를 <strong>하드웨어적 스레드</strong>로, <strong>프로그램</strong>에서 사용되는 스레드를 <strong>소프트웨어적 스레드</strong>로 다룬다.
  </li>
</ul>

<h3>1-2-1. 하드웨어적 스레드</h3>
<ul>
  <li>
    스레드를 하드웨어적으로 정의하면 <strong>하나의 코어가 동시에 처리하는 단위</strong>를 의미한다.
  </li>
  <li>
    여러 스레드를 지원하는 CPU는 <strong>하나의 코어로도 여러 개의 명령어</strong>를 동시에 실행할 수 있다.
  </li>
    <ul>
      <li>
        예를 들어 2코어 4스레드라면 스레드가 2개인 코어가 2개인 구조를 떠올릴 수 있다. (core의 수 * 각 코어당 thread의 수).
      </li>
    </ul>
  <li>
    하나의 코어로 여러 명령어를 동시에 처리하는 CPU를 <strong>멀티스레드(multithread)프로세서</strong> 또는 <strong>멀티스레드 CPU</strong>라 한다.
  </li>
  <li>
    인텔의 경우 자신들의 멀티스레드 기술에 <strong>하이퍼스레딩(hyper-threading)</strong>이라는 명칭을 부여했는데 이는 멀티스레드와 자주 접하게 될 용어이다.
  </li>
</ul>

<h3>1-2-2. 소프트웨어적 스레드</h3>
<ul>
  <li>
    소프트웨어적 스레드는 <strong>하나의 프로그램에서 독립적으로 실행되는 단위</strong>를 의미한다.
  </li>
  <li>
    소프으웨어 스레드의 각 작업을 다른 메모리 영역에 할당하고 CPU가 멀티스레드로 시행하는 경우가 해당한다.
  </li>
    <ul>
      <li>
        단, 1코어 1스레드의 경우 병렬성보다는 소프트웨어의 동시성이라고 의미하는 게 맞는 거 같다(?). ALU를 쓰지 않는 명령어 처리도 있다;;
      </li>
    </ul>
</ul>

<h3>1-2-3. 멀티스레드 프로세서</h3>
<ul>
  <li>
    멀티스레드 프로세서를 실제로 설계하는 일은 매우 복잡하지만, 가장 큰 핵심은 <strong>레지스터</strong>이다.
  </li>
    <ul>
      <li>
        하나의 코어가 여러 명령어를 동시 처리하도록 하려면 프로그램 카운터, 스택 포인터, 메모리 버퍼 레지스터, 메모리 주소 레지스터와 같이 하나의 <strong>명령어 처리를 위해 꼭 필요한 레지스터를 여러 개</strong> 가지고 있으면 된다.
      </li>
        <ul>
          <li>
            아직도 ALU가 하나인데 병렬처리된다는 게 이해가 안 된다. 동시성을 병렬성으로 설명하고 있는건가? ALU를 쓰지 않는 명령어 처리도 있음;;
          </li>
        </ul>
    </ul>
  <li>
    CPU는 다수의 코어와 스레드로 여러 명령어를 처리할 수 있으나 메모리가 보기에는 한 번에 하나의 명령어를 처리하는 <strong>다수의 CPU</strong>가 있는 것으로 보인다.
  </li>
    <ul>
      <li>
        하드웨어 스레드는 하나의 코어로 여러 명령어 동시 처리가 가능하나 시스템이 보기에는 CPU가 여럿인 것처럼보이기에 하드웨어 스레드를 <strong>논리 프로세서(logical processor)</strong>라 부르기도 한다.
      </li>
    </ul>
  <li>
    핵심 정리.
  </li>
    <ul>
      <li>
        <strong>코어</strong>는 명령어를 실행할 수 있는 하드웨어 부품이다.
      </li>
      <li>
        <strong>스레드</strong>는 명령어를 실행하는 단위이다.
      </li>
      <li>
        <strong>멀티코어 프로세서</strong>는 명령어를 실행할 수 있는 하드웨어 부품이 CPU 안에 두 개 이상 있는 CPU를 의미한다.
      </li>
      <li>
        <strong>멀티스레드 프로세서</strong>는 하나의 코어로 여러 개의 명령어를 동시에 실행할 수 있는 CPU를 의미한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 명령어 병렬 처리 기법</h1>
<ul>
  <li>
    빠른 CPU를 위해서는 클럭 속도, 멀티코어, 멀티스레드도 중요하지만 CPU가 <strong>놀지 않도록</strong> 하는 것 또한 중요하다.
  </li>
  <li>
    CPU가 놀지 않도록 작동시키는 기법인 <strong>명령어 병렬 처리 기법(ILP; Instruction-Level Parallelism)</strong>을 알아본다.
  </li>
    <ul>
      <li>
        대표적으로는 명령어 파이프 라이닝, 슈퍼스칼라, 비순차적 명령어 처리가 있다.
      </li>
    </ul>
</ul>

<br>

<h2>2-1. 명령어 파이프라인</h2>
<ul>
  <li>
    대표적으로 명령어 처리 과정을 클럭 단위로 나누면 아래와 같다.
  </li>
    <ol>
      <li>
        명령어 인출(Instruction Fetch)
      </li>
      <li>
        명령어 해석(Instruction Decode)
      </li>
      <li>
        명령어 실행(Execute Instruction)
      </li>
      <li>
        결과 저장(Write Back)
      </li>
    </ol>
  <li>
    중요한 점은 상단의 단계 중 같은 단계가 <strong>겹치지 않는다면</strong> CPU는 각 단계를 <strong>동시에 실행</strong>할 수 있다는 점이다. (p157 그림 참고).
  </li>
    <ul>
      <li>
        예를 들어 명령어1의 인출 과정과 명령어 2의 해석 과정을 동시실행할 수 있다.
      </li>
    </ul>
  <li>
    공장 생산 라인과 같이 명령어들을 <strong>명령어 파이프라인(instruction pipeline)</strong>에 넣고 동시에 처리하는 기법을 <strong>명령어 파이프라이닝(instruction pipelining)</strong>이라고 한다.
  </li>
  <li>
    파이프라이닝이 높은 성능을 가져오기는 하지만 특정 상황에서는 성능 향상에 실패하는 경우도 있으며 이러한 상황을 <strong>파이프라인 위험(pipeline hazard)</strong>라고 부른다.
  </li>
    <ul>
      <li>
        파이프라인 위험에는 대표적으로 데이터 위험, 제어 위험, 구조적 위험이 있다.
      </li>
    </ul>
</ul>

<h3>2-1-1. 데이터 위험</h3>
<ul>
  <li>
    데이터 위험(data hazard)은 <strong>명령어 간 데이터 의존성</strong>에 의해 발생한다.
  </li>
  <li>
    하나의 명령어를 수행하기 위해서는 <strong>이전 명령어를 처리하여 나온 데이터<strong>/를 필요로할 때가 있다 이 때에는 명령어 파이프라이닝으로 처리가 불가하다.
  </li>
</ul>

<h3>2-1-2. 제어 위험</h3>
<ul>
  <li>
    제어 위험(control hazard)은 주로 분기 등으로<strong>인한 프로그램 카운터의 갑작스러운 변화</strong>에 의해 발생한다.
  </li>
    <ul>
      <li>
        프로그램 실행 흐름이 바뀌어 명령어가 실행되면서 프로그램 카운터 값이 갑자기 변한다면 이로 인해 명령어 파이프라인에 미리 가지고 와 처리 중이던 명령어들이 아무 쓸모 없어질 수 있다.
      </li>
    </ul>
  <li>
    제어 위험을 해결하기 위해 사용하는 기술 중 하나는 <strong>분기 예측(branch prediction)</strong>이다.
  </li>
    <ul>
      <li>
        분기 예측은 어디로 분기할지 미리 <strong>예측</strong>한 후 해당 주소를 인출하는 기술이다.
      </li>
    </ul>
</ul>

<h3>2-1-3. 구조적 위험</h3>
<ul>
  <li>
    구조적 위험(structural hazard)은 명령어들을 겹쳐 실행하는 과정에서 서로 다른 명령어가 <strong>동시에 ALU, 레지스터 등과 같은 CPU 부품을 사용</strong>하려 할 때 발생한다.
  </li>
  <li>
    구조적 위험은 <strong>자원 위험(resource hazard)</strong>라고도 부른다.
  </li>
</ul>

<br>

<h2>2-2. 슈퍼스칼라</h2>
<ul>
  <li>
    오늘날 대부분의 CPU는 여러 개의 파이프라인을 이용한다. 이렇게 <strong>CPU 내부에 여러 개의 명령어 파이프라인을 포함</strong>한 구조를 슈퍼스칼라(superscalar)라고 한다.
  </li>
  <li>
    슈퍼스칼라 구조로 명령어 처리가 가능한 CPU를 <strong>슈퍼스칼라 프로세서</strong> 또는 <strong>슈퍼스칼라 CPU</strong>라고 한다.
  </li>
    <ul>
      <li>
        매 클럭 주기마다 동시에 여러 명령어를 인출, 실행할 수 있어야 한다.
      </li>
    </ul>
  <li>
    슈퍼스칼라 프로세서는 이론적으로 <strong>파이프라인 개수</strong>에 비례하여 프로그램 처리 속도가 빨라지지만, 파이프라인 위험 등 예상치 못한 문제가 있어 반드시 비례하지는 않는다.
  </li>
   <ul>
     <li>
       여러 파이프라인을 이용하기 때문에 단일 파이프라인을 사용할 때보다 고도로 설계되어야 한다.
     </li>
   </ul>
</ul>

<br>

<h2>2-3. 비순차적 명령어 처리</h2>
<ul>
  <li>
    많은 전공서에서 다루지는 않지만 오늘날 CPU 성능 향상에 크게 기여한 기법으로 비순차적 명령어 처리(OoOE; Out-of-order execution)이 있다.
  </li>
  <li>
    모든 명령어가 의존이되는 것은 아니기에 <strong>순서를 바꾸어 실행해도 무방</strong>한 명령어를 먼저 실행하여 명령어 파이프라인이 다른 명령어 처리를 <strong>대기하는거나 멈추는 것을 방지</strong>하는 기법을 비순차적 명령어 처기 기법이라 한다.
  </li>
  <li>
    비순차적 명령어 처리가 가능한 CPU는 명령어들이 <strong>어떤 명령어와 데이터 의존성</strong>을 가지고 있는지 <strong>순서를 바꿔 실행할 수 있는 명렁어</strong>에는 어떤 것들이 있는지 <strong>판단</strong>할 수 있어야 한다.
  </li>
</ul>

<br><br>

<h1>3. CISC와 RISC</h1>
<ul>
  <li>
    CPU가 파이프라이닝과 슈퍼스칼라 기법을 효과적으로 사용하기 위해서는 <strong>명령어가 파이프라이닝 하기 쉽게</strong> 생겨야 한다.
  </li>
  <li>
    파이프라이닝 하기 쉬운 명령어로 CPU의 언어인 <strong>ISA</strong>와 각기 다른 성격의 ISA인 <strong>CISC</strong>와 <strong>RISC</strong>를 학습한다.
  </li>
</ul>

<br>

<h2>3-1. 명령어 집합</h2>
<ul>
  <li>
    CPU의 명령어 의 세세한 생김새, 연산, 주소지정 방식 등은 큰 틀에서 유사하나 CPU마다 조금씩 차이가 있다.
  </li>
  <li>
    CPU가 이해할 수 있는 명령어들의 모음을 <strong>명령어 집합(instruction set)</strong> 또는 <strong>명령어 집합 구조(ISA; Instruction Aset Architecture)</strong>이라고 한다.
  </li>
    <ul>
      <li>
        구조(Architecture)라고 칭한 이유는 CPU가 어떤 명령어를 이해하는지에 따라 <strong>컴퓨터 구조 및 설게 방식</strong>이 달라지기 때문이다.
      </li>
    </ul>
  <li>
    ISA가 다르다는 것은 CPU가 이해할 수 있는 명령어와 어셈블리어도 달라짐을 의미한다.
  </li>
    <ul>
      <li>
        동일한 소스를 작성하고 ISA가 다른 컴퓨터에서 어셈블리어로 컴파일하면 결과로 나온 어셈블리어도 다르다.
      </li>
      <li>
        참고로 사용한 컴파일러에 따라서도 어셈블리어가 달라질 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>3-2. CISC</h2>
<ul>
  <li>
    CISC는 Complex Instruction Set Computer의 약자로 <strong>복잡하고 다양한 명령어</strong>들을 활용하는 CPU 설계 방식이다.
  </li>
  <li>
    CISC는 다양하고 강력한 기능의 명령어 집합을 활용하기 때문에 명령어의 형태와 크기가 다양한 <strong>가변 길이 명령어</strong>를 사용한다.
  </li>
    <ul>
      <li>
        메모리에 접근하는 주소 지정 방식도 다양하기 때문에 특별한 상황에서만 사용되는 독특한 주소 지정 방식들도 존재한다.
      </li>
    </ul>
  <li>
    다양하고 강력한 명령어를 활용한다는 점은 <strong>상대적으로 적은 수의 명령어</strong>로도 프로그램을 실행할 수 있음을 의미한다.
  </li>
    <ul>
      <li>
        또한 <strong>컴파일된 프로그램의 크기</strong>가 작다.
      </li>
    </ul>
  <li>
    CISC는 적은 수의 명령어만으로도 프로그램을 동작시킬 수 있고 이로인해 <strong>메모리 공간을 절약</strong>할 수 있어 과거에 주로 사용되었다.
  </li>
  <li>
    단, CISC는 활용하는 명령어가 워낙 복잡하고 다양한 기능을 제공하여 명령어의 크기와 실행되기까지의 시간이 <strong>일정하지 못하다는 치명적인 단점</strong>이 존재한다.
  </li>
    <ul>
      <li>
        복잡한 명령어 때문에 명령어 하나를 실행하는 데 <strong>여러 클럭 주기</strong> 또한 필요로 한다.
      </li>
    </ul>
  <li>
    명령어 파이프라인 기법은 각 단계에 소요되는 시간이 동일해야 하는데 CISC는 명령어 수행 시간이 길고 다양하기 때문에 <strong>명령어 파이프라인에 제대로 동작하지 않는다</strong>는 치명적인 문제를 갖는다.
  </li>
    <ul>
      <li>
        또한 대다수의 복잡한 명령어는 사용 빈도가 낮아 효율적이지 못하다.
      </li>
    </ul>
  <li>
    요약하자면 메모리를 절약할 수는 있지만 명령어 규격화가 어려워 파이프라이닝이 어려우며 이로인해 CISC 기반 CPU는 성장에 한계가 있다.
  </li>
</ul>

<br>

<h2>3-3. RISC</h2>
<ul>
  <li>
    CISC에서 얻은 교훈은 아래 두 개이다.
  </li>
    <ul>
      <li>
        원활한 파이프라이닝을 위해서는 <strong>명령어 길이</strong>와 <strong>수행 시간</strong>이 짧고 규격화 되어 있어야 한다.
      </li>
      <li>
        복잡한 기능을 지원하는 명령어를 추가하기보다 <strong>자주 쓰이는 기본적인 명령어를 작고 빠르게</strong> 만드는 것이 중요하다.
      </li>
    </ul>
  <li>
    CISC의 교훈을 통해 등장한 것이 RISC(Reduced Instruction Set Computer)이다.
  </li>
    <ul>
      <li>
        RISC는 CISC에 비해 <strong>명령어의 종류가 적고 짧고 규격화</strong> 되었으며 되도록 <strong>1클럭 내외</strong>로 실행되는 명령어를 지향한다.
      </li>
    </ul>
  <li>
    RISC는 <strong>고정 길이 명령어</strong>를 활용하며 상기한 특징들로 인해 RISC 명령어 집합은 <strong>명령어 파이프라이닝에 최적화</strong>되어 있다.
  </li>
    <ul>
      <li>
        메모리에 직접 접근하는 명령어를 <strong>load</strong>와 <strong>store</strong> 두 개로 제한할 만큼 메모리 접근을 단순화하고 최소화를 추구한다. 이런 점에서 RISC를 <strong>load-store 구조</strong>라 부르기도 한다.
      </li>
    </ul>
  <li>
    RISC는 메모리 접근을 단순화, 최소화하는 대신 <strong>레지스터</strong>를 적극적으로 활용한다.
  </li>
    <ul>
      <li>
        이로 인해 CISC보다 레지스터를 이용하는 연산이 많고, 범용 레지스터의 개수 또한 더 많다.
      </li>
      <li>
        또 사용 가능한 명령어의 수가 CISC보다 적기 때문에 RISC는 CISC보다 더 많은 명령으로 프로그램을 작동시킨다.
      </li>
    </ul>
</ul>