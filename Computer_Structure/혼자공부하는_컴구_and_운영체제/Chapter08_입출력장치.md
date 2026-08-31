<h1>1. 장치 컨트롤러와 장치 드라이버</h1>
<ul>
  <li>
    이번 장에서는 <strong>장치 컨트롤러</strong>와 <strong>장치 드라이버</strong>에대해 배운다.
  </li>
  <li>
    입출력장치에는 보조기억장치도 정보를 주고 받는 방식이 크게 다르지 않기 때문에 보조기억장치에도 이번 장의 내용이 해당된다 볼 수 있다.
  </li>
</ul>

<br>

<h2>1-1. 장치 컨트롤러</h2>
<ul>
  <li>
    입출력장치는 앞서 학습한 CPU, 메모리보다 다루기가 더 힘든데 두 가지 이유가 있다.
  </li>
</ul>

<h3>1-1-1. 첫째, 입출력장치에는 종류가 너무나도 많다.</h3>
<ul>
  <li>
    입출력장치는 정말 많고 장치마다 속도, 데이터 전송 형식 등도 다양하다. 따라서 다양한 입출력장치와 정보를 주고받는 방식을 <strong>규격화</strong> 어렵다.
  </li>
</ul>

<h3>1-1-2. 둘째, 일반적으로 CPU와 메모리의 데이터 전송률은 높지만 입출력장치의 데이터 전송률은 낮다</h3>
<ul>
  <li>
    <strong>전송률(transfer rate)</strong>이란 데이터를 얼마나 <strong>빨리 교환</strong>할 수 있는지를 나타내는 지표이다.
  </li>
  <li>
    CPU와 메모리처럼 전송률이 높다면 상관없지만 키드보드와 마우스처럼 전송률이 낮은 장치는 <strong>데이터를 조금씩만</strong> 주고받을 수 있다.
  </li>
    <ul>
      <li>
        어떤 입출력장치는 CPU나 메모리보다 전송률이 높은 경우도 있으나 결국 CPU나 메모리와 <strong>전송률이 비슷하지 않는 문제</strong>는 여전하다.
      </li>
    </ul>
  <li>
    입출력장치의 전송률이 비슷하지 않기 때문에 입출력장치는 컴퓨터에 바로 연결되지 않고 <strong>장치 컨트롤러(device controller)</strong>라는 하드웨어를 통해 연결된다.
  </li>
    <ul>
      <li>
        장치 컨트롤러는 <strong>입출력 제어기(I/O controller)</strong>와 <strong>입출력 모듈(I/O module)</strong> 등으로 다양하게 불리기도 한다.
      </li>
    </ul>
  <li>
    모든 입출력장치는 <strong>각자의 장치 컨트롤러</strong>를 통해 컴퓨터 내부와 정보를 주고받고, 장치 컨트롤러는 <strong>하나 이상의 입출력장치</strong>에 연결되어 있다.
  </li>
  <li>
    장치 컨트롤러는 일반적으로 다음과 같은 역할을 통해 앞에서 언급한 문제들을 해결한다.
  </li>
    <ul>
      <li>
        CPU와 입출력장치 간의 통신 중계.
      </li>
      <li>
        오류 검출
      </li>
      <li>
        데이터 버퍼링
      </li>
        <ul>
          <li>
            버퍼링(buffering)은 전송률이 가장 높은 장치와 낮은 장치 사이에 주고받는 데이터를 <strong>버퍼(buffer)</strong>라는 임시 저장 공간에 전송하여 <strong>전송률을 비슷하게 맞추는 방법</strong>이다.
          </li>
          <li>
            버퍼에 데이터를 조금씩 모아 한꺼번에 보내거나 데이터르 한 번에 많이 받아 조금씩 내보내는 방법이다.
          </li>
        </ul>
    </ul>
  <li>
    장치 컨트롤러 내부는 다양하게 구성되지만 <strong>데이터 레지스터(data register)</strong>, <strong>상태 레지스터(status register)</strong> 그리고 <strong>제어 레지스터(control register)</strong>세 가지를 기억하면된다.
  </li>
    <ul>
      <li>
        상태 레지스터와 제어 레지스터는 하나의 레지스터로 사용되기도 한다.
      </li>
      <li>
        <strong>데이터 레지스터</strong>는 CPU와 입출력장치 사이에 <strong>주고받을 데이터</strong>가 담기는 레지스터이다.
      </li>
        <ul>
          <li>
            데이터 레지스터가 <strong>버퍼</strong>의 역할을 한다.
          </li>
        </ul>
      <li>
        <strong>상태 레지스터</strong>에는 입출력장치가 입출력 작업을 할 준비가 되었는지, 입출력 장업이 완료되었는지, 입출력자치에 오류는 없는지 등의 <strong>상태 정보</strong>가 저장된다.
      </li>
      <li>
        <strong>제어 레지스터</strong>는 입출력장치가 수행할 내용에 대한 <strong>제어 정보</strong>와 <strong>명령</strong>을 저장한다.
      </li>
    </ul>
  <li>
    레지스터들에 담긴 값들은 버스를 타고 CPU나 다른 입출력장치로 전달되기도 하고, 장치 컨트롤러에 연결된 입출력장치로 전달된다.
  </li>
</ul>

<br>

<h2>1-2. 장치 드라이버</h2>
<ul>
  <li>
    새로운 장치를 컴퓨터에 연결하려면 장치 드라이버를 설치해야 한다.
  </li>
  <li>
    <strong>장치 드라이버(device driver)</strong>란 장치 컨트롤러의 동작을 감지하고 제어하여 장치 컨트롤러가 <strong>컴퓨터 내부와 정보를 주고받을 수 있게 하는 프로그램</strong>이다.
  </li>
  <li>
    프로그램이기 때문에 실행 과정에서 <strong>메모리</strong>에 저장된다.
  </li>
  <li>
    장치 컨트롤러가 입출력장치를 연결하기 위한 <strong>하드웨어적인 통로</strong>라면, 장치 드라이버는 입출력장치를 연결하기 위한 <strong>소프트웨어적 통로</strong>이다.
  </li>
</ul>

<h4>장치 드라이버를 인식하고 실행하는 주체</h4>
<ul>
  <li>
    장치 드라이버를 인식하고 실행하는 주체는 윈도우, mac OS와 같은 <strong>운영체제</strong>이다.
  </li>
    <ul>
      <li>
        <strong>운영체제가 장치 드라이버를 인식하고 실행</strong>할 수 있다면 해당 장치는 컴퓨터 내부와 정보를 주고받을 수 있다.
      </li>
    </ul>
  <li>
    장치 드라비어는 <strong>운영체제</strong>가 기본으로 제공하는 경우도 있지만 <strong>장치 제작자</strong>가 따로 제공하기도 한다.
  </li>
    <ul>
      <li>
        장치 제작자가 제공하는 경우 입출력장치는 <strong>해당 드라이버를 OS에 직접 설치</strong>해야만 사용이 가능하다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 다양한 입출력 방법</h1>
<ul>
  <li>
    장치 컨트롤러가 정보를 주고받는 방법에는 크게 <strong>프로그램 입출력</strong>, <strong>인터럽트 기반 입출력</strong>, <strong>DMA 입출력</strong>이 있다.
  </li>
</ul>

<br>

<h2>2-1. 프로그램 입출력</h2>
<ul>
  <li>
    프로그래밍 입출력(programming I/O)은 기본적으로 <strong>프로그램 속 명령어</strong>로 입출력장치를 제어하는 방법이다.
  </li>
    <ul>
      <li>
        <strong>CPU</strong>가 프로그램 속 명령어를 실행하는 과정에서 <strong>입출력 명령어</strong>를 만나면 CPU는 입출력장치에 연결된 장치 컨트롤러와 상호작용하며 작업을 수행한다.
      </li>
    </ul>
  <li>
    전체적인 작업을 흐름으로 정리하면 아래와 같다.
  </li>
    <ol>
      <li>
        메모리에 저장된 정보를 하드 디스크에 백업한다는 것은 하드 디스크에 <strong>새로운 정보를 쓴다</strong>는 것과 같다.
      </li>
      <li>
        CPU는 하드 디스크 컨트롤러의 <strong>제어 레지스터에 쓰기 명령</strong>을 보낸다.
      </li>
      <li>
        하드 디스크 컨트롤러는 하드 디스크의 상태를 확인한다. 상태가 준비된 상태라면 하드 디스크 컨트롤러는 <strong>상태 레지스터에 준비되었다고 표시</strong>한다.
      </li>
      <li>
        CPU는 상태 레지스터를 <strong>주기적</strong>으로 읽으며 하드 디스크의 <strong>준비 여부를 확인</strong>한다.
      </li>
      <li>
        하드 디스크가 준비된 것을 CPU가 알게 되면 <strong>백업할 정보</strong>를 <strong>데이터 레지스터</strong>에 쓴다.
      </li>
        <ul>
          <li>
            쓰기 작업이 완료되지 않았다면 첫 번째 단계부터 반복하고 완료가 되었다면 작업을 종료한다.
          </li>
        </ul>
    </ol>
  <li>
    CPU는 장치 컨트롤러의 레지스터 값을 읽고 쓰는데 <strong>메모리 맵 입출력</strong>과 <strong>고립형 입출력</strong>을 사용한다.
  </li>
</ul>

<h3>2-1-1. 메모리 맵 입출력</h3>
<ul>
  <li>
    <strong>메모리 맵 입출력(memory-mapped I/O)</strong>은 메모리에 접근하기 위한 주소 공간과 입출력장치에 접근하기 위한 주소 공간을 <strong>하나의 주소 공간</strong>으로 간주하는 방법이다.
  </li>
    <ul>
      <li>
        1,024개의 주소를 표현할 수 있는 컴퓨터라면 512는 메모리 주소를, 나머지 512는 장치 컨트롤러의 레지스터를 표현하기 위해 사용한다.
      </li>
    </ul>
  <li>
    하나의 주소 공간에서 처리를하기 때문에 메모리에 접근하는 명령어와 입출력장치에 접근하는 <strong>명령어는 굳이 다를 필요가 없다</strong>.
  </li>
</ul>

<h3>2-1-2. 고립형 입출력</h3>
<ul>
  <li>
    고립형 입출력(isolated I/O)은 메모리를 위한 주소 공간과 입출력장치를 위한 주소 공간을 <strong>분리하는 방법</strong>이다.
  </li>
  <li>
    예를 들어 1,024개의 주소 공간을 가진 컴퓨터라면 <strong>두 개의 독립적인 주소 공간</strong>을 두어 1,024개의 주소 공간은 <strong>메모리에</strong>서 활용하고, <strong>입출력장치</strong>에도 1,024개의 주소 공간을 두어 활용할 수 있다.
  </li>
  <li>
    따라서 고립형 입출력 방식에서 CPU는 입출력장치에 접근하기 위해 메모리에 접근하는 명령어와 <strong>다른(입출력 읽기/쓰기 선을 활성화시키는) 입출력 명령어</strong>를 사용한다.
  </li>
</ul>

<br>

<h2>2-2. 인터럽트 기반 입출력</h2>
<ul>
  <li>
    입출력장치에 의한 하드웨어 인터럽트는 정확히는 입출력장치가 아닌 <strong>장치 컨트롤러</strong>에 의해 발생한다.
  </li>
    <ul>
      <li>
        CPU는 장치 컨트롤러에 입출력 작업을 명령하고, <strong>장치 컨트롤러</strong>가 입출력장치를 제어하며 입출력을 수행하는 동안 <strong>CPU는 다른 일</strong>을 할 수 있다.
      </li>
    </ul>
  <li>
    장치 컨트롤러가 입출력 작업을 끝낸 뒤 <strong>CPU에게 인터럽트 요청 신호</strong>를 보내면 CPU는 하던 일을 <strong>잠시 백업</strong>하고 <strong>인터럽트 서비스 루틴을 실행</strong>한다.
  </li>
  <li>
    이렇게 인터럽트를 기반으로 하는 입출력을 <strong>인터럽트 기반 입출력(Interupt-Driven I/O)</strong>이라고 한다.
  </li>
</ul>

<h4>폴링</h4>
<ul>
  <li>
    인터럽트와 자주 비교되는 개념 중 <strong>폴링(polling)</strong>이 있다.
  </li>
    <ul>
      <li>
        폴링이란 입출력장치의 상태는 어떤지, 처리할 데이터가 있는지를 <strong>주기적으로 확인</strong>하는 방식이다.
      </li>
    </ul>
  <li>
    단, 폴링은 인터럽트와 달리 <strong>주기적으로 CPU가 장치 상태 레지스터를 반복해서 확인</strong>하기 때문에, 이동안 다른 작업을 하는 것이 어렵다. 이를 <strong>바쁜 대기(busy waiting)</strong>이라 한다.
  </li>
  <li>
    모니터, 키보드, 마우스 등 <strong>여러 입출력장치에서 인터럽트가 동시에 발생</strong>한 경우 이를 처리하는 방법에는 몇 가지가 있다.
  </li>
    <ul>
      <li>
        간단한 방법에는 인터럽트가 발생한 순서대로 처리하는 방법이 있다.
      </li>
        <ul>
          <li>
            CPU가 <strong>플래그 레지스터 속 인터럽트 비트를 비활성화</strong>한 채 인터럽트를 처리하며 다른 입출력장치에 의한 하드웨어 인터럽트를 받아들이지 않는다.
          </li>
        </ul>
      <li>
        일반적으로 모든 인터럽트를 순차적으로 처리할 수 없기 때문에 우선순위를 고려하여 <strong>우선순위가 높은 인터럽트 순으로 여러 인터럽트를 처리</strong>하는 방법이 있다.
      </li>
        <ul>
          <li>
            예를 들어 인터럽트 A를 처리하는 도중 인터럽트 B가 발생하였고 인터럽트 B의 우선 순위가 더 높다면 인터럽트 B를 먼저 처리한 뒤 다시 A를 처리한다.
          </li>
          <li>
            플래그 레지스터 속 <strong>인터럽트 비트가 활성화</strong>되어 있는 경우, 혹은 인터럽트 비트를 비활성화해도 무시할 수 없는 인터럽트인 <strong>NMI(Non-Maskable Interrupt)</strong>가 발생한 경우가 해당한다.
          </li>
          <li>
            우선순위를 반영하여 다중 인터럽트를 처리하는 방법에는 여러 가지가 있지만, 많은 컴퓨터에서는 <strong>프로그래머블 인터럽트 컨트롤러(PIC: Programmable Interrupt Controller)</strong>라는 하드웨어를 이용한다.
          </li>
            <ul>
              <li>
                PIC는 여러 장치 컨트롤러에 연결되어 장치 컨트롤러에서 보낸 하드웨어 인터럽트 요청들의 <strong>우선순위를 판별</strong>하고 <strong>CPU에 지금 처리해야할 하드웨어 인터럽트</strong>는 무엇인지 알려준다.
              </li>
              <li>
                PIC의 다중 인터럽트 처리 과정은 다음과 같다.
              </li>
                <ol>
                  <li>
                    PIC가 장치 컨트롤러에서 <strong>인터럽트 요청 신호(들)</strong>을 받아들인다.
                  </li>
                  <li>
                    PIC는 인터럽트 우선순위를 판단한 뒤 CPU에 처리해야 할 <strong>인터럽트 요청 신호</strong>를 보낸다.
                  </li>
                  <li>
                    CPU는 PIC에 <strong>인터럽트 확인 신호</strong>를 보낸다.
                  </li>
                  <li>
                    PIC는 데이터 버스를 통해 CPU에 <strong>인터럽트 벡터</strong>를 보낸다.
                  </li>
                  <li>
                    CPU는 인터럽트 벡터를 통해 인터럽트 요청의 주체를 알게 되고, 해당 장치의 <strong>인터럽트 서비스 루틴</strong>을 실행한다.
                  </li>
                </ol>
              <li>
                일반적으로 더 많고 복잡한 장치들의 인터럽트를 관리하기 위해 PIC를 <strong>두 개 이상 계층적</strong>으로 구성한다.
              </li>
              <li>
                PIC가 무시할 수 없는 인터럽트인 NMI까지 우선순위를 판별하지는 않는다. NMI는 우선순위가 가장 높아 판별이 불필요하기 때문이다.
              </li>
                <ul>
                  <li>
                    즉 인터럽트 비트를 통해 막을 수 있는 <strong>하드웨어 인터럽트</strong>만 관리한다.
                  </li>
                </ul>
            </ul>
        </ul>
    </ul>
</ul>

<br>

<h2>2-3. DMA 입출력</h2>
<ul>
  <li>
    프로그램 기반 입출력과 인터럽트 기반 입출력의 공통점은 입출력장치와 메모리 간의 데이터 이동은 <strong>CPU가 주도</strong>하고, 이동하는 데이터도 반드시 <strong>CPU를 거친다</strong>는 점이다.
  </li>
    <ul>
      <li>
        입출력장치 데이터를 메모리에 저장하는 경우는 다음과 같다.
      </li>
        <ol>
          <li>
            CPU는 장치 컨트롤러에서 입출력장치 데이터를 하나씩 읽어 레지스터에 적재한다.
          </li>
          <li>
            적재한 데이터를 다시 메모리에 저장한다.
          </li>
        </ol>
      <li>
        메모리 속 데이터를 입출력장치에 내보내는 경우는 다음과 같다.
      </li>
        <ul>
          <li>
            CPU는 메모리에서 데이터를 하나씩 읽어 레지스터에 적재한다.
          </li>
          <li>
            적재한 데이터를 하나씩 입출력장치에 보낸다.
          </li>
        </ul>
    </ul>
  <li>
    입출력장치와 메모리 사이에 전송되는 모든 데이터가 반드시 CPU를 거쳐야 한다면 CPU는 입출력장치에 시간을 뺏기게 되며 하드 디스크 백업과 같은 대용량 데이터를 옮길 때는 CPU 부담이 더욱 커진다.
  </li>
    <ul>
      <li>
        위와 같은 문제를 해결하고자 <strong>DMA(Direct Memory Access)</strong>를 활용한다. DMA는 이름 그대로 <strong>메모리에 직접 접근</strong>할 수 있는 입출력 기능이다.
      </li>
    </ul>
  <li>
    DMA 입출력을 하기 위해서는 시스템 버스에 연결된 <strong>DMA 컨트롤러</strong>라는 하드웨어가 필요하다.
  </li>
</ul>

<h3>2-3-1. DMA 입출력 과정</h3>
<ul>
  <li>
    일반적으로 DMA 입출력은 아래와 같은 과정으로 이루어진다.
  </li>
    <ol>
      <li>
        CPU는 <strong>DMA 컨트롤러</strong>에 입출력장치의 주소, 수행할 연산(읽기/쓰기), 읽거나 쓸 메모리의 주소 등과 같은 정보로 <strong>입출력 작업을 명령</strong>한다.
      </li>
      <li>
        DMA 컨트롤러는 <strong>CPU 대신</strong> 장치 컨트롤러와 상호작용하며 입출력 작업을 수행한다. 이때 DMA 컨트롤러는 필요한 경우 <strong>메모리에 직접 접근</strong>하여 정보를 읽거나 쓴다.
      </li>
      <li>
        입출력 작업이 끝나면 DMA 컨트롤러는 <strong>CPU에 인터럽트</strong>를 걸어 작업이 끝났음을 알린다.
      </li>
    </ol>
  <li>
    메모리 내의 정보를 하드 디스크에 백업하는 작업이 DMA 입출력으로 이루러지는 과정은 아래와 같다.
  </li>
    <ol>
      <li>
        <strong>CPU는 DMA 컨트롤러</strong>에 하드 디스크 주소, 수행할 연산(쓰기), 백업할 내용이 저장된 메모리의 주소 등의 정보를 함께 <strong>입출력 작업을 명령</strong>한다.
      </li>
      <li>
        DMA 컨트롤러는 CPU를 거치지 않고 <strong>메모리와 직접 상호작용</strong>하며 백업할 정보를 읽어오고 이를 <strong>하드 디스크의 장치 컨트롤러</strong>에 내보낸다.
      </li>
      <li>
        백업이 끝나면 DMA 컨트롤러는 <strong>CPU에게 인터럽트</strong>를 걸어 작업이 끝났음을 알린다.
      </li>
    </ol>
  <li>
    단, DMA 컨트롤러는 시스템 버스로 메모리에 직접 접근이 가능하지만, <strong>시스템 버스는 공용 자원이기 때문에 동시에 사용이 불가</strong>하다. 즉 DMA가 사용 중일 때에는 <strong>CPU가 사용할 수 없는 문제</strong>가 발생한다.
  </li>
    <ul>
      <li>
        따라서 DMA는 CPU가 시스템 버스를 <strong>이용하지 않을 때마다 조금씩</strong> 시스템 버스를 이용하거나, CPU가 일시적으로 시스템 버스를 이용하지 않도록 <strong>허락</strong>을 구하고 활용한다.
      </li>
    </ul>
  <li>
    CPU 입장에서는 버스에 접근하는 주기를 도둑 맞는 느낌이기 때문에 DMA의 시스템 버스 이용을 <strong>사이클 스틸링(cycle stealing)</strong>이라고 부른다.
  </li>
</ul>

<h3>2-3-2. 입출력 버스</h3>
<ul>
  <li>
    CPU, 메모리, DMA 컨트롤러와 장치 컨트롤러가 모두 같은 버스를 공유하는 구성에서 DMA가 한 번 메모리에 접근할 때마다 <strong>시스템 버스를 두 번 사용</strong>하는 부작용이 있다.
  </li>
    <ul>
      <li>
        이런 문제를 해결하기 위해 DMA 컨트롤러와 장치 컨트롤러들을 <strong>입출력 버스(input/outpu bus)</strong>라는 별도의 버스에 연결하여 해결할 수 있다.
      </li>
      <li>
        입출력 버스를 통해 DMA 컨트롤러와 장치 컨트롤러가 서로 데이터를 전송할 때 시스템 버스를 이용하지 않아 문제가 해결된다.
      </li>
      <li>
        현대 대부분의 컴퓨터에는 입출력 버스가 존재한다.
      </li>
    </ul>
  <li>
    입출력 버스에는 <strong>PCI(Peripheral Component Interconnect) 버스</strong>, <strong>PCI Express(PCIe) 버스</strong> 등 여러 종류가 있다.
  </li>
    <ul>
      <li>
        <strong>메인 보드의 PCIe 슬롯</strong>은 <strong>입출력장치들을 PCIe 버스와 연결</strong>해 주는 통로의 역할을 한다.
      </li>
      <li>
        사용하는 대부분의 거의 모든 입출력장치들은 위와 같은 방식으로 시스템 버스를 타고 CPU와 정보를 주고받는다.
      </li>
    </ul>
  <li>
    PCIe는 주로 CPU와 명령어와 인터럽트를 주고받는다.
  </li>
</ul>

<h4>더욱 발전한 DMA, 입출력 채널</h4>
<ul>
  <li>
    최근에는 메모리에 직접 접근할 뿐만 아니라 입출력 명령어를 직접 인출하고, 해석하고, 실행까지 하는 일종의 <strong>입출력 전용 CPU</strong>가 만들어 졌으며 이를 <strong>입출력 프로세서(IOP, Input/Output Processor)</strong> 혹은 <strong>입출력 채널(Input/Output Channel)</strong>이라고 부른다.
  </li>
  <li>
    PCI가 데이터의 통로 역할을 하고 메인 CPU가 명령어를 처리했다면 입출력 채널은 <strong>메인 CPU가 하던 작업을 전담하는 CPU가 독립적으로 존재</strong>한다.
  </li>
</ul>