<h1>1. RAM의 특징과 종류</h1>
<ul>
  <li>
    이번 절에서는 메모리라는 용어로 지칭되는 RAM과 DRAM, SRAM, SDRAM, DDR SDREAM에 대해 학습한다.
  </li>
</ul>

<br>

<h2>1-1. RAM의 특징</h2>
<ul>
  <li>
    RAM에는 실행할 <strong>프로그램의 명령어</strong>와 <strong>데이터</strong>가 저장된다.
  </li>
  <li>
    다만 RAM은 전원을 끄면 저장된 내용이 사라지는 <strong>휘발성 저장 장치(volatile memory)</strong> 이다.
  </li>
    <ul>
      <li>
        반대로 전원이 꺼져도 저장된 내용이 유지되는 <strong>비휘발성 저장 장치(non-volatile memory)</strong>도 있으며 하드 디스크, SSD, CD-ROM, USB 메모리와 같은 <strong>보조기억장치</strong>가 대표적이다.
      </li>
    </ul>
  <li>
    보조기억장치는 전원을 꺼도 내용을 유지하지만 CPU는 <strong>보조기억장치에 직접 접근</strong>을 할 수가 없다.
  </li>
    <ul>
      <li>
        위와 같은 이유로 보조기억장치인 비휘발성 저장 장치에는 <strong>보관할 대상</strong>을 저장하고, 휘발성 저장 장치인 RAM에는 <strong>실행할 대상</strong>을 저장한다.
      </li>
      <li>
        CPU가 실행하고 싶은 프로그램이 보조기억장치에 있다면 이를 <strong>RAM으로 복사하여 저장</strong>한 뒤 실행한다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. RAM의 용량과 성능</h2>
<ul>
  <li>
    RAM의 용량이 크다면 보조기억장치에서 많은 데이터를 가져와 <strong>미리 RAM에 저장</strong>할 수 있지만, 그렇지 못하다면 매 실행마다 보조기억장치에서 RAM으로 복사를 해와야하기 때문에 <strong>속도</strong>가 느려진다.
  </li>
    <ul>
      <li>
        반대로 RAM의 용량이 크면 많은 프로그램들을 <strong>동시에 빠르게 실행</strong>하는 데 유리하다.
      </li>
    </ul>
  <li>
    단, RAM의 용량이 커지면 프로그램 실행 속도가 어느 정도 증가하는 것은 맞지만, 용량이 필요 이상으로 커지면 속도가 비례하여 커지지 않는다.
  </li>
    <ul>
      <li>
        미리 데이터를 올려둘 수는 있지만 결국 데이터를 복사해서 올리는 데에는 시간이 걸리기 때문이다.
      </li>
    </ul>
</ul>

<br>

<h2>1-3. RAM의 종류</h2>
<h3>1-3-1. DRAM</h3>
<ul>
  <li>
    DRAM은 Dynamic RAM의 준말로 저장된 데이터가 <strong>동적으로 변하는</strong> RAM을 의미한다.
  </li>
  <li>
    시간이 지나면 저장된 데이터가 점차 사라지기 때문에 <strong>데이터의 소멸</strong>을 막기 위해 일정 주기로 데이터를 <strong>재활성화(다시 저장)</strong>해야 한다.
  </li>
  <li>
    데이터를 재활성화해야한다는 단점은 있지만 소비 전력이 비교적 낮고 저렴하며 집적도가 높아 대용량으로 설계하기 용이하다는 장점으로인해 일반적으로 사용하는 메모리이다.
  </li>
</ul>

<h3>1-3-2. SRAM</h3>
<ul>
  <li>
    SRAM은 Static RAM의 준말로 저장된 데이터가 변하지 않는 <strong>정적인 RAM</strong>을 의미한다.
  </li>
  <li>
    DRAM과 달리 시간이 지나도 저장된 데이터가 사라지지 않으며 주기적으로 데이터를 재활성할 필요도 없고 DRAM보다 일반적으로 속도도 더 빠르다.
  </li>
    <ul>
      <li>
        그렇다고 SRAM이 비휘발성 메모리인 것은 아니며 전원이 공급되지 않으면 저장된 데이터가 사라지는 것은 동일하다.
      </li>
    </ul>
  <li>
    하지만 여전히 SRAM이 DRAM보다 집적도가 낮고, 소비 전력이 크며 가격도 더 비싸기 때문에 일반적으로 사용되지는 않는다.
  </li>
  <li>
    SRAM이 사용되는 경우는 대용량으로 만들어질 필요는 없지만 속도가 빨라야하는 저장 장치, 예를 들어 <strong>캐시 메모리</strong>에 주로 사용한다.
  </li>
</ul>

<h3>1-3-3. SDRAM</h3>
<ul>
  <li>
    SDRAM(Synchronous Dynamic RAM)은 <strong>클럭 신호와 동기화</strong>된 발전된 형태의 <strong>DRAM</strong>이다.
  </li>
    <ul>
      <li>
        클럭 신호와 동기화되었다는 의미는 <strong>클럭 타이밍</strong>에 맞추어 <strong>CPU와 정보</strong>를 주고받을 수 있음을 의미한다.
      </li>
      <li>
        요약하면 SDRAM은 클럭에 맞춰 동작하며 클럭마다 CPU와 정보를 주고받을 수 있는 DRAM이다.
      </li>
    </ul>
</ul>

<h3>1-3-4. DDR SDRAM</h3>
<ul>
  <li>
    DDR SDRAM(Double Data Rate SDRAM)은 최근 흔히 사용되는 RAM이며 SDRAM의 <strong>대역폭</strong>을 넓혀 속도를 빠르게 만든 SDRAM이다.
  </li>
    <ul>
      <li>
        대역폭(data rate)이란 <strong>데이터를 주고받는 길의 너비</strong>를 의미한다.
      </li>
    </ul>
  <li>
    이름에 맞게(Double) SDRAM과 비교했을 <strong>두 배의 대역폭</strong>으로 한 클럭당 <strong>두 번씩</strong> CPU와 데이터를 주고받을 수 있다.
  </li>
    <ul>
      <li>
        이런 이유에서 한 클럭당 하나씩 데이터를 주고받을 수 있는 SDRAM을 SDR SDRAM(Single Data Rate SDRAM)이라 부르기도 한다.
      </li>
    </ul>
  <li>
    DDR2 SDRAM은 DDR SDRAM보다 대역폭이 두 배 넓고, DDR3 SDRAM은 DDR2 SDRAM보다 두 배 널고 SDR SDRAM보다 여덟 배 넓은 SDRAM이다. 최근 흔히 사용하는 DDR4 SDRAM은 SDR SDRAM보다 열여섯 배 넓은 대역폭을 갖는다.
  </li>
</ul>

<br><br>

<h1>2. 메모리의 주소 공간</h1>
<ul>
  <li>
    메모리에는 정확히는 물리 주소와 논리 주소가 존재한다. <strong>물리 주소</strong>는 <strong>하드웨어</strong>가 사용하는 주소이고, <strong>논리 주소</strong>는 <strong>CPU와 실행 중인 프로그램</strong>이 사용하는 주소이다.
  </li>
</ul>

<br>

<h2>2-1. 물리 주소와 논리 주소</h2>
<ul>
  <li>
    CPU와 메모리에 저장되어 실행 중인 프로그램은 메모리 몇 번지에 무엇이 저장되어 있는지 다 알지 못한다.
  </li>
    <ul>
      <li>
        메모리에 저장된 정보는 시시각각 변한다. 예를 들어 새롭게 실행되는 프로그램이 시시때때로 적재되고, 실행이 끝난 프로그램은 삭제되며 같은 프로그램을 실행해도 실행할 때마다 적재되는 주소가 달라질 수 있다.
      </li>
    </ul>
  <li>
    메모리가 사용하는 <strong>물리 주소(physical address)</strong>는 말 그대로 정보가 실제로 저장되는 <strong>하드웨어상의 주소</strong>를 의미한다.
  </li>
  <li>
    <strong>논리 주소(logical address)</strong>는 실행 중인 프로그램 각각에 부여된 <strong>0번지부터 시작되는 주소</strong>를 의미한다.
  </li>
    <ul>
      <li>
        프로그램 실행에 필요한 정보는 물리 주소가 어디서 시작하냐가 아니라 0번지부터 읽어오는 정보만 중요하기 때문이다. (p188 참고).
      </li>
    </ul>
  <li>
    논리 주소와 물리 주소 간의 변환은 CPU와 주소 버스 사이에 위치한 <strong>메모리 관리 장치(MMU; Memory Management Unit)</strong>라는 하드웨어에 의해 수행된다.
  </li>
    <ul>
      <li>
        MMU는 CPU가 발생시킨 논리 주소에 <strong>베이스 레지스터 값</strong>을 더하여 논리 주소를 물리 주소로 변환한다.
      </li>
    </ul>
  <li>
    논리 주소를 사용하지 않는다면 프로그램의 물리 주소의 할당이 달라질 때마다 포인터의 주소를 함께 수정해 주어야 한다. 반면 논리 주소를 사용하면 <strong>베이스 레지스터</strong>의 값만 수정하면 된다.
  </li>
    <ul>
      <li>
        베이스 레지스터는 프로그램의 가장 작은 물리 주소, 즉 프로그램의 <strong>첫 물리 주소</strong>를 저장하는 것이고 논리 주소는 프로그램의 시작점으로부터 <strong>떨어진 거리</strong>이다.
      </li>
    </ul>
</ul>

<br>

<h2>2-2. 메모리 보호 기법</h2>
<ul>
  <li>
    논리 주소 범위를 벗어나는 명령어 실행을 방지하고 실행 중인 프로그램이 다른 프로그램에 영향을 받지 않도록 보호할 방법이 필요하다. 이런 역할은 <strong>한계 레지스터(limit register)</strong>라는 레지스터가 담당한다.
  </li>
  <li>
    베이스 레지스터가 실행중인 프로그램의 가장 작은 물리 주소를 저장한다면 한계 레지스터는 <strong>논리 주소의 최대 크기</strong>를 저장한다.
  </li>
    <ul>
      <li>
        즉 프로그램의 물리 주소 범위는 <strong>'베이스 레지스터 값 이상, 베이스 레지스터 값 + 한계 레지스터 값 미만'</strong>이 된다.
      </li>
    </ul>
  <li>
    결국 논리 주소는 한계 레지스터의 값을 넘을 수가 없다. <strong>'논리 주소 + 베이스 레지스터 < 한계 레지스터 + 베이스 레지스터'</strong>를 만족해야하기 때문이다.
  </li>
  <li>
    CPU는 메모리에 접근하기 전에 접근하고자 하는 논리 주소가 한계 레지스터보다 작은지를 항상 검사하며 만약 한계 레지스터보다 높은 논리 주소에 접근하려고 한다면 <strong>인터럽트(트랩)</strong>을 발생시켜 중단한다.
  </li>
</ul>

<br><br>

<h1>3. 캐시 메모리</h1>
<ul>
  <li>
    CPU가 메모리에 접근하는 시간은 CPU 연산 속도보다 느리다. 메모리에 접근하는 속도가 CPU 연산 속도보다 느리다면 연산 속도는 아무런 쓸모가 없어지는데 이를 극복하기 위한 저장 장치가 바로 <strong>캐시 메모리</strong>이다.
  </li>
  <li>
    캐시 메모리의 탄샐 배경과 특징을 이해하기 위해서는 우선 <strong>저장 장치 계층 구조</strong>라는 개념을 이해해야하며 이번 절에서는 이에 대해 학습한다.
  </li>
</ul>

<br>

<h2>3-1. 저장 장치 계층 구조</h2>
<ul>
  <li>
    저장 장치는 아래의 두 명제를 따르기 때문에 <strong>빠르고 용량이 큰</strong> 저장장치는 존재할 수 없다.
  </li>
    <ul>
      <li>
        CPU와 가까운 저장 장치는 빠르고, 멀리 있는 저장 장치는 느리다.
      </li>
      <li>
        속도가 빠른 저장 장치는 저장 용량이 작고, 가격이 비싸다.
      </li>
    </ul>
  <li>
     <strong>용량과 속도의 trade-off 관계</strong>로 인해 일반적으로 컴퓨터는 다양한 저장 장치를 모두 사용하게 된다.
  </li>
  <li>
    컴퓨터가 사용하는 저장 장치들은 <strong>CPU에 얼마나 가까운가</strong>를 기준으로 계층적으로 나타낼 수 있으며 이를 <strong>저장 장치 계층 구조(memory hierachy)</strong>라고 한다.
  </li>
    <ul>
      <li>
        저장 장치 계층 구조를 영문으로 나타내면 memory hierachy, 즉 메모리 계층 구조를 의미하는데 여기서 말하는 메모리는 RAM이 아닌 <strong>일반적인 저장 장치</strong>를 의미한다.
      </li>
      <li>
        CPU에 가까운 저장 장치일수록 용량은 자고 비싸다. 반대로 멀수록 용량은 커지지만 가격은 저렴하다.
      </li>
    </ul>
</ul>

<br>

<h2>3-2. 캐시 메모리</h2>
<ul>
  <li>
    캐시 메모리(cache memory)는 <strong>CPU와 메모리 사이</strong>에 위치하며 레지스터보다 용량이 크고 메모리보다 빠른 <strong>SRAM 기반의 저장 장치</strong>이다.
  </li>
    <ul>
      <li>
        캐시 메모리는 <strong>CPU의 연산 속도</strong>와 <strong>메모리 접근 속도</strong>의 차이를 조금이나마 줄이기 위해 탄생했다.
      </li>
    </ul>
  <li>
    컴퓨터 내부에는 여러 개의 캐시 메모리가 있으며 CPU와 가까운 순서대로 <strong>L1(level 1) 캐시, L2(level 2) 캐시, L3(level 3) 캐시</strong>라고 부른다.
  </li>
    <ul>
      <li>
        메모리의 용량은 L1, L2, L3 순으로 커지고, 속도는 L3, L2, L1 순으로 빨라진다.
      </li>
      <li>
        멀티 코어 프로세서에서 L1-L2-L3 캐시는 일반적으로 <strong>L1 캐시와 L2 캐시</strong>는 <strong>코어마다 고유한 캐시 메모리</strong>로 할당되고, <strong>L3 캐시</strong>는 <strong>여러 코어가 공유</strong>하는 형태로 사용된다.
      </li>
    </ul>
  <li>
    L1 캐시의 경우 접근 속도를 빠르게 하기 위해 명령어만 저장하는 <strong>L1I 캐시</strong>와 데이터만 저장하는 <strong>L1D 캐시</strong>로 분리되는 경우도 있으며 이를 <strong>분리형 캐시(split cache)</strong>라고 한다.
  </li>
  <li>
    저장 장치 계층 구조는 암기할 필요는 없다 클라우드 서비스에서 제공하는 원격 스토리지와 같은 것들도 있기 때문에 언제나 가변될 수 있다.
  </li>
</ul>

<br>

<h2>3-3. 참조 지역성 원리</h2>
<ul>
  <li>
    캐시 메모리는 <strong>CPU가 사용할 법한 대상을 예측하여 저장</strong>한다.
  </li>
    <ul>
      <li>
        이때 자주 사용될 것으로 예측한 데이터가 실제로 들어맞아 캐시 메모리 내 데이터가 CPU에서 활용될 경우 이를 <strong>캐시 히트(cache hit)</strong>라고 한다.
      </li>
      <li>
        반대로 자주 사용될 것으로 예측하여 캐시 메모리에 저장했지만 예측이 틀려 메모리에서 필요한 데이터를 직접 가져와야 하는 경우 이를 <strong>캐시 미스(cache miss)</strong>라고 한다.
      </li>
        <ul>
          <li>
            캐시 미스가 발생하면 CPU가 직접 메모리에서 데이터를 가져와야하기 때문에 성능이 떨어진다.
          </li>
        </ul>
    </ul>
  <li>
    캐시가 히드 되는 비율을 <strong>캐시 적중률(cache hit ratio)</strong>라고 하며 <strong>'캐시 히트 횟수 / (캐시 히트 횟수 + 캐시 미스 횟수)'</strong>로 계산한다.
  </li>
  <li>
    캐시 적중률을 높이기위해 캐시 메모리는 메모리로부터 가져올 데이터를 <strong>참조 지역성 원리(locality of reference, principle of locality)</strong>라는 한 가지 원칙에 따라 가져온다.
  </li>
    <ul>
      <li>
        참조 지역성의 원리란 CPU가 메모리에 접근할 때 주된 경향을 바탕으로 만들어진 원리로 다음과 같다.
      </li>
        <ol>
          <li>
            CPU는 <strong>최근에 접근</strong>했던 메모리 공간에 <strong>다시 접근</strong>하려는 경향이 있다.
          </li>
          <li>
            CPU는 <strong>접근한 메모리 공간 근처</strong>를 접근하려는 경향이 있다.
          </li>
        </ol>
    </ul>
</ul>

<h3>3-3-1. 첫째, '최근에 접근했던 메모리 공간에 다시 접근하려는 경향'이란?</h3>
<ul>
  <li>
    예를 들어 프로그래밍에서 <strong>변수</strong>가 있다. 변수에 값을 저자앟고 나면 언제든 변수에 다시 접근하여 변수에 저장된 값을 사용할 수 있다. 다시 말하면 CPU는 <strong>변수가 저장된 메모리 공간을 언제든 다시 참조</strong>할 수 있다.
  </li>
  <li>
    최근에 접근했던 메모리 공간에 다시 접근하는 경향을 <strong>시간 지역성(temporal locality)</strong>이라고 한다.
  </li>
</ul>

```c
#include <stdio.h>

// num과 i를 여러 번 접근한다.
int main(void) {
    int num = 2;

    for (int i = 1; i <= 9; i++)
        printf("%d X %d = %d\n", num, i, num * i);
    return 0;
}
```

<h3>3-3-2. 둘째, '접근한 메모리 공간 근처를 접근하려는 경향'이란?</h3>
<ul>
  <li>
    CPU가 실행하려는 프로그램은 보통 관련 데이터들끼리 <strong>한데 모여</strong> 있다.
  </li>
  <li>
    결과적으로 접근한 메모리 공간에 데이터가 모여있기 때문에 해당 공간 근처를 다시 접근하는 경향이 있고 이를 <strong>공간 지역성(spatial locality)</strong>이라고 한다.
  </li>
</ul>