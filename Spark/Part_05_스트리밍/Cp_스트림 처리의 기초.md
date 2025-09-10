<ul>
  <li>
    과거에는 map과 reduce, 그리고 DStream을 활용하였다. 2016년 부터는 DataFrame과 Dataset 코드와 쉽게 통합될 수 있는 신규 스트리밍 API가 <strong>DataFrame을 기반으로 구현</strong>되었으며 <strong>구조적 스트리밍</strong>이라는 이름으로 Spark에 추가 되었다.
  </li>
  <li>
    <strong>구조적 스트리밍</strong>은 DStream의 주요 기능에 대한 <strong>상위 기능</strong>을 제공하며 <strong>코드 생성 기능</strong>과 카탈리스트 옵티마이저를 사용한 <strong>최적화 기법</strong>을 제공한다.
  </li>
</ul>

<br>

<h1>1. 스트림 처리란</h1>
<ul>
  <li>
    <strong>스트림 처리(stream processing)</strong>는 신규 데이터를 <strong>끊임없이 처리</strong>해 결과를 만들어 내는 행위이다.
  </li>
  <li>
    스트림 처리의 <strong>입력 데이터</strong>는 <strong>무한</strong>하며 <strong>시작과 끝을 사전에 정의</strong>하지 않는다.
  </li>
  <li>
    <strong>입력 데이터</strong>는 스트림 처리 시스템에 도작한 일련의 <strong>이벤트</strong>이다.
  </li>
  <li>
    스트리밍 앱은 이벤트 스트림에 <strong>다양한 쿼리를 수행</strong>하고, <strong>다양한 버전의 결과</strong>를 출력하거나 key-value 저장소 같은 외부 sink 시스템에 <strong>최신 데이터를 저장</strong>할 수도 있다.
  </li>
  <li>
    <strong>배치 처리</strong>는 스트림 터리와 유사한 연산용 쿼리를 사용하지만 <strong>결과를 한 번만</strong> 만들어 낸다.
  </li>
  <li>
    스트림 처리와 배치 처리는 달라보이지만 실전에서는 <strong>함께 사용</strong>하기도 한다.
  </li>
    <ul>
      <li>
        스트리밍 앱이 <strong>스트림 입력 데이터</strong>를 배치 작업에서 주기적으로 만들어내는 <strong>데이터셋</strong>과 <strong>조인</strong>해야하는 경우가 있다.
      </li>
      <li>
        <strong>스트리밍 작업의 출력</strong>이 <strong>배치 작업용 쿼리</strong>에 필요한 파일이나 테이블일 수 있다.
      </li>
    </ul>
  <li>
    구조적 스트리밍은 배치 앱을 포함한 여러 컴포넌트와 <strong>쉽게 연동</strong>할 수 있도록 설계 되었다.
  </li>
  <li>
    구조적 스트리밍 개발자는 <strong>연속형 애플리케이션(continuous application)</strong>이라는 용어를 만들고 Spark에 개념을 추가하였다.
  </li>
    <ul>
      <li>
        연속형 애플리케이션(continuous application)이란 스트리밍, 배치 그리고 대화형 작업으로 구성된 <strong>통합 앱</strong>을 의미한다.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 스트림 처리 사례</h2>
