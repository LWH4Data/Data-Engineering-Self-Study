<h1>1. 심층 강화학습이란 무엇인가?</h1>
<ul>
  <li>
    <strong>심층 강화학습(deep reinforcedment learning, DRL)</strong>은 <strong>시행착오</strong>를 통해 얻은 반응을 학습한다.
  </li>
    <ul>
      <li>
        반응은 <strong>순차적</strong>이면서 <strong>평가가 가능</strong>하고 강력한 <strong>비선형 함수 근사(non-linear function approximation)</strong>를 통해 샘플링해서 얻는다.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 심층 강화학습: 인공지능에 대한 머신러닝 접근법</h2>
<ul>
  <li>
    <strong>머신러닝</strong>은 데이터로부터 학습을 통해 <strong>지능이 요구되는 문제를 해결</strong>할 수 있는 컴퓨터 프로그램과 관련된 인공지능 영역이다.
  </li>
    <ul>
      <li>
        <strong>지도학습(supervised learning, SL)</strong>
      </li>
        <ul>
          <li>
            <strong>라벨</strong>이 있는 데이터로 학습한다.
          </li>
          <li>
            <strong>인간</strong>이 어떤 데이터를 수집하고 라벨을 어떻게 설정할지 결정한다.
          </li>
          <li>
            지도학습의 목표는 <strong>일반화</strong>이다.
          </li>
        </ul>
      <li>
        <strong>비지도학습(unsupervised learning, UL)</strong>
      </li>
        <ul>
          <li>
            <strong>라벨이 없는 데이터</strong>로 학습한다.
          </li>
          <li>
            데이터를 수집하는 과정은 인간이 하지만, <strong>라벨을 부여하지는 않는다</strong>.
          </li>
          <li>
            비지도학습의 목표는 <strong>압축</strong>이다.
          </li>
        </ul>
      <li>
        <strong>강화학습(reinforced learning, RL)</strong>
      </li>
        <ul>
          <li>
            <strong>시행착오</strong>를 통해 학습한다.
          </li>
          <li>
            데이터 수집과 라벨링 <strong>모두 필요 없다</strong>.
          </li>
          <li>
            강화학습의 목표는 <strong>행동하기</strong>이다.
          </li>
        </ul>
    </ul>
  <li>
    <strong>딥러닝(depp learning, DL)</strong>
  </li>
    <ul>
      <li>
        보통 <strong>신경망</strong>이라 표현되는 여러 층으로 구성된 <strong>비선형 함수 근사법</strong>을 사용한다.
      </li>
      <li>
        딥러닝은 지도학습이나 비지도학습 그리고 강화학습을 가리지 않고 머신러닝 문제를 해결하는데 <strong>신경망</strong>을 사용하는 <strong>기술과 방법론의 집합</strong>으로 볼 수 있다.
      </li>
    </ul>
  <li>
    <strong>심층 강화학습</strong>은 단순히 강화학습 문제를 해결하는데 <strong>딥러닝을 사용</strong>한 것을 의미한다. 즉, 문제에 대한 <strong>접근법 중 하나</strong>이다.
  </li>
  <li>
    보통 강화학습을 칭할 때에는 심층 강화학습도 포함된다.
  </li>
</ul>

<br>

<h2>1-2. 컴퓨터 프로그램을 만드는 심층 강화학습</h2>
<ul>
  <li>
    심층 강화학습은 불확실에 놓여있는 <strong>복잡하고 연속적인 의사 결정</strong>이 필요한 문제를 다루며 <strong>다양한 분야</strong>에서 관심을 갖는 주제이다.
  </li>
    <ul>
      <li>
        <strong>제어 이론(control theory, CT)</strong>은 복잡하지만 알려진 시스템 내부를 제어하는 방법에 대해 연구한다.
      </li>
      <li>
        <strong>동작 연구(operations research, OR)</strong> 불확실성에 놓인 의사 결정에 대해 연구한다.
      </li>
      <li>
        <strong>심리학</strong> 또한 어떻게 보면 불확실성에 놓인 복잡하면서 연속적인 인간 해동에 대해 연구한다.
      </li>
    </ul>
  <li>
    심층 강화학습에서는 이와 같은 각 분야의 컴퓨터 프로그램을 에이전트(agent)라 한다.
  </li>
    <ul>
      <li>
        GPT의 에이전트와 환경을 관찰하고, 행동을 선택하고, 목표를 향해 움직이는 것은 동일하지만 <strong>GPT</strong>는 <strong>LLM 기반</strong>인 반면 <strong>DRL</strong>은 <strong>행동 최적화 기반</strong>이다.
      </li>
    </ul>
  <li>
    에이전트는 의사를 결정하는 <strong>객체 자체</strong>로 로봇의 팔이 아닌 로봇의 팔이 움직이는 의사결정을 좌우하는 <strong>코드</strong>가 에이전트와 연관된다.
  </li>
</ul>

<br>

<h2>1-3. 지능이 요구되는 문제를 해결하는 심층 강화학습 에이전트</h2>
<ul>
  <li>
    에이전트에 반대되는 개념은 <strong>환경(environment)</strong>이다. 즉, 에이전트가 <strong>제어할 수 없는 모든 것들</strong>을 의미한다.
  </li>
    <ul>
      <li>
        의사를 결정하는 객체인 에이전트는 딱 하나의 규칙인 <strong>의사를 결정하는 것</strong>만 갖고 있으며 결정 이후에 나오는 모든 것은 환경 속에 포함된다.
      </li>
    </ul>
  <li>
    환경은 문제와 연관된 <strong>변수들의 집합</strong>으로 표현할 수 있다.
  </li>
    <ul>
      <li>
        <strong>변수들의 집합</strong>과 변수들이 갖을 수 있는 <strong>속성</strong>은 <strong>상태 영역(state space)</strong>로 표현된다.
      </li>
    </ul>
  <li>
    종종 에이전트는 실제 환경에 놓여진 모든 상태에 대해서 접근할 수 없으며 이때 에이전트가 <strong>관찰할 수 있는 상태의 일부</strong>를 <strong>관찰(observation)</strong>이라 한다.
  </li>
    <ul>
      <li>
        에이전트들은 각 요소들에 상태에 대해서는 알 수 없지만, 에이전트가 인지한 관찰은 <strong>상태에서 도출</strong>된다.
      </li>
      <li>
        예를 들어 10cm 거리에 물체가 있다면 10cm임은 인지할 수 없지만 물체가 대략 그 정도 떨어져 있다는 것은 확인이 가능하다.
      </li>
    </ul>
  <li>
    각 상태에서 환경은 에이전트가 취할 수 있는 가능한 행동을 만들고, 에이전트는 행동들을 통제하여 환경에 영향을 준다. 이와 같은 <strong>에이전트와 환경 사이의 관계</strong>를 정의한 함수를 <strong>전이 함수(trasition function)</strong>라고 부른다.
  </li>
    <ul>
      <li>
        <strong>환경</strong>은 행동에 대한 반응으로 <strong>보상 신호</strong>를 제공할 수 있다. 보상 신호와 관련된 함수를 <strong>보상 함수(reward function)</strong>라고 한다.
      </li>
    </ul>
  <li>
    전이 함수와 보상 함수를 통틀어 환경의 <strong>모델(model)</strong>이라 표현할 수도 있다.
  </li>
  <li>
    <strong>요약</strong>: 관찰 → 전이 함수에 따라 행동 → 환경의 변화 → 보상 함수에 따라 보상 → 반복...
  </li>
  <li>
    <strong>에이전트의 세 단계 과정</strong>
  </li>
    <ul>
      <li>
        <strong>정책</strong>: <strong>관찰과 행동 사이의 관계</strong>를 표현한 것을 학습하도록 설계.
      </li>
      <li>
        <strong>모델</strong>: <strong>환경에 내재된 관계들</strong>을 학습하도록 설계
      </li>
      <li>
        <strong>가치 함수(value function)</strong>: <strong>보상과 행동 사이의 관계</strong>를 평가한 함수를 학습.
      </li>
    </ul>
</ul>

<br>

<h2>1-4. 시행착오를 통한 학습으로 행동을 개선할 수 있는 심층 강화학습 에이전트</h2>
<ul>
  <li>
    
  </li>
</ul>