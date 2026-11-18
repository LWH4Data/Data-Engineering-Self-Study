<h1>1. 안정성을 위한 기술</h1>
<ul>
  <li>
    안정성을 수치로 표현하는 <strong>가용성</strong>, 안정성을 높이기 위한 방법으로 물리적 장비나 프로그램 등을 여러 개 두는 기술인 <strong>이중화</strong>와 <strong>다중화</strong>, 트래픽을 고르게 분산하는 기술인 <strong>로드 밸런싱</strong>에 대해 배운다.
  </li>
</ul>

<br>

<h2>1-1. 가용성</h2>
<ul>
  <li>
    안정성은 특정 기능을 <strong>언제든 균일</strong>한 성능으로 수행할 수 있는 특성으로 정의할 수 있다.
  </li>
  <li>
    안정성의 정도를 나타내는 용어로 <strong>가용성(availability)</strong>과 <strong>고가용성(High Availability)</strong>라는 용어가 있다.
  </li>
    <ul>
      <li>
        가용성이란 컴퓨터 시스템이 특정 기능을 <strong>실제로 수행할 수 있는 시간의 비율</strong>을 의미한다.
      </li>
      <li>
        식으로 정리하면 가용성이란 <strong>'업타입 / (업타임 + 다운타임)'</strong>으로 나타낼 수 있다.
      </li>
        <ul>
          <li>
            업타임(uptime)은 정상적인 사용 시간을, 다운타임(downtime)은 정상적인 사용이 불가능한 시간을 나타낸다.
          </li>
        </ul>
      <li>
        가용성이 큰 경우 전체 사용 시간 중에서 대부분을 사용할 수 있음을 의미하며 이를 고가용성이라 한다. High Availability 혹은 HA라고도 한다.
      </li>
      <li>
        안정적이라고 평가받는 시스템은 <strong>99.999% 이상</strong>을 목표로하며 9가 다섯 개라는 의미에서 파이브 나인스라고도 한다.
      </li>
    </ul>
  <li>
    가용성을 높이기 위해서는 다운타임을 낮추어야하며 여기에는 다양한 방법이 있다.
  </li>
    <ul>
      <li>
        핵심은 문제가 발생하지 않도록 하는 것이 아니라 <strong>문제가 발생하더라도 계속 기능</strong>할 수 있도록 설계하는 것이며 이를 <strong>결함 감내(fault tolerance)</strong>라 한다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 이중화</h2>
<ul>
  <li>
    <strong>이중화</strong>는 가용성을 높이기 위한 가장 기본적이고 대표적인 방법으로 쉽게 말해 <strong>백업</strong>을 마련하는 방법을 의미한다.
  </li>
</ul>