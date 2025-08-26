<ul>
  <li>
    구조적 API에는 다음 세 가지 <strong>분산 컬렉션 API</strong>가 있다. <strong>Dataset</strong>과 <strong>DataFrame</strong> 그리고 <strong>SQL Table & View</strong>
  </li>
  <li>
    <strong>배치(batch)</strong>와 <strong>스트리밍(streaming) 처리</strong>에 <strong>구조적 API</strong>를 사용할 수 있다.
  </li>
  <li>
    이번 장에서는 다음 세 가지를 반드시 이해해야 한다.
  </li>
    <ul>
      <li>
        <strong>타입형(typed)</strong> & <strong>비타입형(untyped)</strong> API 개념과 차이점
      </li>
      <li>
        <strong>핵심 용어</strong>들
      </li>
      <li>
        Spark가 구조적 API의 <strong>데이터 흐름을 해석</strong>하고 <strong>클러스터에서 실행</strong>하는 방식.
      </li>
    </ul>
  <li>
    복습 내용
  </li>
    <ul>
      <li>
        Spark는 <strong>transformation</strong>의 처리 과정을 정의하는 <strong>분산 프로그래밍 모델</strong>이다.
      </li>
      <li>
        사용자가 정의한 다수의 <strong>transformation</strong>은 지향성 비순환 그래프(<strong>DAG</strong>)로 표현되는 <strong>명령을 생성</strong>한다.
      </li>
      <li>
        <strong>Action</strong>은 <strong>하나의 Job</strong>을 클러스터에서 실행하기 위해 <strong>Stage</strong>와 <strong>Task</strong> 단위로 나누고, <strong>DAG 처리 프로세스를 실행</strong>한다.
      </li>
      <li>
        <strong>DataFrame</strong>과 <strong>Dataset</strong>은 transformation과 action으로 다루는 논리적 구조이다.
      </li>
      <li>
        <strong>새로운</strong> DataFrame이나 Dataset을 생성하려면 <strong>transformation을 호출</strong>해야 한다.
      </li>
      <li>
        <strong>연산을 시작</strong>하거나 사용한 언어에 맞는 <strong>데이터 타입으로 변환</strong>하려면 <strong>action을 호출</strong>해야한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>1. DataFrame과 Dataset</h1>
<ul>
  <li>
    Spark는 <strong>DataFrame</strong>과 <strong>Dataset</strong> 두 가지 구조화된 컬렉션 개념을 갖는다.
  </li>
  <li>
    DataFrame과 Dataset은 <strong>row</strong>와 <strong>column</strong>을 갖는 <strong>분산 테이블 형태</strong>의 컬렉션이다.
  </li>
  <li>
    각 컬럼은 다른 컬럼과 <strong>동일한 수의 row</strong>를 갖는다. (값이 없는 경우는 null).
  </li>
  <li>
    컬렉션의 모든 row는 <strong>같은 데이터 타입 정보</strong>를 갖는다.
  </li>
  <li>
    DataFrame과 Dataset은 어떤 연산을 적용해야 하는지 정의하는 <strong>지연 연산의 실행 계획</strong>이며, <strong>불변성</strong>을 갖는다.
  </li>
  <li>
    DataFrame에 <strong>action을 호출</strong>하면 Spark는 <strong>transformation을 수행</strong>하고, <strong>결과를 반환</strong> 받는다.
  </li>
  <li>
    태이블과 뷰는 DataFrame과 같다. 단, <strong>테이블은 SQL을 사용</strong>한다.
  </li>
</ul>

<br><br>

<h1>2. 스키마</h1>
<ul>
  <li>
    Schema는 DataFrame의 <strong>컬럼명</strong>과 <strong>데이터 타입</strong>을 정의한다.
  </li>
  <li>
    Schema는 <strong>데이터소스</strong>에서 얻거나(schema-on-read) <strong>직접 정의</strong>할 수 있다.
  </li>
  <li>
    Schema는 <strong>여러 데이터 타입으로 구성</strong>되기 때문에 <strong>어떤 데이터 타입</strong>이 <strong>어느 위치</strong>에 있는지 <strong>정의하는 방법</strong>이 필요하다.
  </li>
</ul>

<br><br>

<h1>3. 스파크의 구조적 데이터 타입 개요</h1>
<ul>
  <li>
    Spark는 프로그래밍 언어이며 <strong>Catalyst 엔진</strong>을 사용한다.
  </li>
  <li>
    <strong>Catalyst 엔진</strong>은 Spark 실행 계획 수립과 처리에 사용하는 <strong>데이터 타입 정보</strong>를 갖는다.
  </li>
  <li>
    Spark는 <strong>자체 데이터 타입</strong>을 지원한다. 다른 구조적 API를 사용하더라도 대부분 연산은 <strong>Spark의 데이터 타입을 사용</strong>한다.
  </li>
</ul>

```python
# 1. Spark의 덧셈 연산 예제
# - Spark 지원 언어 
#   → Catalyst 엔진이 Spark 데이터 타입으로 변환 
#   → 명령을 처리.
df = spark.range(500).toDF("number")
df.select(df["number"] + 10)
```

<br>

<h2>3-1. DataFrame과 Dataset 비교</h2>
<ul>
  <li>
    구조적 API에는 <strong>untyped인 DataFrame</strong>과 typed인 Dataset이 있다.
  </li>
    <ul>
      <li>
        <strong>DataFrame</strong>은 schema에 명시된 데이터 <strong>타입의 일치 여부</strong>를 <strong>런타임</strong>에 확인한다.
      </li>
      <li>
        Dataset은 schema에 명시된 데이터 타입의 일치 여부를 컴파일 타임에 확인한다.
      </li>
      <li>
        Dataset은 JVM 기반의 Scala와 Java에서만 지원된다.
      </li>
        <ul>
          <li>
            데이터 타입을 정의하려면 Scala의 case class 혹은 Java의 JavaBean을 사용해야 한다.
          </li>
        </ul>
    </ul>
  <li>
    책의 실습 예제들은 <strong>DataFrame</strong>을 사용한다. Spark의 DataFrame은 <strong>row 타입으로 구성된 Dataset</strong>이다.
  </li>
  <li>
    Row 타입은 Spark가 사용하는 연산에 최적화된 인메모리 포맷의 내부적인 표현 방식이다.
  </li>
  <li>
    <strong>Row 타입</strong>을 사용하면 garbage collection과 객체 초기화 부하가 있는 JVM 데이터 타입을 사용하는 대신 <strong>자체 데이터 포맷</strong>을 사용하기에 <strong>매우 효율적인 연산</strong>이 가능하다.
  </li>
  <li>
    핵심은 <strong>DataFrame</strong>을 사용하면 <strong>Spark의 최적화된 내부 포맷</strong>을 사용할 수 있다는 것이다.
  </li>
</ul>

<br>

<h2>3-2. 컬럼</h2>
<ul>
  <li>
    Column은 정수형이나 문자열 같은 <strong>단순 데이터 타입</strong>과 배열이나 맵 같은 <strong>복합 데이터 타입</strong> 그리고 <strong>null 값</strong>을 표현한다.
  </li>
  <li>
    Spark의 column은 테이블의 컬럼으로 생각할 수도 있다.
  </li>
</ul>

<br>

<h2>3. 로우</h2>
<ul>
  <li>
    Row는 데이터 record이다.
  </li>
  <li>
    DataFrame의 record는 row 타입으로 구성된다.
  </li>
  <li>
    Row는 SQL, RDD, 데이터소스에서 얻거나 직접 만들 수 있다.
  </li>
</ul>

```python
# 1. Row 생성 예제
spark.range(2).collect()
```

<br>

<h2>3-4. 스파크 데이터 타입 (P116)</h2>
<ul>
  <li>
    각 언어의 데이터 타입과 매핑되는 Spark의 데이터 타입을 표로 정리. 필요할 때 참고하면 된다.
  </li>
  <li>
    최신 데이터 타입을 확인하려면 Spark의 공식 문서(http://bit.ly/2EdflXW)를 확인하면 된다.
  </li>
</ul>

```python
# 1. 파이썬 데이터타입 선언 예
from pyspark.sql.types import *

b = ByteType()
```

<br><br>

<h1>4. 구조적 API의 실행 과정</h1>
<ul>
  <li>
    Spark 코드가 클러스터에서 실제 처리되는 과정을 정리한다.
  </li>
    <ul>
      <li>
        DataFrame/Dataset/SQL을 이용해 코드를 작성한다.<br>→ Spark가 논리적 실행 계획으로 변환한다.<br>→ Spark는 논리적 실행 계획을 물리적 실행 계획으로 변환하고 추가적인 최적화 가능 여부를 확인한다.<br>→ Spark는 클러스터에서 물리적 실행 계획(RDD 처리)을 실행한다.
      </li>
    </ul>
  <li>
    실행할 <strong>코드 작성</strong><br>→ 콘솔이나 spark-submit shell script로 <strong>실행</strong>.<br>→ Catalyst Optimizer가 코드를 넘겨받고 실제 <strong>실행 계획을 생성</strong>.<br>→ Spark가 코드를 실행한 후 <strong>결과 반환</strong>.
  </li>
</ul>

<br>

<h2>4-1. 논리적 실행 계획</h2>
<ul>
  <li>
    사용자 코드<br>→ 검증 전 논리적 실행 계획<br>→ 분석(카탈로그)<br>→ 검증된 논리적 실행 계획<br>→ 논리적 최적화<br>→ 최적화된 논리적 실행 계획
  </li>
  <li>
    논리적 실행 계획 단계에서는 <strong>추상적 트랜스포메이션</strong>만 표현하고 드라이버나 익스큐터의 정보는 고려하지 않는다.
  </li>
  <li>
    <strong>검증 전 논리적 실행 계획(unresolved logical plan)</strong> 단계에서는 <strong>코드의 유효성</strong>과 <strong>테이블이나 컬럼의 존재 여부</strong>만을 판단한다.
  </li>
    <ul>
      <li>
        검증 시에는 <strong>카탈로그 분석</strong>이 진행된다. Spark의 분석기(analyzer)는 컬럼과 테이블을 검증하기 위해 카탈로그, 모든 테이블의 저장소 그리고 DataFrame 정보를 활용한다.
      </li>
    </ul>
  <li>
    검증이 완료되면 <strong>카탈리스트 옵티마이저</strong>로 전달된다.
  </li>
    <ul>
      <li>
        카탈리스트 옵티마이저란 조건절 푸시다운, 선택절 구문 등 논리적 <strong>실행 계획을 최적화하는 규칙 모음</strong>이다.
      </li>
      <li>
        필요한 경우 도메인에 최적화된 규칙을 적용할 수 있는 카탈리스트 옵티마이저 확장형 패키지도 만들 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>4-2. 물리적 실행 계획</h2>
<ul>
  <li>
    최적화된 논리적 실행 계획<br>→ 물리적 실행 계획<br>→ 비용 모델<br>→ 최적의 물리적 실행 계획<br>→ 클러스터에서 처리
  </li>
  <li>
    물리적 실행 계획은 논리적 실행 계획을 <strong>클러스터에 환경에서 실행</strong>하는 방법을 정의한다.
  </li>
  <li>
    최적화된 논리적 실행 계획은 <strong>비용 모델을 통해 비교</strong>된 후 <strong>최적의 전략</strong>을 선택한다.
  </li>
    <ul>
      <li>
        비용 모델의 예로는 테이블의 크기, 파티션의 수 등이 있다. 
      </li>
    </ul>
  <li>
    <strong>RDD</strong>와 <strong>transformation</strong>으로 최적화된 물리적 실행 계획은 <strong>클러스터에서 실행</strong>된다. 
  </li>
</ul>

<br>

<h2>4-3. 실행</h2>
<ul>
  <li>
    Spark <strong>물리적 실행 계획 선정</strong><br>→ 저수준 프로그래밍 인터페이스인 <strong>RDD</strong>를 대상을 <strong>모든 코드 실행</strong><br>→ Spark runtime에 전체 task 혹은 stage를 제거할 수 있는 <strong>자바 바이트 코드</strong>를 생성하여 추가적 <strong>최적화</strong><br>→ 처리 결과를 <strong>사용자에게 반환</strong>
  </li>
</ul>