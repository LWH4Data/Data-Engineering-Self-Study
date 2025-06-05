<h1>Chapter 1. What Is Apache Spark</h1>
<ul>
  <li>
    Apache Spark는 <a href="#computer-clusters">computer clusters</a>에서 데이터 병렬 처리를 위해 사용되는 통합된 컴퓨팅 엔진이자 라이브러리들의 모음.
  </li>
  <li>
    유연한 확장성
    <ul>
      <li>다양한 언어(e.g. Python, Java, Scala, and R)에서 사용 가능.</li>
      <li>SQL과 ML을 포함한 다양한 라이브러리 포함.</li>
      <li>단일 labtop부터 수천개의 서버를 포함하는 클러스터에도 적용 가능.</li>
    </ul>
  </li>
  <li>
    하단의 그림처럼 Spark의 모든 측면에 대해서 배운다.  
    (하단의 이미지는 Spark가 end-users에게 제공하는 모든 components와 libraries이다).
    <br>
    <img src="images/Figure_01.png" alt="Spark toolkit" width="40%">
  </li>
</ul>

<br><br>

<h2>1-1. Apache Spark's Philosophy</h2>
<h3>1-1-1. Unified</h3>

<ul>
  <li>
    Spark의 핵심 목표는 빅데이터 애플리케이션을 작성하기 위한 <strong>통합 플랫폼</strong>을 제공하는 것.
    <ul>
      <li>
        e.g. 데이터 적재, SQL 쿼리, 머신러닝, 스트리밍 연산 등을 하나의 엔진과 API 구조에서 처리
      </li>
    </ul>
  </li>

  <li>
    즉, Jupyter Notebook 같은 분석 도구나, production 시스템 개발 환경에서도 Spark는 다양한 processing types와 libraries를 <strong>하나의 환경에 통합</strong>하여 보다 쉽고 효율적인 <strong>데이터 파이프라인</strong> 구성이 가능하다.
  </li>

  <li>
    Spark의 Unified 특성이 더 쉽고 효율적인 이유
    <ul>
      <li>
        첫째, 일관되고 조합 가능한 <strong>composable API</strong> 제공 → 다양한 라이브러리를 결합하여 유연한 애플리케이션 구성 가능
      </li>
      <li>
        둘째, 고성능 실행을 위한 최적화된 엔진 제공 → 여러 라이브러리/함수 조합에도 <cstrong>고성능 유지</strong>
        <ul>
          <li>
            예: SQL로 데이터 로딩 → MLlib로 모델 평가 → 이 과정을 한 번의 데이터 스캔으로 파이프라인화 가능
          </li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    Spark 이전에는 다양한 시스템과 API를 수작업으로 연결해야 했지만, Spark는 이를 하나의 <strong>통합된 엔진</strong>으로 해결함.
    <ul>
      <li>
        이는 Python, R의 통합 라이브러리 생태계나, 웹 프레임워크(Node.js, Django)처럼 일관된 개발 환경과 유사한 철학이다.
      </li>
    </ul>
  </li>
</ul>
<br>

<h3>1-1-2. Computing engine</h3>
<ul>
  <li>
    Spark는 <strong>컴퓨팅 엔진</strong>에만 집중하도록 설계되었으며, 데이터 저장이 아닌 <strong>계산 처리</strong>에 초점을 맞춘다.
    <ul>
      <li>
        다양한 스토리지 시스템으로부터 데이터를 불러와 연산만 수행하며, 저장은 외부 시스템에 맡긴다.
      </li>
      <li>
        Spark는 부족한 데이터 저장 기능을 주로 <strong>Hadoop</strong>과 연동하여 보완한다.
      </li>
    </ul>
  </li>

  <li>
    Spark에서 사용하는 다양한 스토리지 시스템과 외부 시스템이란 다음과 같다.
    <ul>
      <li>예: Azure Storage, Amazon S3, Apache Hadoop, Apache Cassandra, Apache Kafka 등</li>
      <li>이러한 저장소 간의 데이터 이동은 비용이 크기 때문에, Spark는 <strong>저장소 위에서 직접 계산</strong>함으로써 효율을 높임</li>
    </ul>
  </li>

  <li>
    저장소에 관계없이 연산 수행이 가능하도록 유저 친화적인 API를 제공하여, 사용자는 <cstrong>데이터 위치</strong>를 신경 쓸 필요가 없음
  </li>

  <li>
    Spark는 기존 빅데이터 플랫폼(예: Hadoop)과 비교해 차별화된 설계 철학을 가짐.
    <ul>
      <li>
        Hadoop은 저장 시스템(HDFS)과 컴퓨팅 시스템(MapReduce)이 강하게 결합되어 있었기 때문에 <strong>외부 데이터 접근에 제약</strong>이 있었음
      </li>
      <li>
        Spark는 Hadoop 위에서도 동작 가능하지만, <strong>클라우드 기반</strong>이나 <strong>다양한 저장소 환경</strong>에서도 유연하게 사용 가능
      </li>
    </ul>
  </li>
</ul>
<br>

<h3>1-1-3. Libraries</h3>
<ul>
  <li>
    Spark의 마지막 구성 요소는 <strong>라이브러리(libraries)</strong>로, 다양한 기능을 모듈화하여 제공한다.
    <ul>
      <li>
        Spark 자체에서 제공하는 공식 라이브러리뿐만 아니라 외부의 third-party 라이브러리도 풍부하게 존재한다.
      </li>
    </ul>
  </li>

  <li>
    대표적인 Spark 라이브러리는 다음과 같다:
    <ul>
      <li><strong>Spark SQL</strong>: SQL 문법을 사용하여 데이터를 질의할 수 있도록 지원</li>
      <li><strong>MLlib</strong>: 분산 머신러닝 처리를 위한 라이브러리</li>
      <li><strong>Spark Streaming 및 Structured Streaming</strong>: 실시간 데이터 스트리밍 처리를 위한 라이브러리</li>
      <li><strong>GraphX</strong>: 대규모 그래프 처리 및 분석을 위한 라이브러리</li>
    </ul>
  </li>

  <li>
    더 다양한 외부 라이브러리는 <a href="https://spark-packages.org" target="_blank">spark-packages.org</a>에서 확인할 수 있다.
  </li>
</ul>

<br><br>

<h2>1-2. Context: The Big Data Problem</h2>
<ul>
  <li>
    Spark는 현대 데이터 환경의 변화에 따라 <strong>병렬 처리</strong>의 필요성이 커지면서 등장한 기술이다.
  </li>

  <li>
    초기에는 컴퓨터 성능의 향상으로 애플리케이션이 자연스럽게 빨라지고, 단일 프로세서에서도 충분한 연산이 가능했다.
    <ul>
      <li>
        더 빠른 하드웨어는 더 큰 데이터와 복잡한 연산을 단일 머신에서 처리하게 만들었다.
      </li>
    </ul>
  </li>

  <li>
    그러나 2005년을 기점으로 하드웨어 성능 향상이 정체되고, 대신 멀티코어 CPU 등 병렬 처리 기반 구조로 전환되었다.
    <ul>
      <li>
        이는 기존 방식으로는 성능 향상이 어려워지고, 애플리케이션 역시 <strong>병렬 처리</strong>를 지원해야 함을 의미했다.
      </li>
    </ul>
  </li>

  <li>
    반면 <strong>데이터 수집 및 저장 기술은 빠르게 발전</strong>해 왔으며, <strong>저렴한 비용으로 대규모 데이터</strong>를 쌓을 수 있게 되었다.
  </li>

  <li>
    결과적으로, 쌓여가는 방대한 데이터를 효과적으로 처리할 수 있는 <strong>병렬 컴퓨팅 시스템</strong>이 필요해졌고,
    <strong>Spark</strong>는 이러한 요구를 충족시키기 위해 등장한 기술이다.
  </li>
</ul>
<br>



<br><br>
<h1>용어 정리</h1>
<h4>computer clusters</h4>
여러 대의 컴퓨터를 하나로 묶어 병렬 처리를 수행하는 시스템이다.


