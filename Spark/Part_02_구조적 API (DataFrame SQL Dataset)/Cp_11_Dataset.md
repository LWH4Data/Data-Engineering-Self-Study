<ul>
  <li>
    Dataset은 구조적 API의 기본 데이터 타입이다.
  </li>
  <li>
    Dataset은 자바 가상 머신을 사용하는 <strong>Scala</strong>와 <strong>Java</strong>에서만 사용할 수 있다.
  </li>
  <li>
    Spark는 지원하는 다양한 언어의 데이터 타입을 <strong>Spark의 특정 데이터 타입</strong>으로 변환할 수 있다.
  </li>
  <li>
    DataFrame API를 사용할 때 Spark는 데이터 타입의 객체를 생성하지는 않지만 <strong>Row 객체를 변환</strong>해 데이터를 처리한다.
  </li>
  <li>
    Scala 혹은 Java를 사용할 때 모든 <strong>DataFrame</strong>은 <strong>Row 타입의 Dataset</strong>을 의미한다.
  </li>
  <li>
    도메인별 특정 객체를 효과적으로 지원하기 위해 <strong>인코더(encoder)</strong>라 부르는 특수 개념이 필요하다.
  </li>
    <ul>
      <li>
        <strong>인코더</strong>란 도메인별 <strong>특정 객체 T</strong>를 <strong>Spark의 내부 데이터 타입으로 매핑</strong>하는 시스템이다.
      </li>
    </ul>
  <li>
    name(string)과 age(int) 두 개의 필드를 갖는 Person 클래스<br>→ 인코더는 런타임 환경에서 Person 객체를 바이너르 구조로 직렬화 코드 생성을 Spark에 지시
  </li>
    <ul>
      <li>
        DataFrame이나 표준 구조적 API를 사용하면 Row 타입을 직렬화된 바이너리 구조로 변환.
      </li>
    </ul>
  <li>
    도메인에 특화된 객체를 생성하여 사용하려면 <strong>Scala의 case class</strong> 혹은 <strong>Java의 JavaBean</strong> 형태로 사용자 정의 데이터 타입을 정의해야 한다.
  </li>
  <li>
    Spark는 Row 타입 대신 <strong>사용자 정의 테이터 타입</strong>을 분산 방식으로 다룰 수 있다.
  </li>
  <li>
    Dataset API를 사용하면 Spark는 데이터셋에 접근할 때마다 Row 포맷이 아닌 사용자 정의 데이터 타입으로 변환한다.
  </li>
    <ul>
      <li>
        변환 작업은 느리지만 사용자에게 더 많은 <strong>유연성</strong>을 제공한다.
      </li>
      <li>
        사용자 정의 데이터 타입을 사용하면 <strong>성능이 나빠진다</strong>. 프로그래밍 언어를 전환하는 것이 사용자 정의 데이터 타입을 사용하는 것보다 느리기 때문이다.
      </li>
    </ul>
</ul>

<br>

<h1>1. Dataset을 사용할 시기</h1>
<ul>
  <li>
    성능이 느려짐에도 Dataset을 사용하는 두 가지 이유는 다음과 같다.
  </li>
    <ul>
      <li>
        DataFrame 기능만으로 수행할 <strong>연산을 표현할 수 없는</strong> 경우.
      </li>
      <li>
        성능 저하를 감수하더라도 <strong>타입 안정성(type-safe)</strong>을 갖는 데이터 타입을 사용할 경우.
      </li>
    </ul>
  <li>
    Dataset을 사용해야 하는 사례들
  </li>
    <ul>
      <li>
        복잡한 비즈니스 로직을 SQL이나 DataFrame 대신 <strong>단일 함수</strong>로 인코딩하는 경우.
      </li>
      <li>
        두 문자열을 사용해 뺄셈 연산을 하는 등 <strong>데이터 타입이 유효하지 않은 경우</strong>. 데이터 타입이 유효하지 않은 경우 컴파일 타임에 오류가 발생한다.
      </li>
    </ul>
  <li>
    단일 노드의 워크로드와 Spark 워크로드에서 전체 row에 대한 다양한 transformation을 <strong>재사용</strong> 하려면 DataSet을 사용하는 것이 적합하다.
  </li>
    <ul>
      <li>
        Spark API는 <strong>스칼라의 Sequence 타입의 API</strong>가 일부 반영되 있으며 <strong>분산 방식</strong>으로 동작한다.
      </li>
    </ul>
  <li>
    올바른 클래스와 데이터 타입이 지정된 DataFrame을 <strong>로컬 디스크</strong>에 저장하면 다음 처리 과정에서 사용할 수 있다.
  </li>
  <li>
    더 적합한 워크로드를 만들기 위해 DataFrame과 Dataset을 <strong>동시해</strong> 사용해야 할 때가 있다.
  </li>
  <li>
    성능과 타입 안정성 중 하나는 희생할 수밖에 없다.
  </li>
</ul>

<br><br>

<h1>2. Dataset 생성</h1>
<ul>
  <li>
    Dataset을 생성하는 것은 수동 작업이기에 정의할 <strong>스키마</strong>를 미리 알고 있어야 한다.
  </li>
</ul>

<br>

<h2>2-1. 자바: Encoders</h2>

```java
// 데이터 타입 클래스를 정의한 뒤 DataFrame(Dataset<Row> 타입)에 지정해 인코딩.
import org.apache.spark.sql.Encoders;

public class Flight implements Serializable(
    String DEST_COUNTRY_NAME;
    STRING ORIGIN_COUNTRY_NAME;
    LONG DEST_COUNTRY_NAME;
)

Dataset<Flight> flights = spark.read
  .parquet("/opt/spark-data/data/flight-data/parquet/2010-summary.parquet/")
  .as(Encoders.bean(Flight.class));
```

<br>


<h2>2-2. 스칼라: 케이스 클래스</h2>
<ul>
  <li>
    Scala에서 Dataset을 생성할 때에는 Scala <strong>case class 구문</strong>을 사용하여 데이터 타입을 정의한다.
  </li>
  <li>
    case class는 다음과 같은 특징을 갖는 <strong>정규 클래스(regular class)</strong>이다.
  </li>
    <ul>
      <li>
        <strong>불변성</strong>: 객체들이 언제 어디서 변경되었는지 추적할 필요가 없다.
      </li>
      <li>
        <strong>패턴 매칭으로 분해 가능</strong>: 로직 분기를 단순화하여 버그를 줄이고 가독성을 높인다.
      </li>
      <li>
        <strong>참조값 대신 클래스 구조를 기반으로 비교</strong>: 값으로 비교되는지 참조로 비교되는지 불확실하지 않다.
      </li>
      <li>
        <strong>사용하기 쉽고 다루기 편함</strong>.
      </li>
    </ul>
</ul>

```scala
// 1. 예제 데이터 셋 중 하나를 case class로 정의. (Flight 데이터 타입의 Dataset 생성)
case class Flight(DEST_COUNTRY_NAME: String,
                  ORIGIN_COUNTRY_NAME: String, count: BigInt)
```

```scala
// 2. Flight 데이터 타입은 스키마만 정의되어 있다. 데이터를 읽으면 DataFrame을 반환한다.
val flightsDF = spark.read
  .parquet("/opt/spark-data/data/flight-data/parquet/2010-summary.parquet/")
```

```scala
// 3. as 메서드를 사용해 Flight 타입으로 변환.
val flights = flightsDF.as[Flight]
```

<br><br>

<h1>3. 액션</h1>
<ul>
  <li>
    Dataset과 DataFrame에 collect, take 그리고 count 같은 <strong>액션</strong>을 적용할 수 있다는 사실이 중요하다.
  </li>
  <li>
    case class에 접근할 때에는 어떠한 데이터 타입도 필요하지 않다. case class 속성명을 지정하면 속성에 맞는 값과 데이터 타입을 모두 반환한다.
  </li>
</ul>

```python
# 1. show()를 통한 조회
flights.show()
```

```scala
// 2. case class 확인.
flights.first.DEST_COUNTRY_NAME // United States
```

<br><br>

<h1>4. 트랜스포메이션</h1>
<ul>
  <li>
    Dataset의 transformation은 <strong>DataFrame과 동일</strong>하다. 
  </li>
  <li>
    Dataset을 사용하면 <strong>원형의 JVM 데이터 타입</strong>을 다루기에 DataFrame만을 사용할 때 보다는 더 <strong>복잡하고 강력한 데이터 타입</strong>으로 transformation을 사용할 수 있다.
  </li>
</ul>

<br>

<h2>4-1. 필터링</h2>
<ul>
  <li>
    Spark는 정의된 함수를 사용해 <strong>모든 row를 평가</strong>하기 때문에 매우 <strong>많은 자원</strong>을 소모한다. 따라서 <strong>단순 필터</strong>는 <strong>SQL 표현식</strong>을 사용하는 것이 좋다.
  </li>
  <li>
    SQL 표현식을 사용하면 데이터 필터링 비용이 크게 줄고 다음 처리 과정에서 Dataset으로 데이터를 다룰 수 있다.
  </li>
</ul>

```scala
// 1. Flight 클래스를 파라미터로 사용해 불리언값을 반환하는 함수 생성(일반 함수).
def originIsDestination(flight_row:Flight): Boolean = {
  return flight_row.ORIGIN_COUNTRY_NAME == flight_row.DEST_COUNTRY_NAME
}
```

```scala
// 2. 정의한 함수를 filter 메서드에 적용해 각 행이 true를 반환하는지 평가하고 데이터셋을 필터링.
flights.filter(flight_row => originIsDestination(flight_row)).first()
```

<br>

<h2>4-2. 매핑</h2>
<ul>
  <li>
    DataFrame에 매핑 작업을 수행하는 것은 Dataset의 select 메서드를 사용하는 것과 같다.
  </li>
  <li>
    사실 매핑 작업보다 더 많은 장점을 얻을 수 있으므로 <strong>DataFrame</strong>을 사용하는 것이 좋다.
  </li>
</ul>

```scala
// 1. 목적지 컬럼을 추출하는 예제
val destinations = flights.map(f => f.DEST_COUNTRY_NAME)
```

<br><br>

<h1>5. 조인</h1>
<ul>
  <li>
    조인 또한 DataFrame과 Dataset 모두 동일하게 작용한다.
  </li>
  <li>
    Dataset은 <strong>joinWith</strong>을 사용하면 더 많은 정보를 유지할 수 있으며 고급 맵이나 필터처럼 정교하게 데이터를 다룰 수 있다.
  </li>
    <ul>
      <li>
        joinWith 메서드는 co-group과 거의 유사하며 <strong>Dataset 안쪽</strong>에 <strong>다른 두 개의 중첩된 Dataset</strong>으로 구성된다.
      </li>
      <li>
        각 컬럼은 단일 Dataset 이기에 <strong>Dataset 객체</strong>를 <strong>컬럼</strong>처럼 다룰 수 있다.
      </li>
    </ul>
</ul>

```scala
// 1. 실습을 위해 가짜 항공운항 메타데이터 Dataset 생성.
case class FlightMetadata(count: BigInt, randomData: BigInt)

val flightsMeta = spark.range(500).map(x => (x, scala.util.Random.nextLong))
  .withColumnRenamed("_1", "count").withColumnRenamed("_2", "randomData")
  .as[FlightMetadata]

val flights2 = flights
  .joinWith(flightsMeta, flights.col("count") === flightMeta.col("count"))

// row는 Flight와 FlightMetadata로 이루어진 일종의 ket-value 형태의 Dataset을 반환한
// 다.
```

```scala
// 2. Dataset이나 복합 데이터 타입의 DataFrame으로 데이터를 조회한다.
flights2.selectExpr("_1.DEST_COUNTRY_NAME")
```

```scala
// 3. 드라이버로 데이터를 모은 다음 결과 반환
flights2.take(2)
```

```scala
// 3. 조인도 잘 수행 되지만 DataFrame을 반환하면서 JVM 데이터 타입 정보를 잃게 된다.
val flights = flights.join(flightsMeta, Seq("count"))
```

```scala
// 4. 잃어버린 JVM 데이터 타입 정보를 얻으려면 Dataset을 정의해야 한다.
val flights = flights.join(flightsMeta.toDF(), Seq("count"))
```

<br><br>

<h1>6. 그룹화 집계</h1>
<ul>
  <li>
    동일한 표준을 따르기에 DataFrame과 동일하게 <strong>groupBy, rollup 그리고 cube 메서드</strong>를 사용할 수 있다. 단, DataFrame을 반환하기에 <strong>데이터 타입 정보를 잃게 된다</strong>.
  </li>
  <li>
    <strong>groupByKey 메서드</strong>와 같은 경우 Dataset의 <strong>특정 키</strong>를 기준으로 그룹화하고 Dataset을 반환하기에 <strong>데이터 타입을 유지</strong>할 수 있다.
  </li>
    <ul>
      <li>
        단, 컬럼명 대신 <strong>함수</strong>를 파라미터로 받는다.
      </li>
      <li>
        Spark는 함수와 JVM 데이터 타입을 최적화 할 수 없기 때문에 trade-off가 발생한다. 이로인해 성능 차이가 발생할 수 있다.
      </li>
    </ul>
  <li>
    Dataset은 빅데이터 처리 파이프라인의 <strong>처음과 끝</strong> 작업에서 주로 사용하게 된다.
  </li>
    <ul>
      <li>
        <strong>처음</strong>: 원시 데이터를 Dataset으로 변환하여 <strong>Spark가 최적화</strong>를 적용할 수 있게 함.
      </li>
      <li>
    </ul>
        <strong>끝</strong>: Spark 파이프라인의 마지막은 보통 <strong>드라이버 변환(collect show)</strong>이다. Spark의 최종 객체 단위가 <strong>Dataset</strong>이기 때문이다.
    </li>
</ul>

```scala
// 1. count() 집계 수행.
flights.groupBy("DEST_COUNTRY_NAME").count()
```

```scala
// 2. groupByKey 메서드를 통해 Dataset을 반환하고 데이터 타입 유지
flgihts.groupByKey(x => x.DEST_COUNTRY_NAME).count()
```

```scala
// 3. groupByKey 메서드를 사용해 DataFrame에 새로운 컬럼을 추가한 다음 그룹화 수행.
flgihts.groupByKey(x => x.DEST_COUNTRY_NAME).count().explain
```

```scala
// 4. Dataset의 key를 이용해 그룹화를 수행한 뒤 결과를 key-value 형태로 함수에 전달하여
//    원시 객체 형태 그대로 그룹화된 데이터를 다룰 수 있다.
def grpSum(countryName:String, values: Iterator[Flight]) = {
  values.dropWhile(_.count < 5).map(x => (countryName, x))
}
flights.groupByKey(x => x.DEST_COUNTRY_NAME).flatMapGroups(grpSum).show(5)
```

```scala
// 5. 새로운 처리 방법을 생성해 그룹을 축소(reduce)
def sum2(left:Flight, right:Flight) = {
  Flight(left.DEST_COUNTRY_NAME, null, left.count + right.count)
}
flights.groupByKey(x => x.DEST_COUNTRY_NAME).reduceGroups((1, r) => sum2(1, r)).take(5)
```

```scala
// 6. groupByKey 메서드는 동일한 결과를 반환하지만 데이터 스캔 직후 집계를 수행하는 
//    groupBy 메서드에 비해 더 비싼 처리를 수행한다.
flights.groupBy("DEST_COUNTRY_NAME").count().explain

// 따라서 사용자가 정의한 인코딩을 세밀한 처리 등이 필요한 경우에만 Dataset의 groupByKey
// 메서드를 사용해야 한다.
```