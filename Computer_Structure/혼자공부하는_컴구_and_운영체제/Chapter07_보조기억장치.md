<h1>1. 다양한 보조기억장치</h1>
<ul>
  <li>
    대표중적인 보조기억장치로는 <strong>하드 디스크</strong>와 <strong>플래시 메모리</strong>가 있다.
  </li>
    <ul>
      <li>
        플래시 메모리에는 우리가 흔히 사용하는 USB 메모리, SD 카드, SSD와 같은 저장 장치가 있다.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 하드 디스크</h2>
<ul>
  <li>
    <strong>하드 디스크(HDD; Hard Disk Drive)</strong>는 자기적인 방식으로 데이터를 저장하는 보조기억장치이다. 이 때문에 하드 디스크를 <strong>자기 디스크(magnetic disk)의 일종</strong>으로 지칭하기도 한다.
  </li>
    <ul>
      <li>
        익히 알고 있는 CD나 옛날 음향 장치인 LP도 하드 디스크와 비슷하게 동작한다.
      </li>
    </ul>
  <li>
    하드 디스크에서 실질적으로 데이터가 저장되는 곳은 동그란 원판 모형이며 이를 <strong>플래터(platter)</strong>라고 한다.
  </li>
    <ul>
      <li>
        플래터는 자기 물질로 덮혀 있어 수많은 <strong>N극과 S극을 저장</strong>한다
      </li>
      <li>
        N극과 S극은 <strong>0과 1의 역할</strong>을 수행한다.
      </li>
    </ul>
  <li>
    플래터를 회전시키는 구성 요소를 <strong>스핀들(spindle)</strong>이라고 한다.
  </li>
  <li>
    스핀들이 플래터를 돌리는 속도는 분당 회전수를 나타내는 <strong>RPM(Revolution Per Minute)</strong>이라는 단위로 표현한다.
  </li>
    <ul>
      <li>
        RPM이 15,000이라면 하드 디스크는 1분에 15,000바퀴를 회전하는 하드 디스크이다.
      </li>
    </ul>
  <li>
    플래터를 대상으로 데이터를 읽고 쓰는 구성 요소는 <strong>헤드(head)</strong>이다.
  </li>
    <ul>
      <li>
        헤드는 플래터 위에서 마세하게 떠 있는 채로 <strong>데이터를 읽고 쓰는</strong>, 마치 <strong>바늘</strong>같이 생긴 부품이다.
      </li>
      <li>
        헤드는 헤드를 원하는 위치로 이동시키는 <strong>디스크 암(disk arm)</strong>에 부착되어 있다.
      </li>
    </ul>
  <li>
    CD나 LP에 비해 하드 디스크는 훨씬 더 많은 양의 데이터를 저장해야하기 때문에 일반적으로 <strong>여러 겹의 플래터</strong>로 이루어져 있으며 <strong>플래터 양면</strong>을 모두 사용할 수 있다.
  </li>
    <ul>
      <li>
        양면 플래터의 경우 위아래로 플래터당 <strong>두 개의 헤드</strong>가 사용되며 일반적으로 모든 헤드는 디스크 앞에 부착되어 <strong>다같이 이동</strong>한다.
      </li>
    </ul>
  <li>
    플래터는 <strong>트랙(track)</strong>과 <strong>섹터(sector)</strong>라는 단위로 데이터를 저장한다.
  </li>
    <ul>
      <li>
        플래터를 여러 <strong>동심원</strong>으로 나누었을 때 <strong>그중 하나의 원</strong>을 <strong>트랙</strong>이라 부른다.
      </li>
      <li>
        트랙은 다시 피자 조각처럼 여러 조각으로 나뉘어지는데 이 <strong>각 조각을 섹터</strong>라고 부른다.
      </li>
        <ul>
          <li>
            하나 이상의 섹터를 묶어서 <strong>블록(block)</strong>이라고 표현하기도 한다.
          </li>
          <li>
            섹터는 하드 디스크의 <strong>가장 작은 전송 단위</strong>이다.
          </li>
            <ul>
              <li>
                하나의 섹터는 일반적으로 512바이트 정도의 크기를 가지고 있지만, 정확한 크기는 하드 디스크에 따라 차이가 있다.
              </li>
            </ul>
        </ul>
    </ul>
  <li>
    여러 겹의 플래터 상에서 <strong>같은 트랙이 위치한 곳</strong>을 모아 연결한 논리적 단위를 <strong>실린더(cylinder)</strong>라고 부른다.
  </li>
    <ul>
      <li>
        한 플래터를 동심원으로 나눈 공간은 트랙, 같은 트랙끼리 연결한 원통 모양의 공간은 실린더이다.
      </li>
      <li>
        <strong>연속된 정보</strong>는 보통 한 실린더에 기록된다.
      </li>
        <ul>
          <li>
            네 개의 섹터에 걸쳐 데이터를 저장할 때에는 첫 번째 플래터의 윗, 뒷면과 두 번째 플래터의 윗, 뒷면에 저장한다.
          </li>
          <li>
            연속된 정보를 하나의 실린더에 기록하는 이유는 <strong>디스크 암을 움직이지 않고도 바로 데이터에 접근</strong>할 수 있기 때문이다.
          </li>
        </ul>
    </ul>
  <li>
    하드 디스크가 저장된 데이터에 접근하는 시간은 크게 <strong>탐색 시간</strong>, <strong>회전 지연</strong>, <strong>전송 시간</strong>으로 나뉜다.
  </li>
    <ul>
      <li>
        <strong>탐색 시간(seek time)</strong>은 접근하려는 데이터가 저장된 트랙까지 <strong>헤드를 이동시키는 시간</strong>을 의미한다.
      </li>
      <li>
        <strong>회전 지연(rotational latency)</strong>은 헤드가 있는 곳으로 <strong>플래터를 회전시키는 시간</strong>을 의미한다.
      </li>
      <li>
        <strong>전송 시간(transfer time)</strong>은 하드 디스크와 컴퓨터 간에 <strong>데이터를 전송하는 시간</strong>을 의미한다.
      </li>
    </ul>
  <li>
    탐색 시간과 회전 지연을 단축 시키기 위해서는 플래터를 빨리 돌려 <strong>RPM</strong>을 높이는 것도 중요하지만, <strong>참조 지역성</strong>을 활용해 데이터가 플래터 혹은 헤드를 조금만 옮겨 데이터에 접근할 수 있는 것도 중요하다.
  </li>
</ul>

<h4>다중 헤드 디스크와 고정 헤드 디스크</h4>
<ul>
  <li>
    플래터의 <strong>한 면당 헤드가 하나씩</strong> 달려 있는 하드 디스크를 <strong>단일 헤드 디스크(single-head disk)</strong>라고 한다.
  </li>
    <ul>
      <li>
        헤드를 데이터가 있는 곳까지 움직여야하기 때문에 <strong>이동 헤드 디스크(movable-head disk)</strong>라고 부른다.
      </li>
    </ul>
  <li>
    헤드가 <strong>트랙별로 여러 개</strong>가 달려 있는 디스크는 <strong>다중 헤드 디스크(multiple-head disk)</strong>라고 부른다.
  </li>
    <ul>
      <li>
        다중 하드 디스크는 트랙마다 헤드가 있기 때문에 탐색 시간이 들지 않는다. 즉 <strong>탐색 시간이 0</strong>이다.
      </li>
      <li>
        헤드를 움직일 필요가 없기 때문에 <strong>고정 헤드 디스크(fixed-head disk)</strong>라고도 부른다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 플래시 메모리</h2>
<ul>
  <li>
    회전을 활용하는 하드 디스크는 많이 사용하는 보조기억장치이지만, <strong>플래시 메모리(flash memory)</strong> 기반의 보조기억장치 또한 많이 사용한다.
  </li>
  <li>
    플래시 메모리는 전기적으로 데이터를 읽고 쓸 수 있는 <strong>반도체 기반의 저장 장치</strong>이다.
  </li>
    <ul>
      <li>
        플래시 메모리는 보조기억장치 범주에만 속한다기보다 다양한 곳에서 널리 사용하는 장치로 보는 것이 적합하다.
      </li>
      <li>
        주기억장치 중 하나인 ROM에도 사용되고, 우리가 일상적으로 접하는 거의 모든 전자 제품 안에 플래시 메모리가 내장되어 있다 볼 수 있다.
      </li>
    </ul>
  <li>
    플래시 메모리에는 <strong>셀(cell)</strong>이라는 단위가 있다.
  </li>
    <ul>
      <li>
        셀이란 플래시 메모리에서 데이터를 저장하는 <strong>가장 작은 단위</strong>이다.
      </li>
      <li>
        셀이 모이고 모여 MB, GB, TB 용량을 갖는 저장 장치가 된다.
      </li>
    </ul>
  <li>
    하나의 셀에 <strong>몇 비트를 저장</strong>할 수 있느냐에 따라 플래시 메모리의 종류가 나뉜다.
  </li>
    <ul>
      <li>
        한 셀에 1비트를 저장할 수 있는 메모리를 <strong>SLC(Single Level Cell)</strong>, 2비트는 <strong>MLC(Multiple Level Cell)</strong>, 3비트를 저장할 수 있는 경우는 <strong>TLC(Triple-Level Cell)</strong>타입이라 한다.
      </li>
    </ul>
  <li>
    저장 비트에 따른 차이(SLC, MLC, TLC)가 큰 차이가 없어 보여도 플래시 메모리의 <strong>수명, 속도, 가격</strong>에 큰 영향을 끼친다.
  </li>
    <ul>
      <li>
        한 셀에 4비트를 저장할 수 있는 QLC 타입도 존재한다.
      </li>
    </ul>
</ul>

<h4>두 종류의 플래시 메모리</h4>
<ul>
  <li>
    플래시 메모리에는 크게 <strong>NAND 플래시 메모리</strong>와 <strong>NOR 플래시 메모리</strong>가 있다.
  </li>
    <ul>
      <li>
        NADN 플래시 메모리는 <strong>NAND 연산(NAND 게이트)</strong>을 수행하는 회로 기반으로 만들어진 메모리이다.
      </li>
      <li>
        NOR 플래시 메모리는 <strong>NOR 연산을 수행하는 회로(NOR 게이트)</strong>를 기반으로 만들어진 메모리를 의미한다.
      </li>
    </ul>
  <li>
    둘 중 <strong>대용량 저장 장치</strong>로 많이 사용되는 플래시 메모리는 <strong>NAND 플래시 메모리</strong>이다.
  </li>
  <li>
    이번 절에서 설명하는 플래시 메모리는 <strong>NAND 플래시 메모리</strong>이다.
  </li>
</ul>

<h4>플래시 메모리도 수명이 있나요?</h4>
<ul>
  <li>
    플래시 메모리를 포함해 하드 디스크와 USB 메모리, SSD, SD 카드 모두 수명이 존재한다.
  </li>
  <li>
    또한 수명이 다하면 더 이상 저장 장치로써 사용이 불가능하다.
  </li> 
</ul>

<h3>1-2-1. SLC 타입</h3>
<ul>
  <li>
    SLC는 1비트 단위이기 때문에 한 셀로 <strong>두 개의 정보</strong>를 표현할 수 있다.
  </li>
    <ul>
      <li>
        SLC 타입은 MLC나 TLC 타입에 비해 비트의 <strong>빠른 입출력</strong>이 가능하다.
      </li>
      <li>
        빠른만큼 가격이 비싸다는 단점이 있다.
      </li>
    </ul>
  <li>
    보통 기업에서는 데이터를 <strong>읽고 쓰기가 매우 많이 반복</strong>되며 <strong>고성능의 빠른 저장 장치</strong>가 필요한 경우에 SLC 타입을 사용한다.
  </li>
</ul>

<h3>1-2-2. MLC 타입</h3>
<ul>
  <li>
    MLC 타입은 한 셀에 두 개의 비트를 포함하기 때문에 한 셀로 <strong>네 개의 정보</strong>를 표현할 수 있다.
  </li>
  <li>
    SLC보다 더 많은 정보를 저장하기 때문에 <strong>대용화</strong>하기 유리하고 비교적 <strong>가격이 저렴</strong>하다.
  </li>
  <li>
    시중에서 사용되는 많은 플래시 메모리 저장 장치들은 MLC(혹은 TLC)로 만들어진다.
  </li>
</ul>

<h3>1-2-3. TLC 타입</h3>
<ul>
  <li>
    한 셀당 3비트씩 저장할 수 있어 한 셀로 <strong>여덟 개의 정보</strong>를 표현할 수 있다.
  </li>
    <ul>
      <li>
        표현할 수 있는 정보가 많아 대용량화 하기 유리하다는 장점이 있다.
      </li>
      <li>
        일반적으로 SLC나 MLC 타입보다 수명과 <strong>속도가 떨어지지만 용량 대비 가격도 저렴</strong>하다.
      </li>
    </ul>
  <li>
    수명, 가격, 성능이 제각기 다르기 때문에 사용 목적에 따라 적합한 메모리를 선택하는 것이 중요하다.
  </li>
  <li>
    셀들이 모여 만들어진 단위를 <strong>페이지(page)</strong>, 페이지가 모여 만들어진 단위를 <strong>블록(block)</strong>, 블록이 모여 만들어진 단위를 <strong>플레인(plane)</strong>, 플레인이 모여 <strong>다이(die)</strong>가 된다.
  </li>
  <li>
    플래시 메모리에서 읽기와 쓰기는 페이지 단위로 이루어진다. 반면 삭제는 블록 단위로 이루어진다. 이렇게 <strong>읽기/쓰기 단위와 삭제 단위가 다르다는 것</strong>은 플래시 메모리의 가장 큰 특징 중 하나이다.
  </li>
  <li>
    페이지는 <strong>Free, Valid, 그리고 Invalid 세 개의 상태</strong>를 가질 수 있다.
  </li>
    <ul>
      <li>
        <strong>Free 상태</strong>는 어떠한 데이터도 저장하고 있지 않아 <strong>새로운 데이터를 저장할 수 있는 상태</strong>를 의미한다.
      </li>
      <li>
        <strong>Valid 상태</strong>는 이미 <strong>유효한 데이터</strong>를 저장하고 있는 상태를 의미한다.
      </li>
      <li>
        <strong>Invalid 상태</strong>는 쓰레기값이라 부르는 <strong>유효하지 않은 데이터</strong>를 저장하고 있는 상태를 의미한다.
      </li>
    </ul>
  <li>
    데이터 읽기/쓰기는 셀 단위, 삭제는 블록 단위로 이루어지기에 예를 들어 수정을 할 때에는 기존의 데이터가 <strong>쓸모없이 자리를 차지</strong>하는 문제가 발생한다.
  </li>
    <ul>
      <li>
        이런 문제를 보완하기 위해 최근 SSD를 비롯한 플래시 메모리는 <strong>가비지 컬렉션(garbage collection)</strong> 기능을 제공한다.
      </li>
    </ul>
  <li>
    가비지 컬레션은 유효한 페이지들만 <strong>새로운 블록으로 복사</strong>한 뒤, <strong>기존의 블록을 삭제</strong>하는 기능이다.
  </li>
</ul>

<br><br>

<h1>2. RAID의 정의와 종류</h1>
<h2>2-1. RAID의 정의</h2>
<ul>
  <li>
    데이터가 쏟아지는 환경에서 데이터를 하드 디스크에 저장하면 된다 생각할 수 있지만 앞서 다루었듯이 하드 디스크와 같은 보조기억장치는 <strong>수명</strong>이 있기 때문에 불가능하다.
  </li>
  <li>
    이때 <strong>RAID(Redundant Array of Independent Disks)</strong>를 활용한다.
  </li>
    <ul>
      <li>
        주로 <strong>하드 디스크와 SSD</strong>에 사용하는 기술이며 <strong>데이터의 안정성</strong> 혹은 <strong>높은 성능</strong>을 위해 <strong>여러 개의 물리적 보조기억장치</strong>를 마치 하나의 논리적 보조기억장치처럼 사용하는 기술이다.
      </li>
    </ul>
</ul>

<br>

<h2>2-2. RAID의 종류</h2>
<ul>
  <li>
    RAID 구성 방법을 <strong>RAID 레벨</strong>이라 표현한다. 대표적으로는 RAID 0, RAID 1, RAID 2, RAID 3, RAID 4, RAID 5, RAID 6이 있다.
  </li>
    <ul>
      <li>
        파생된 방법들로는 RAID 10, RAID 50 등이 있다.
      </li>
    </ul>
</ul>

<h3>2-2-1. RAID 0</h3>
<ul>
  <li>
    RAID 0은 여러 개의 보조기억장치에 데이터를 <strong>단순히 나누어 저장</strong>하는 구성 방식이다.
  </li>
  <li>
    저장되는 데이터는 각 하드 디스크를 <strong>번갈아 가며</strong> 데이터를 저장한다. 즉 저장되는 데이터가 하드 디스크 개수만큼 나뉘어 저장되는 것이다.
  </li>
  <li>
    데이터는 마치 줄무늬처럼 분산되어 저장되는데 이때 저장된 데이터를 <strong>스트라입(stripe)</strong>, 분산하여 저장하는 것을 <strong>스트라이핑(striping)</strong>이라고 한다.
  </li>
    <ul>
      <li>
        이렇게 데이터를 분산하여 저장하면 동시에 데이터를 읽고 쓸 수 있기 때문에 <strong>속도가 빨라진다</strong>.
      </li>
    </ul>
  <li>
    단, RAID 0은 구성된 하드 디스크 중 하나에 문제가 생기면 다른 모든 하드 디스크의 정보를 읽는데 문제가 생길 수 있어 <strong>저장된 정보가 안전하지 못하다</strong>는 문제가 있다.
  </li>
</ul>

<h3>2-2-2. RAID 1</h3>
<ul>
  <li>
    RAID 1은 RAID 0의 단점을 보완하여 복사본을 만드는 방식으로 <strong>미러링(mirroring)</strong>이라고도 부른다.
  </li>
  <li>
    데이터를 저장하는 것은 RAID 0과 같이 스프라이핑이 적용되지만 데이터를 저장하는 하드 디스크를 다른 하드 디스크에 그대로 복사해 둔다.
  </li>
    <ul>
      <li>
        단, 복사를 하며 쓰기 때문에 <strong>RAID 0보다 느리다</strong>.
      </li>
    </ul>
  <li>
    RAID 1은 미러링을 해두기 때문에 <strong>복구가 매우 간단</strong>하다는 장점이 있다.
  </li>
  <li>
    반면 미러링을 해야하기 때문에 하드 디스크 개수가 한정되었을 때 <strong>사용 가능한 용량이 적어지는 단점</strong>이 존재한다.
  </li>
    <ul>
      <li>
        이는 곧 필요한 하드 디스크의 개수가 많아지고 비용이 증가한다는 단점과 연결된다.
      </li>
    </ul>
</ul>

<h3>2-2-3. RAID 4</h3>
<ul>
  <li>
    RAID 4는 RAID 1처럼 완전한 복사본을 만드는 대신 <strong>오류를 검출</strong>하고 <strong>복구</strong>하기 위한 정보를 저장한 장치를 두는 구성 방식이다.
  </li>
    <ul>
      <li>
        오류를 검출하고 복구하기 위한 정보를 <strong>패리티 비트(parity bit)</strong>라고 한다.
      </li>
    </ul>
  RAID 4는 패리티 비트를 통해 RAID 1보다 적은 하드 디스크로도 데이터를 안전하게 보관할 수 있다.
</ul>

<h4>오류를 검출하는 패리티 비트</h4>
<ul>
  <li>
    원래 패리티 비트는 오류 검출만 가능할 뿐 오류 복구는 불가능하다. 하지만 RAID에서는 패리티 값으로 <strong>오류 수정</strong>도 가능하다.
  </li>
  <li>
    단 두 가지를 기억하면 된다.
  </li>
    <ol>
      <li>
        패리티 비트는 RAID 4에서는 패리티 정보를 저장한 장치로써 <strong>나머지 장치들의 오류를 검출 및 복구</strong>한다.
      </li>
      <li>
        패리티 정보는 본래 오류 검출용 정보지만, RAID에서는 <strong>오류 복구</strong>도 가능하다.
      </li>
    </ol>
</ul>

<h3>2-2-4. RAID 5</h3>
<ul>
  <li>
    RAID 5는 <strong>패리티 정보를 분산하여 저장</strong>하는 방식으로 RAID 4에서 패리티 정보를 저장할 때 발생하는 병목 현상을 해소한다.
  </li>
    <ul>
      <li>
        RAID 4에서는 새로운 데이터가 저장될 때마다 패리티를 저장하는 디스크에도 데이터를 쓰기 때문에 <strong>패리티를 저장하는 장치에 병목 현상</strong>이 발생한다.
      </li>
    </ul>
</ul>

<h3>2-2-5. RAID 6</h3>
<ul>
  <li>
    RAID 6은 RAID 5와 같지만 패러티를 저장할 때 <strong>서로 다른 두 개의 패러티</strong>를 저장하는 방식이다.
  </li>
    <ul>
      <li>
        오류를 검출하고 복구할 수 있는 수단이 두 개가 생긴 것과 같으며 따라서 RAID 4와 RAID 5보다는 안전한 구성이라 볼 수 있다.
      </li>
    </ul>
  <li>
    다만 새로운 정보를 저장할 때마다 함께 저장할 패리티가 두 개이기 때문에 쓰기 속도는 RAID 5보다 느리다.
  </li>
    <ul>
      <li>
        즉 RAID 6은 데이터 저장 속도를 조금 희생한 대신 안전성을 더욱 보장하는 방향을 채택한 것이다.
      </li>
    </ul>
  <li>
    RAID 1과 RAID 0을 결합한 RAID 10, RAID 5와 RAID 0을 결합한 RAID 50 등이 있는데 이렇게 RAID 레발을 혼합하는 방식은<strong>Nested RAID</strong>라고 한다.
  </li>
</ul>