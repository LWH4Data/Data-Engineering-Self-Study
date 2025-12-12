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
    에이전트와 환경 사이의 상호 반응은 <strong>몇 단계</strong> 동안 수행된다. 이때 각 단계를 <strong>타임 스텝(time step)</strong>이라 한다.
  </li>
    <ul>
      <li>
        매 스템마다 얻을 수 있는 상태와 행동, 보상 그리고 새로운 상태를 <strong>경험</strong>이라 부른다.
      </li>
      <li>
        모든 경험은 <strong>학습이나 성능을 개선</strong>할 여지를 부여한다.
      </li>
    </ul>
  <li>
    에이전트가 해결하고자 하는 업부가 자연적으로 끝나는 업무일 경우 이를 <strong>에피소드형 업무(episodic task)</strong>라하고, 자연적으로 끝나지 않는 경우 이를 <strong>연속형 업무(continuing task)</strong>라 한다.
  </li>
    <ul>
      <li>
        에피소드형 작업에서 처음부터 끝까지의 연속적인 스텝들을 <strong>에피소드(episode)</strong>라 한다.
      </li>
      <li>
        보통 에이전트가 무제를 해결하는 방법을 학습할 때, 여러 스탭과 에피소드를 필요로 한다.
      </li>
    </ul>
</ul>

<br>

<h2>1-5. 순차적인 피드백으로부터 학습하는 심층 강화학습 에이전트</h2>
<ul>
  <li>
    문제에 시간적 개념이 들어가 있고, 행동에도 지연된 속성이 있는 등 <strong>시간</strong>으로 인해 보상에 대한 가치를 부여하기 어려운 문제를 <strong>시간적 가치 할당 문제(temporal credit assignment)</strong>라 한다.
  </li>
  <li>
    3 장에서 이와 관련된 문제를 다룬다.
  </li>
</ul>

<br>

<h2>1-6. 평가 가능한 피드백으로부터 학습하는 심층 강화학습 에이전트</h2>
<ul>
  <li>
    에이전트는 <strong>평가 가능한 피드백(evaluative feedback)</strong>으로부터 학습할 수 있어야하며, 이때 평가 가능한 피드백을 하기 위해서는 <strong>탐험(exploration)</strong>이 필요하다.
  </li>
    <ul>
      <li>
        에이전트는 <strong>현재 가지고 있는 정보</strong>에서 얻을 수 있는 가장 좋은 것과 <strong>정보를 새로 얻는 것</strong> 같의 균형을 맞출 수 있어야 하며 이를 <strong>탐험과 착취 간의 트레이드오프(exploration versus exploitation trade-off)</strong>라 한다.
      </li>
    </ul>
  <li>
    이와 관련해서는 4 장에서 자세히 다룬다.
  </li>
</ul>

<br>

<h2>1-7. 샘플링된 피드백으로부터 학습하는 심층 강화학습 에이전트</h2>
<ul>
  <li>
    에이전트가 받는 보상은 샘플 정도이며, 상태와 행동 공간의 차원이 크기에 약한 피드백으로는 학습이 매우 어려우며 따라서 <strong>샘플링된 피드백</strong>으로 학습하고 일반화할 수 있어야 한다.
  </li>
  <li>
    각 가치에 근사화 하도록 한 에이전트들에는 다음이 있다.
  </li>  
    <ul>
      <li>
        <strong>정책 기반(policy-based) 에이전트</strong>: 정책을 근사화하도록 설계.
      </li>
      <li>
        <strong>가치 기반(value-based) 에이전트</strong>: 가치 함수를 근사하도록 설계
      </li>
      <li>
        <strong>모델 기반(model-based) 에이전트</strong>: 모델이 근사하도록 설계
      </li>
      <li>
        <strong>액터-크리틱(actor-critic) 에이전트</strong>: <strong>정책</strong>과 <strong>함수</strong> 둘 다 근사화하도록 설계.
      </li>
    </ul>
</ul>

<br>

<h2>1-8. 강력한 비선형 함수 근사화 기법을 사용하는 심층 강화학습 에이전트</h2>
<ul>
  <li>
    에이전트에는 decision tree와 support vector machine 등 다양한 머신러닝 기법을 통해 근사화할 수 있지만 도서에서는 <strong>신경망</strong>만을 사용한다.
  </li>
  <li>
    인공 신경망(artificial neural networks, ANN)이란 여러 계층의 비선형 함수 근사기를 의미한다.
  </li>
  <li>
    마지막으로 다시 한 번 심층 강화학습 에이전트는 <strong>순차적</strong>이면서 <strong>평가 가능</strong>하면서 동시에 <strong>샘플링된 피드백</strong>으로 학습할 수 있다.
  </li>
</ul>

<br><br>

<h1>2. 심층 강화학습의 과거와 현재 그리고 미래</h1>
<h2>2-1. 현재까지의 인공지능과 심층 강화학습의 역사</h2>
<ul>
  <li>
    튜링 테스트(Turing Test)는 인간 검사자가 일정 시간동안의 Q & A를 통해 상대가 기계인지 사람인지 구분하지 못하는 경우 해당 컴퓨터는 지능이 있는 것으로 간주한다.
  </li>
    <ul>
      <li>
        초보적인 검사지만 연구자가 추구할 수 있는 목표를 제시하여 좀 더 똑똑한 기계를 창조할 여지를 만들었다.
      </li>
    </ul>
  <li>
    존 매카시(John McCarthy)는 1955년 인공지능이라는 용어를 만들고, 1956년 최초의 인공지능 학회를 주도, 1958년 Liso 프로그래밍 언어 개발, 1959 MIT 인공지능 연구소를 설립하는 등 인공지능의 사작과 발전에 큰 기여를 하였다.
  </li>
</ul>

<br>

<h2>2-2. 인공지능의 겨울</h2>
<ul>
  <li>
    수년간 인간과 유사한 기계 지능을 만드는 방법을 제안하였지만 물리적인 한계로 이루어지지 못하며 첫 번째 인공지능의 겨울로 불리는 침체기가 이어졌다.
  </li>
</ul>

<br>

<h2>2-3. 인공지능의 현재 상태</h2>
<ul>
  <li>
    현재는 물리적 자원이 뒷받침되면서 인공지능이 빠르게 발전하고 있다.
  </li>
</ul>

<br>

<h2>2-4. 심층 강화학습의 발전</h2>
<ul>
  <li>
    강화학습 문제에 인공 신경망이 사용되기 시작한 것은 1990년대부터이다.
  </li>
    <ul>
      <li>
        1990년 TD-Gammon: 백개먼 게임을 할 수 있도록 학습.
        <br>→ 2004 앤드류 응(Andrew Ng) 역강화학습(inverse reinforced learning)을 통한 자율 헬리콥터 개발 & 네이트 콜(Nate Kohl)과 피터 스톤(Peter Stone)이 정책-경사법(policy gradient method)이라는 심층 강화학습을 사용해 축구하는 로봇을 선보임.
        <br>→ 2010 강화학습 분야가 딥러닝을 넘어서기 시작.
        <br>→ 2013 ~ 2015 므니흐의 심층 Q 신경망(deep Q-network, DQN) 알고리즘이 아타리(Atari) 게임 규칙을 학습
        <br>→ 2014년 실버(Silver)가 DPG(deterministic policy gradient)를 선보임.
        <br>→ 2015년 릴리크랩(Lillicrap)이 DDPG(deep deterministic policy gradient) 알고리즘 발전.
        <br>→ 2016년 슐만이 TRPO(trust region policy optimization)와 GAE(generalized advantage estimation) 알고리즘 소개 등.
      </li>
    </ul>
</ul>

<br>

<h2>2-5. 주어진 기회들</h2>
<ul>
  <li>
    특이점 등 인공지능의 발전이 빠른 문제에 대해 다루는데 저자는 1750 년 산업혁명으로 부의 분배가 더 수월해졌음을 이야기하며 인공지능의 발전도 비슷한 효과를 줄 것을 기대한다.
  </li>
</ul>

<br><br>

<h1>3. 심층 강화학습의 적절성</h1>
<h2>3-1. 심층 강하학습의 장점과 단점</h2>
<ul>
  <li>
    심층 강화학습은 실패를 반복해야하며 탐색 방법을 고려하는 등 <strong>비용이 높다</strong>.
  </li>
    <ul>
      <li>
        위와 같은 문제에 <strong>전이학습(transfer learning)</strong>을 활용하면 학습과정에서 얻은 지식을 새로운 주제에 적용할 수 있어 비교적 가볍다.
      </li>
      <li>
        인간 또한 새로운 행동을 학습할 때마다 저수준 행동을 재학습할 필요가 없으며 이런 <strong>계층적 강화학습(hierarchical reinforced learning)</strong>을 심층 강화학습 에이전트에 반영한다.
      </li>
    </ul>
</ul>

<br>

<h2>3-2. 심층 강화학습의 강점</h2>
<ul>
  <li>
    심층 강화학습은 <strong>특정 업무를 숙지</strong>하는 학습으로 일반화를 하는 것이 목표인 지도학습과는 다르며 <strong>정확하고 잘 정의된 동작</strong>에 뛰어나다.
  </li>
  <li>
    단, 심층 강화학습도 일반화 기법을 사용할 때가 있는데 원래의 센서 데이터에서 <strong>간단한 기술을 학습</strong>할 때가 해당한다.
  </li>
</ul>

<br>

<h2>3-3. 심층 강화학습의 약점</h2>
<ul>
  <li>
    인간은 적은 상호 교감으로 학습이 가능하지만, 에이전트는 정책을 학습하도록 수백만의 샘플이 필요하기에 <strong>샘플에 대한 효율성(sample  efficiency)</strong>은 중요 개선사항이다.
  </li>
  <li>
    보상이란 관점에 따라 달라지는 경우가 있기에 <strong>명확한 보상 함수를 설계</strong>하기 어렵다.
  </li>
    <ul>
      <li>
        저자는 <strong>본질적 동기(intrinsic motivation)</strong>이라는 연구 주제를 언급하는데 에이전트가 호기심을 통해 <strong>새로운 행도을 탐색</strong>하도록 한다.
      </li>
      <li>
        이는 드문드문 정의된 보상(sparse reward)이 있는 환경에서도 개선된 학습 성능을 보여준다.
      </li>
    </ul>
</ul>