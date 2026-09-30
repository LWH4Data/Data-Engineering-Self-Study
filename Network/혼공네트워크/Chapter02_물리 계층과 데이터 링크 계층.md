<h1>1. 이더넷</h1>
<ul>
  <li>
    물리 계층과 데이터 링크 계층은 <strong>이더넷</strong>이라는 공통된 기술이 사용되기 때문에 서로 밀접하게 연관되어 있다.
  </li>
  <li>
    <strong>이더넷(Ethernet)</strong>은 현대 LAN, 특히 <strong>유선 LAN 환경</strong>에서 가장 대중적으로 사용되는 기술이다.
  </li>
    <ul>
      <li>
        예를 들어 두 대의 컴퓨터가 있다면 서로 정보를 주고받기 위해서는 먼저 <strong>케이블과 같은 통신 매체</strong>가 필요하고 통신 매체를 통해 <strong>정보를 송수신하는 방법</strong>이 정해져 있어야 한다.
      </li>
    </ul>
  <li>
    따라서 이더넷은 통<strong>신 매체의 규격</strong>들과 <strong>송수신되는 프레임의 형태, 프레임을 주고받는 방법 등</strong>이 정의된 네트워크 기술이다.
  </li>
</ul>

<br>

<h2>1-1. 이더넷 표준</h2>
<ul>
  <li>
    오늘날 유선 LAN 환경은 대부분 <strong>이더넷</strong>을 기반으로 구성된다.
  </li>
    <ul>
      <li>
        LAN 환경을 구축했다면 물리 계층과 데이터 링크 계층에서 주고받는 프레임은 십중팔구 이더넷 프레임의 형식을 따를 것이다.
      </li>
    </ul>
  <li>
    이더넷은 국제적으로 표준화가 되었으며 처음 등장한 이후 전기전자공학자협회(IEEE; Institute of Electrical and Electronics Engineers)라는 국제 조직은 관련 기술을 <strong>IEEE 802.3</strong>이라는 이름으로 표준화하였다.
  </li>
    <ul>
      <li>
        IEEE 802.3은 이더넷 관련 다양한 표준들의 모음을 의미한다고 생각할 수 있다.
      </li>
      <li>
        서로 다른 컴퓨터가 각기 다른 제조사의 네트워크 장비를 사용해도 동일한 형식의 프레임을 주고받을 수 있는 것도 이 덕이다.
      </li>
      <li>
        IEEE는 이더넷 작업 그룹(Ethernet working group)의 이름이기도 하며 관련 홈페이지에는 현제도 새로운 표준이 개발되고 있다.
      </li>
    </ul>
  <li>
    이더넷의 표준들은 802.3u 혹은 802.3ab와 같이 <strong>버전을 나타내는 알파벳</strong>으로 표현한다.
  </li>
  <li>
    핵심은 <strong>이더넷 표준</strong>에 따라 지원되는 네트워크 장비, 통신 매체의 전송 속도 등이 달라질 수 있다는 것이다.
  </li>
</ul>

<br>

<h2>1-2. 통신 매체 표기 형태</h2>
<ul>
  <li>
    일반적으로 이더넷 표준 규격에 따라 구현된 통신 매체를 지칭할 때에는 <strong>통신 매체의 속도와 특성</strong>을 한눈에 파악하기 위해 <strong>'전송 속도 BASE-추가특성'</strong>과 같은 형태로 표기한다.
  </li>
     <ul>
       <li>
         예를 들면 1000BASE-sx, 5GBASE-T, 1000BASE-LX 등 이다.
       </li>
     </ul>
  <li>
    <strong>전송 속도(data rate)</strong>는 숫자만 표기되어 있으면 Mbps, 숫자 뒤에 G가 붙으면 Gbps를 의미한다.
  </li>
  <li>
    <strong>BASE</strong>는 베이스밴드(BASEband)의 약자로 변조 타입(modulation type)을 의미한다.
  </li>
    <ul>
      <li>
        변조 타입이란 비트 신호로 변환된 데이터를 <strong>통신 매체로 전송하는 방법</strong>을 의미한다.
      </li>
      <li>
        일반적인 LAN 환경에서는 특별한 경우가 아니라면 대부분 디지털 신호를 송수신하는 베이스밴드 방식을 이용한다.
      </li>
        <ul>
          <li>
            예를 들면 BASE 외에 BROAD로 표기하는 브로드밴드(BROADband), PASS로 표기하는 패스밴드(PASSband)도 있다.
          </li>
        </ul>
    </ul>
  <li>
    <strong>추가 특성(additional distinction)</strong>에는 통신 매체의 특성을 명시한다.
  </li>
    <ul>
      <li>
        예를 들어 10BASE-2, 10BASE-5와 같이 <strong>전송 가능한 최대 거리</strong>가 명시되기도 하고, 데이터가 비트 신호로 변환되는 방식을 의미하는 <strong>물리 계층 인코딩 방식</strong>이 명시되기도 하며, 비트 신호를 옮길 수 있는 전송로 수를 의미하는 <strong>레인 수</strong>가 명시되기도 한다.
      </li>
    </ul>
</ul>