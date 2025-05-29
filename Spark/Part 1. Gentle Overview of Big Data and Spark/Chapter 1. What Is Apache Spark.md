# Chapter 1. What Is Apache Spark
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
<br>

## Apache Spark's Philosophy
<ul>



</ul>

<br><br>

## 1-1. Apache Spark's Philosophy 
### 1-1-1. Unified

<ul>
  <li>
    Spark의 핵심 목표는 빅데이터 애플리케이션을 작성하기 위한 <code>통합 플랫폼</code>을 제공하는 것.
    <ul>
      <li>
        e.g. 데이터 적재, SQL 쿼리, 머신러닝, 스트리밍 연산 등을 하나의 엔진과 API 구조에서 처리
      </li>
    </ul>
  </li>

  <li>
    즉, Jupyter Notebook 같은 분석 도구나, production 시스템 개발 환경에서도 Spark는 다양한 processing types와 libraries를 <code>하나의 환경에 통합</code>하여 보다 쉽고 효율적인 <code>데이터 파이프라인</code> 구성이 가능하다.
  </li>

  <li>
    Spark의 Unified 특성이 더 쉽고 효율적인 이유
    <ul>
      <li>
        첫째, 일관되고 조합 가능한 <code>composable API</code> 제공 → 다양한 라이브러리를 결합하여 유연한 애플리케이션 구성 가능
      </li>
      <li>
        둘째, 고성능 실행을 위한 최적화된 엔진 제공 → 여러 라이브러리/함수 조합에도 <code>고성능 유지</code>
        <ul>
          <li>
            예: SQL로 데이터 로딩 → MLlib로 모델 평가 → 이 과정을 한 번의 데이터 스캔으로 파이프라인화 가능
          </li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    Spark 이전에는 다양한 시스템과 API를 수작업으로 연결해야 했지만, Spark는 이를 하나의 <code>통합된 엔진</code>으로 해결함.
    <ul>
      <li>
        이는 Python, R의 통합 라이브러리 생태계나, 웹 프레임워크(Node.js, Django)처럼 일관된 개발 환경과 유사한 철학이다.
      </li>
    </ul>
  </li>
</ul>
<br>

### 1-1-2. Computing engine
<ul>
  <li>

  </li>
</ul>
- computing engine에도 신경을 많이 씀. <br>
- 


<br><br>
# 용어 정리
#### computer clusters 
여러 대의 컴퓨터를 하나로 묶어 병렬 처리를 수행하는 시스템이다.

