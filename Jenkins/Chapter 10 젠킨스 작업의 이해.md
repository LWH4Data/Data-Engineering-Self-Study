<h1>1. 젠킨스의 작업</h1>
<ul>
  <li>
    젠킨스의 <strong>작업</strong>이란? 젠킨스가 <strong>무엇을 언제</strong> 해야하는지를 지시하는 일련의 <strong>명령 집합</strong>을 의미한다.
  </li>
</ul>

<br>

<h2>1-1. 작업의 세 가지 구성 요소</h2>
<h3>1-1-1. 트리거 (trigger)</h3>
<ul>
  <li>
    작업을 수행하는 시점을 의미한다.
  </li>
  <li>
    작업에서 수행할 태스크(task)가 <strong>언제 시작</strong>될지 젠킨스에 지시한다.
  </li>
</ul>

<h3>1-1-2. 빌드 스탭 (build step)</h3>
<ul>
  <li>
    작업을 구성하는 단계를 의미한다.
  </li>
  <li>
    사용자는 태스크를 <strong>단계별(step)</strong>로 구성하여 작업을 생성한다.
  </li>
</ul>

<h3>1-1-3. 포스트-빌드 액션 (post-build action)</h3>
<ul>
  <li>
    태스크가 완룐된 후 수행할 명령이다.
  </li>
  <li>
    태스크 <strong>실행이 완료된 후</strong> 젠킨스가 수행할 작업을 수행한다. (e.g. 작업 결과 알림, 코드 복사, etc.).
  </li>
</ul>

<br><br>

<h1>2. 젠킨스의 빌드</h1>
<ul>
  <li>
    젠킨스의 빌드는 젠킨스 작업의 <strong>특정 실행 버전</strong>을 의미한다.
  </li>
  <li>
    젠킨스는 작업을 여러 번 수행할 수 있는데 매 작업마다 <strong>고유한 빌드 번호</strong>가 부여된다. 
  </li>
  <li>
    작업 실행 중의 콘솔 로그 등 특정 실행 버전과 관련된 모든 세부 정보는 <strong>고유한 빌드 번호로 저장</strong>된다. 
  </li>
</ul>

<br><br>

<h1>3. 프리스타일 작업</h1>
<ul>
  <li>
    프리스타일 작업(freestyle Job)은 일반적인 형태의 빌드 작업(or 태스크)를 의미한다.
  </li>
  <li>
    태스크의 실행, 애플리케이션 빌드 및 패키징, 보고서 전송 등이 해당한다.
  </li>
</ul>

<br><br>

<h3>Chapter 10 까지의 과정은 Jenkins에 대한 소개로 간단히 정리한다. Chatper 11부터 실습을 하며 Jenkins를 활용해본다.</h3>