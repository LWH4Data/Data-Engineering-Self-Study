<h1>1. ALU와 제어장치</h1>
<h2>1-1. ALU</h2>
<ul>
  <li>
    ALU는 연산한 결괏값과 플래그를 내보낸다.
  </li>
  <li>
    ALU는 <strong>레지스터</strong>를 통해 <strong>피연산자</strong>를 받아들이고, <strong>제어장치</strong>로부터 수행할 연산을 알려주는 <strong>제어 신호</strong>를 받아들인다.
  </li>
  <li>
    ALU가 연산을 수행한 결과는 일시적으로 <strong>레지스터</strong>에 저장된다.
  </li>
    <ul>
      <li>
        메모리에 저장할 경우 CPU는 메모리에 자주 접근하게 되는데 이로인한 <strong>속도저하</strong>가 발생하기 때문이다.
      </li>
    </ul>
  <li>
    ALU는 음수를 나타내거나 연산 결과가 결과를 담은 레지스터보다 클 때 이러한 추가 정보를 전달하기 위해 <strong>플래그</strong>를 내보낸다.
  </li>
    <ul>
      <li>
        연산 결과가 연산 결과를 담을 레지스터보터 큰 상황을 <strong>오버플로우(overflow)</strong>라 한다.
      </li>
    </ul>
  <li>
    대표적인 플래그들에는 다음이 있다. (플래그는 1과 0으로 표현한다. p106참고).
  </li>
    <ul>
      <li>
        <strong>부호 플래그</strong>: 연산한 결과의 부홀르 나타낸다.
      </li>
      <li>
        <strong>제로 플래그</strong>: 연산 결과가 0인지 여부를 나타낸다.
      </li>
      <li>
        <strong>캐리 플래그</strong>: 연산 결과 올림수나 빌림수가 발생했는지를 나타낸다.
      </li>
      <li>
        <strong>오버플로우 플래그</strong>: 오버플로우가 발생했는지를 나타낸다.
      </li>
      <li>
        <strong>인터럽트 플래그</strong>: 인터럽트가 가능한지 나타낸다.
      </li>
      <li>
        <strong>슈퍼바이저 플래그</strong>: 커널 모드로 실행 중인지, 사용자 모드로 실행 중인지를 나타낸다.
      </li>
    </ul>
  <li>
    플래그는 CPU가 프로그램을 실행하는 도중 <strong>반드시 기억</strong>해야하는 일종의 참고 정보이며 <strong>플래그 레지스터</strong>라는 레지스터에 저장된다.
  </li>
    <ul>
      <li>
        즉 플래그 레지스터를 읽으면 연산 결과에 대한 추가적인 정보, 참고 정보를 얻을 수 있다.
      </li>
      <li>
        각 플래그의 공간이 존재하며 이들은 회로로 연결되어 0 혹은 1의 값을 가지고 있다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 제어장치</h2>
<ul>
  <li>
    <strong>제어장치</strong>는 제어 신호를 내보내고, 명령어를 해석하는 부품이다.
  </li>
  <li>
    <strong>제어 신호</strong>는 컴퓨터 부품들을 관리하고 작동시키기 위한 일종의 전기 신호이다.
  </li>
  <li>
    제어장치는 CPU의 구성 요소 중 가장 정교하게 설계된 부품이다. 제조사마다 제어장치의 구현 방식과 명령어를 해석하는 방식은 다르기때문에 암기보다는 이해를 권한다.
  </li>
  <li>
    <strong>제어장치가 받아들이는 정보</strong>
  </li>
    <ul>
      <li>
        첫째, 제어장치는 <strong>클럭 신호</strong>를 받아들인다.
      </li>
        <ul>
          <li>
            <strong>클럭(clock)</strong>이란 컴퓨터의 <strong>모든 부품</strong>을 일시불란하게 움질 수 있게 하는 <strong>시간 단위</strong>이다.
          </li>
          <li>
            <strong>클럭의 주기</strong>에 맞추어 다른 레지스터로 데이터가 이동되거나, ALU에서 연산이 수행되거나, CPU가 메모리에 저장된 명령어를 읽어들인다.
          </li>
          <li>
            단, 모든 부품이 클럭에 맞추어 작동하지만 매 클럭마다 작동하는 것은 아니다.
          </li>
        </ul>
      <li>
        둘째, 제어장치는 <strong>'해석해야 할 명령어'</strong>를 받아들인다.
      </li>
        <ul>
          <li>
            CPU가 해석해야할 명령어는 명령어 레지스터라는 특별한 레지스터에 저장된다.
          </li>
          <li>
            제어장치는 명령어 레지스터로부터 해석할 명령어를 받아들이고 해석한 뒤, 제어 신호를 발생시켜 컴퓨터 부품들에 <strong>수행해야할 내용을 알려준</strong>.
          </li>
        </ul>
      <li>
        셋째, 제어장치는 플래그 레지스터 속 <strong>플래그 값</strong>을 받아들인다.
      </li>
        <ul>
          <li>
            제어장치는 제어 신호를 통해 컴퓨터 부품들을 제어할 때 플래그 값을 받아들이고 참고하여 제어 신호를 발생시킨다.
          </li>
        </ul>
      <li>
        넷째, 제어장치는 시스템 버스, 그중에서 <strong>제어 버스</strong>로 전달된 제어 신호를 받아들인다.
      </li>
        <ul>
          <li>
            제어 신호는 CPU뿐만 아니라 입출력장치를 포함한 <strong>CPU 외부 장치</strong>도 발생키길 수 있다.
          </li>
          <li>
            제어장치는 제어 버스를 통해 <strong>외부로부터 전달된 제어 신호</strong>를 받아들일 수 있다.
          </li>
        </ul>
    </ul>
  <li>
    제어장치가 내보내는 정보
  </li>
    <ul>
      <li>
        CPU <strong>외부</strong>에 전달하는 제어 신호
      </li>
        <ul>
          <li>
            제어장치가 CPU 외부에 제어 신호를 전달한다는 것은 곧 <strong>제어 버스</strong>로 제어 신호를 내보내는 것을 의미한다.
          </li>
          <li>
            이러한 예로는 크게 <strong>메모리</strong>에 전달하는 제어 신호와 <strong>입출력장치</strong>에 전달하는 제어 신호가 있다.
          </li>
        </ul>
      <li>
        CPU <strong>내부</strong>에 전달하는 제어 신호
      </li>
        <ul>
          <li>
            제어장치가 CPU 내부에 전달하는 제어 신호에는 크게 <strong>ALU</strong>에 전달하는 제어 신호와 <strong>레지스터</strong>에 전달하는 제어 신호가 있다.
          </li>
        </ul>
    </ul>
</ul>

<br><br>

<h1>2. 레지스터</h1>
<ul>
  <li>
    프로그램 속 명령어와 데이터는 실행 전후로 반드시 <strong>레지스터</strong>에 저장된다. 따라서 레지스터 속의 값 만으로도 CPU에서 어떤 명령어가 어떻게 수행되는지 추정할 수도 있다.
  </li>
</ul>

<br>

<h2>2-1. 반드시 알아야 할 레지스터</h2>
<ul>
  <li>
    사용화된 CPU 속 레지스터들은 CPU마다 <strong>이름, 크기, 종류가 다양</strong>하고 각 제조사 홈페이지나 공식 문서 등에서 확인할 수 있다.
  </li>
  <li>
    도서에서는 많은 CPU가 공통으로 포함하고 있는 여덟 개의 레지스터를 학습한다.
  </li>
    <ul>
      <li>
        프로그램 카운터
      </li>
      <li>
        명령어 레지스터
      </li>
      <li>
        메모리 주소 레지스터
      </li>
      <li>
        메모리 버퍼 레지스터
      </li>
      <li>
        플래그 레지스터
      </li>
      <li>
        범용 레지스터
      </li>
      <li>
        스택 포인터
      </li>
      <li>
        베이스 레지스터
      </li>
    </ul>
</ul>

<h3>2-1-1. 프로그램 카운터</h3>
<ul>
  <li>
    <strong>프로그램 카운터(PC; Program Counter)</strong>는 메모리에서 가져올 명령어의 주소, 즉 <strong>메모리에서 읽어 들일 명령어의 주소</strong>를 저장한다.
  </li>
  <li>
    프로그램 카운터를 <strong>명령어 포인터(IP; Instruction Pointer)</strong>라고 부르는 CPU도 있다.
  </li>
</ul>

<h3>2-1-2. 명령어 레지스터</h3>
<ul>
  <li>
    명령어 레지스터(IR; Instruction Register)는 해석할 명령어, 즉 <strong>방금 메모리에서 읽어 들인 명령어를 저장</strong>하는 레지스터이다.
  </li>
</ul>

<h3>2-1-3. 메모리 주소 레지스터</h3>
<ul>
  <li>
    메모리 주소 레지스터(MAR; Memory Address Register)는 <strong>메모리 주소</strong>를 저장하는 레지스터이다.
  </li>
  <li>
    CPU가 읽어 들이고자 하는 주소 값을 <strong>주소 버스</strong>로 보낼 때 메모리 주소 레지스터를 거친다.
  </li>
</ul>

<h3>2-1-4. 메모리 버퍼 레지스터</h3>
<ul>
  <li>
    메모리 버퍼 레지스터(MBR; Memory Buffer Register)는 <strong>메모리와 주고받을 값(데이터와 명령어)</strong>을 저장하는 레지스터이다.
  </li>
  <li>
    <strong>메모리에 쓰고 싶은 값</strong>이나 <strong>메모리로부터 전달받은 값</strong>은 메모리 버스 레지스터를 거친다.
  </li>
  <li>
    쉽게 말해 <strong>주소 버스</strong>로 내보낼 값이 <strong>메모리 주소 레지스터</strong>를, <strong>데이터 버스</strong>로 주고받을 값은 <strong>메모리 버퍼 레지스터</strong>를 거친다.
  </li>
    <ul>
      <li>
        메모리 버퍼 레지스터는 메모리 데이터 레지스터(MDR; Memory Data Register)라고도 부른다.
      </li>
    </ul>
</ul>

<h4>프로그램 실행 과정</h4>
<ul>
  <li>
    프로그램을 처음부터 실행하기 위해 프로그램 카운터에 할당된 <strong>메모리의 시작 번지</strong>를 저장한다.
    <br>➡ 프로그램 카운터에 저장된 읽어들일 번지를 <strong>메모리 주소 레지스터</strong>에 저장한다.
    <br>➡ 메모리 주소 레지스터에 저장된 번지를 <strong>''메시지 읽기' 제어 신호 + 주소 버스(메모리 주소)'</strong>로 <strong>메모리</strong>로 보낸다.
    <br>➡ 메모리에서 찾은 값은 <strong>데이터 버스</strong>를 통해 <strong>메모리 버퍼 레지스터</strong>로 전달된다.
    <br>➡ 프로그램 카운터는 <strong>값이 증가</strong>하며 <strong>다음 명령어</strong>를 읽어 들일 준비를 한다.
    <br>➡ 메모리 버퍼 레지스터에 저장된 값은 <strong>명령어 레지스터</strong>로 이동한다.
    <br>➡ 제어장치는 명령어 레지스터의 명령어를 해석하고 제어 신호를 발생시킨다.
  </li>
</ul>

<h4>순차적인 실행 흐름이 끊기는 경우</h4>
<ul>
  <li>
    일반적으로 프로그램 카운터는 꾸준히 증가하지만 종종 전혀 다른 값으로 업데이트 되는 경우가 있다.
  </li>
  <li>
    명령어 중에서 JUMP, CONDITIONAL JUMP, CALL, RET와 같이 <strong>특정 메모리 주소</strong>로 실행 흐름을 이동하는 명령어가 실행되었을 때가 해당한다.
  </li>
  <li>
    인터럽트가 발생하는 경우에도 실행 흐름이 끊어진다.
  </li>
</ul>

<h3>2-1-5. 범용 레지스터</h3>
<ul>
  <li>
    범용 레지스터(general purpose register)는 일반적인 상황에서 <strong>자유롭게 사용</strong>할 수 있는 레지스터이다.
  </li>
    <ul>
      <li>
        메모리 버퍼 레지스터는 데이터 버스로 주고받을 값만, 메모리 주소 레지스터는 주소 버스로 보낼 주소값만 저장하지만 범용 레지스터는 <strong>데이터와 주소 모두 저장</strong>할 수 있다.
      </li>
    </ul>
  <li>
    일반적으로 CPU 안에는 여러 개의 범용 레지스터들이 있고, 현대 대다수 CPU는 모두 범용 레지스터를 가지고 있다.
  </li>
</ul>

<h3>2-1-6. 플래그 레지스터</h3>
<ul>
  <li>
    플래그 레지스터(flag register)는 <strong>연산 결과</strong> 또는 <strong>CPU 상태에 대한 부가적인 정보</strong>를 저장한다.
  </li>
</ul>

<br>

<h2>2-2. 특정 레지스터를 이용한 주소 지정 방식(1): 스택 주소 지정 방식</h2>
<ul>
  <li>
    레지스터 중 프로그램 카운터, 스택 포인터, 베이스 레지스터는 <strong>주소 지정</strong>에 사용될 수 있는 특별한 레지스터이다.
  </li>
    <ul>
      <li>
        스택 포인터(stack pointer)는 <strong>스택 주소 지정 방식</strong>이라는 주소 지정 방식에 사용된다.
      </li>
      <li>
        프로그램 카운터와 베이스 레지스터는 <strong>변위 주소 지정 방식</strong>이라는 주소 지정 방식에 사용된다.
      </li>
    </ul>
  <li>
    스택 주소 지정 방식은 <strong>스택</strong>과 <strong>스택 포인터</strong>를 이용한 주소 지정 방식이다. 자료 구조의 그 스택이 맞다.
  </li>
    <ul>
      <li>
        스택 포인터란 <strong>스택의 꼭대기</strong>를 가리키는 레지스터이다. 즉 <strong>마지막으로 저장한 값의 위치</strong>를 저장하는 레지스터이다.
      </li>
    </ul>
  <li>
    스택은 메모리 안에 스택처럼 사용할 영역이 존재하며 이를 <strong>스택 영역</strong>이라 한다.
  </li>
    <ul>
      <li>
        다른 주소 공간과는 다르게 스택처럼 사용하기로 암묵적으로 약속된 영역이다.
      </li>
    </ul>
</ul>

<br>

<h2>2-3. 특정 레지스터를 이용한 주소 지정 방식(2): 변위 주소 지정 방식</h2>
<ul>
  <li>
    변위 주소 지정 방식(displacement addressing mode)이란 <strong>오퍼랜드 필드의 값(변위)</strong>과 <strong>특정 레지스터의 값을 더하여 유효 주소</strong>룰 얻어내는 주소 지정 방식이다.
  </li>
  <li>
    변위 주소 지정 방식을 사용하는 명령어는 기존과 같이 연산 코드 필드와 오퍼랜드 필드가 있는 건 동일하지만 <strong>어떤 레지스터의 값과 더할지를 나타내는 레지스터 필드</strong>를 포함한다.
  </li>
    <ul>
      <li>
        연산 코드 + 레지스터 + 오퍼랜드
      </li>
    </ul>
  <li>
    변위 주소 지정 방식은 오퍼랜드 필드의 주소와 어떤 레지스터를 더하는지에 따라 <strong>상대 주소 지정 방식과 베이스 레지스터 주소 지정 방식 등</strong>으로 나뉜다.
  </li>
</ul>

<h3>2-3-1. 상대 주소 지정 방식</h3>
<ul>
  <li>
    상대 주소 지정 방식(relative addressing mode)은 <strong>오퍼랜드</strong>와 <strong>프로그램 카운터</strong>의 값을 더하여 유효 주소를 얻는다.
  </li>
    <ul>
      <li>
        예를 들어 오퍼랜드가 -3이라면 프로그램 카운터의 번지를 기준으로 세 번째 이전(-3) 번지로 접근한다.
      </li>
    </ul>
  <li>
    상대 주소 지정 방식은 프로그래밍 언어의 if문과 유사하게 <strong>분기하여 특정 주소의 코드를 실행</strong>할 때 사용한다.
  </li>
</ul>

<h3>2-3-2. 베이스 레지스터 주소 지정 방식</h3>
<ul>
  <li>
    베이스 레지스터 주소 지정 방식(base-register addressing mode)은 <strong>오퍼랜드</strong>와 <strong>베이스 레지스터의 값</strong>을 더하여 유효 주소를 얻는다.
  </li>
  <li>
    여기서는 베이스 레지스터가 <strong>기준 주소</strong>, 오퍼랜드가 <strong>기준 주소로부터 떨어진 거리</strong>의 역할을 한다.
  </li>
</ul>

<h4>상용화된 CPU 속 레지스터 및 주소 지정 방식</h4>
<ul>
  <li>
    CPU는 전공서 속의 모습과 실제 모습이 가장 다른 부품이기 때문에 임베디드나 저수준에 가까운 개바을 할 때 괴리가 큰 영역이다.
  </li>
  <li>
    이런 괴리를 줄이고 싶다면 가장 대중적인 CPU인 x86(x86-64)과 ARM의 레지스터 등 각종 CPU의 실제 <strong>레지스터</strong>를 봐두는 것이 좋다.
  </li>
  <li>
    https://github.com/kangtegong/self-learning-cs/blob/main/registers/registers.md#%EB%8C%80%ED%91%9C%EC%A0%81%EC%9D%B8-arm-%EB%A0%88%EC%A7%80%EC%8A%A4%ED%84%B0
  </li>
</ul>

<br><br>

<h1>3. 명령어 사이클과 인터럽트</h1>
<ul>
  <li>
    CPU가 하나의 명령어를 처리하는 과정에는 정해진 <strong>흐름</strong>이 있다. 이렇게 하나의 명령어를 처리하는 정형화된 흐름을 <strong>명령어 사이클</strong>이라 한다.
  </li>
  <li>
    CPU는 정해진 흐름에 따라 명령어를 처리하지만 흐름이 끊어지는 경우도 발생한다. 이 경우를 <strong>인터럽트</strong>라 한다.
  </li>
</ul>

<br>

<h2>3-1. 명령어 사이클</h2>
<ul>
  <li>
    프로그램에는 수많은 명령어가 있고 CPU는 각 명령어를 하나씩 실행한다. 이때 명령어들은 <strong>일정한 주기</strong>가 반복되며 실행되고 이 주기를 <strong>명령어 사이클(instruction cycle)</strong>이라 한다.
  </li>
  <li>
    가장 먼저 명령어를 메모리에서 CPU로 가져오는 것이 명령어 사이클의 첫 번째 과정이며 이를 <strong>인출 사이클(fetch cycle)</strong>이라 한다.
  </li>
    <ul>
      <li>
        명령어를 가져왔다면 명령어를 실행하는 사이클의 두 번째 과정을 진행하며 이를 <strong>실행 사이클(execution cycle)</strong>이라 한다.
      </li>
        <ul>
          <li>
            제어장치가 명령어 레지스터에 담긴 값을 해석하고, 제어 신호를 발생시키는 단계이다.
          </li>
        </ul>
    </ul>
  <li>
    프로그램을 이루는 수많은 명령어는 일반적으로 <strong>인출과 실행 사이클을 반복</strong>하며 실행된다.
  </li>
  <li>
    단, 간접 주소 지정 방식 등 실행 사이클이 아닌 다시 메모리에 접근하는 경우 등이 존재하는데 이렇게 <strong>다른 단계</strong>를 진행하게 되는 경우 이를 <strong>간접 사이클(indirect cycle)</strong>이라 한다.
  </li>
</ul>

<br>

<h2>3-2. 인터럽트</h2>
<ul>
  <li>
    CPU가 수행하는 작업은 방해를 받아 잠시 중단될 수 있는데 이렇게 CPU를 방해하는 신호를 <strong>인터럽트(interrupt)</strong>라고 한다.
  </li>
  <li>
    인터럽트의 종류에는 크게 <strong>동기 인터럽트</strong>와 <strong>비동기 인터럽트</strong>가 있다.
  </li>
    <ul>
      <li>
        동기 인터럽트(synchronous interrupts)는 <strong>CPU에 의해 발생</strong>하는 인터럽트이다.
      </li>
        <ul>
          <li>
            CPU가 명령어를 수행하는 도중 예상치 못한 상황을 마주했을 때 발생한다.
          </li>
          <li>
            이렇게 예외적인 상황을 마주하여 발생한 동기 인터럽트는 <strong>예외(exception)</strong>라고 부른다.
          </li>
        </ul>
      <li>
        비동기 인터럽트(asynchronous interrupt)는 주로 <strong>입출력장치</strong>에 의해 발생하는 인터럽트이다. 
      </li>
        <ul>
          <li>
            일반적으로 <strong>알림 역할</strong>을 한다.
          </li>
            <ul>
              <li>
                예를 들면 CPU가 프린터에 작업을 부탁하면 작업을 끝낸 프린터가 CPU에 완료 알림(인터럽트)을 보낸다.
              </li>
            </ul>
          <li>
            일반적으로 비동기 인터럽트를 인터럽트라 칭하기도 한다. 도서에서는 <strong>하드웨어 인터럽트</strong>라는 용어를 사용한다.
          </li>
        </ul>
    </ul>
</ul>

<h3>3-2-1. 하드웨어 인터럽트</h3>
<ul>
  <li>
    하드웨어 인터럽트는 <strong>알림</strong>과 같은 인터럽트이며 CPU가 <strong>명령어를 효율적으로 처리</strong>하기 위해 사용한다.
  </li>
  <li>
    에를 들어 프린터 작업을 하면 프린터의 작업은 CPU의 처리 속도보다 느리기 때문에 CPU는 주기적으로 확인을 해야한다. 이때 하드웨어 인터럽트를 사용하면 CPU가 주기적으로 확인을 할 필요가 없어지기 때문에 효율적인 운영이 가능하다.
  </li>
</ul>

<h3>3-2-2. 하드웨어 인터럽트 처리 순서</h3>
<ul>
  <li>
    하드웨어 인터럽트를 처리하는 방식은 대부분의 CPU에서 대동소이하다.
  </li>
    <ol>
      <li>
        입출력장치는 CPU에 <strong>인터럽트 요청 신호</strong>를 보낸다.
      </li>
      <li>
        CPU는 실행 사이클이 끝나고 명령어를 인출하기 전 항상 인터럽트 여부를 확인한다.
      </li>
      <li>
        CPU는 인터럽트 요청을 확인하고 <strong>인터럽트 플래그</strong>를 통해 현재 인터럽트를 받아들일 수 있는지 여부를 확인한다.
      </li>
      <li>
        인터럽트를 받아들일 수 있다면 CPU는 지금까지의 작업을 백업한다.
      </li>
      <li>
        CPU는 <strong>인터럽트 벡터</strong>를 참조하여 <strong>인터럽트 서비스 루틴</strong>을 실행한다.
      </li>
      <li>
        인터럽트 서비스 루틴 실행이 끝나면 4번에서 백업해 둔 작업을 복구하여 실행을 재개한다.
      </li>
    </ol>
  <li>
    <strong>인터럽트 요청 신호</strong>란 인터럽트를 하기 전에 지금 작업에 <strong>끼어들어도 되는지 확인</strong>하는 것을 의미한다.
  </li>
    <ul>
      <li>
        CPU가 인터럽트 요청을 수행하기 위해서는 플래그 레지스터의 <strong>인터럽트 플래그(interrupt flag)</strong>가 활성화되어 있어야 한다.
      </li>
        <ul>
          <li>
            인터럽트 플래그는 하드웨어 인터럽트를 받아들일지, 무시할지를 결정하는 플래그이다.
          </li>
        </ul>
      <li>
        단, 무시할 수 없는 인터럽트 요청도 존재한다. <strong>가장 먼저 처리</strong>해야하는 인터럽트이며 대표적으로는 <strong>정전</strong>이나 <strong>하드웨어 고장</strong>으로 인한 인터럽트가 해당핞다.
      </li>
    </ul>
  <li>
    CPU가 인터럽트 요청을 받아들이기로 했다면 CPU는 <strong>인터럽트 서비스 루틴(ISR; Interrupt Service Routine)</strong>이라는 프로그램을 실행한다.
  </li>
    <ul>
      <li>
        인터럽트 서비스 루틴은 인터럽트를 처리하기 위한 프로그램으로 <strong>인터럽트 핸들러(interrupt handler)</strong>라고도 부른다.
      </li>
      <li>
        일반적으로 어떤 인터럽트가 발생했을 때 해당 <strong>인터럽트를 어떻게 처리하고 작동</strong>해야 할지에 대한 정보로 이루어진 프로그램이다.
      </li>
      <li>
        인터럽트를 처리하는 방법은 입출력장치마다 다르기 때문에 각기 다른 인터럽트 서비스 루틴을 가지고 있어야 한다.
      </li>
        <ul>
          <li>
            이 때문에 수많은 인터럽트 서비스 루틴을 구분하기 위해 <strong>인터럽트 벡터(interrupt vector)</strong>를 이용한다. 이는 인터럽트 서비스 루틴을 <strong>식별하기 위한 정보</strong>이다.
          </li>
          <li>
            인터럽트 벡터를 알면 <strong>인터럽트 서비스 루틴의 시작 주소</strong>를 알 수 있기 때문에 CPU는 인터럽트 벡터를 통해 특정 인터럽트 서비스 루틴을 <strong>처음부터 실행</strong>할 수 있다.
          </li>
          <li>
            CPU는 하드웨어 인터럽트 요청을 보낸 대상으로부터 <strong>데이터 버스</strong>를 통해 인터럽트 벡터를 전달 받는다.
          </li>
          <li>
            인터럽트 서비스 루틴도 결국 프로그램 카운터를 비롯한 <strong>레지스터</strong>들을 사용하여 실행된다.
          </li>
          <li>
            인터럽트 요청을 받기 전까지 CPU가 수행하고 있었던 일은 인터럽트 서비스 루틴이 끝나면 되돌아와서 마저 수행을 해야하기 때문에 진행 중인 정보는 <strong>스택에 백업</strong>을 해 둔다.
          </li>
        </ul>
    </ul>
  <li>
    핵심 정리
  </li>
    <ul>
      <li>
        인터럽트 요청 신호: CPU의 작업을 방해하는 인터럽트에 대한 요청
      </li>
      <li>
        인터럽트 플래그: 인터럽트 요청 신호를 받아들일지 무시할지를 결정하는 비트
      </li>
      <li>
        인터럽트 벡터: 인터럽트 서비스 루틴의 시작 주소를 포함하는 인터럽트 서비스 루틴의 식별 정보
      </li>
      <li>
        인터럽트 서비스 루틴: 인터럽트를 처리하는 프로그램
      </li>
    </ul>
</ul>

<h4>예외의 종류</h4>
<ul>
  <li>
    예외의 종류에는 폴트, 트랩, 중단, 소프트웨어 인터럽트가 있다. 
  </li>
  <li>
    예외가 발생하면 CPU는 예외를 처리하고 돌아오는데 이때 <strong>예외가 발생한 명령어</strong>부터 처리하는지 아니면 예외가 발생한 명령어의 <strong>다음 명령어</strong>부터 실행하냐에 따라 폴트와 트랩으로 나뉜다.
  </li>
  <li>
    <strong>폴트(fault)</strong>는 예외를 처리한 직후 <strong>예외가 발생한 명령어</strong>부터 실행을 재개한다.
  </li>
    <ul>
      <li>
        예를 들어 보조 기억 장치의 데이터가 필요한 경우 잠시 예외를 발생시켜 데이터를 가져온 뒤 해당 명령어부터 다시 시행하는 경우가 해당한다.
      </li>
    </ul>
  <li>
    <strong>트랩(trap)</strong>은 예외를 처리한 직후 <strong>예외가 발생한 명령어의 다음 명령어</strong>부터 실행을 재개한다.
  </li>
    <ul>
      <li>
        CPU가 특정 코드가 실행된 순간의 프로그램 상태를 보려는 경우 다음 코드 실행 전에 멈추는 경우가 해당한다. (주로 디버깅).
      </li>
    </ul>
  <li>
    <strong>중단(abort)</strong>은 CPU가 실행 중인 프로그램을 <strong>강제로 중단</strong>시킬 수밖에 없는 심각한 오류를 발견헸을 때 발생하는 예외이다.
  </li>
  <li>
    <strong>소프트웨어 인터럽트(software interrupt)</strong>는 <strong>시스템 호출</strong>이 발생했을 때 나타난다.
  </li>
</ul>