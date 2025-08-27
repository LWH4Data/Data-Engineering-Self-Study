<h1>0. DataFrame과 DataFrame의 데이터를 다루는 기술.</h1>
<ul>
  <li>
    <strong>Row 타입의 record</strong>: 테이블의 row와 같다.
  </li>
  <li>
    <strong>Column</strong>: 스트레드시트의 컬럼과 같다. 각 record에 수행할 연산 표현식을 나타낸다.
  </li>
  <li>
    <strong>Schema</strong>: 각 컬럼명과 데이터 타입을 정의한다.
  </li>
  <li>
    <strong>Partitioning</strong>: DataFrame이나 Dataset이 클러스터에서 물리적으로 배치되는 형태를 정의한다.
  </li>
  <li>
    <strong>Partitioning Schema</strong>: partition을 배치하는 방법을 정의한다.
  </li>
    <ul>
      <li>
        partitioning의 분할 기준은 <strong>특정 컬럼</strong>이나 <strong>비결정론적(nondeterministically) 값</strong>을 기반으로 설정할 수 있다.
      </li>
    </ul>
</ul>

```bash
# 1. 필요한 데이터가 있는 경로를 마운트하여 Spark 컨테이너 가동.
docker run --rm -it \
  -v "/mnt/c/Users/SSAFY/Desktop/spark-prac/Spark-The-Definitive-Guide:/opt/spark-data:ro" \
  apache/spark:3.5.2 /opt/spark/bin/pyspark
```

```python
# 2. 실습을 위한 DataFrame을 생성.
df = spark.read.format("json").load("/opt/spark-data/data/flight-data/json")

# 결과 확인 
df.printSchema()
```

<br><br>

<h1>1. 스키마</h1>
<ul>
  <li>
    Schema는 DataFrame의 <strong>컬럼명</strong>과 <strong>데이터 타입</strong>을 정의한다.
  </li>
  <li>
    Schema는 <strong>데이터소스</strong>에서 얻거나 <strong>직접 정의</strong>할 수 있다.
  </li>
    <ul>
      <li>
        <strong>비정형 분석(ad-hoc analysis)</strong>을 할 때에는 직접 schema를 얻는 <strong>schema-on-read</strong>를 사용하기 좋다.
      </li>
      <li>
        <strong>ETL 작업 중</strong>에는 데이터 타입을 잘못 읽는 경우가 있어 <strong>직접 정의</strong>하는 것이 나을 수 있다.
      </li>
      <li>
        ETL 작접 중에 <strong>CSV나 JSON</strong>이 있다면 <strong>스키마 추론</strong>에서 읽은 샘플 데이터의 타입을 참고하여 활용할 수 있다.
      </li>
    </ul>
  <li>
    Schema는 여러 개의 <strong>StructField 타입</strong>으로 구성된 <strong>StructType 객체</strong>이다.
  </li>
    <ul>
      <li>
        <strong>StructField</strong>는 이름, 데이터 타입, 컬럼의 값이 없거나 <strong>null</strong>일 수 있는지를 지정하는 <strong>불리언값</strong>을 갖는다.
      </li>
      <li>
        컬럼과 관련된 <strong>메타 데이터</strong>를 지정할 수 있다.
      </li>
        <ul>
          <li>
            메타 데이터는 해당 <strong>컬럼</strong>과 관련된 정보이며 Spark의 <strong>머신러닝 라이브러리</strong>에서 사용한다.
          </li>
        </ul>
    </ul>
  <li>
    Schema는 <strong>복합 데이터 타입</strong>인 <strong>StructType</strong>을 가질 수 있다. (6장 설명).
  </li>
  <li>
    Spark는 런타임에 데이터 타입이 스키마의 데이터 타입과 일치하지 않으면 오류를 발생시킨다.
  </li>
  <li>
    Spark는 <strong>자체 데이터 타입</strong> 정보를 사용하기 때문에 <strong>프로그래밍 언어</strong>의 데이터 타입을 Spark의 데이터 타입으로 설정할 수 없다.
  </li>
</ul>

```python
# 1. 실습에 활용할 데이터의 형식 확인.
spark.read.format("json").load("/opt/spark-data/data/flight-data/json/2015-summary.json").schema
```

```python
# 2. DataFrame에 스키마를 만들고 적용하는 예
from pyspark.sql.types import StructField, StructType, StringType, LongType

myManualSchema = StructType([
    StructField("DEST_COUNTRY_NAME", StringType(), True),
    StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
    StructField("count", LongType(), False, metadata={"hello":"world"})
])
df = spark.read.format("json").schema(myManualSchema)\
.load("/opt/spark-data/data/flight-data/json/2015-summary.json")
```

<br><br>

<h1>2. 컬럼과 표현식</h1>
<ul>
  <li>
    Spark의 컬럼은 다른 포맷의 컬럼과 유사하며 <strong>표현식</strong>으로 DataFrame의 컬럼을 선택, 조작, 제거할 수 있다.
  </li>
  <li>
    Spark의 <strong>컬럼</strong>은 <strong>표현식</strong>을 사용하여 <strong>record 단위로 계산한 값</strong>을 단순하게 나타내는 구조이다.<br>→ 컬럼의 실젯값을 얻으려면 <strong>row</strong>가 필요하다.<br>→ Row를 얻기 위해서는 <strong>DataFrame</strong>이 필요하다.<br>→ 즉, DataFrame을 통하지 않으면 외부에서 컬럼에 접근할 수 없다.<br>→ 따라서 컬럼의 내용을 수정하려면 반드시 DataFrame의 <strong>Spark transformation</strong>을 사용해야 한다.
  </li>
</ul>

<br>

<h2>2-1. 컬럼</h2>
<ul>
  <li>
    <strong>col 함수</strong>나 <strong>column 함수</strong>를 사용하여 컬럼을 생성하고 참조하는 방식이 가장 간단하다.
  </li>
    <ul>
      <li>
        col과 column 두 함수는 <strong>컬럼명</strong>을 인수로 받는다.
      </li>
    </ul>
  <li>
    책에서는 col 함수를 지속적으로 활용한다.
  </li>
  <li>
    컬럼은 컬럼명을 카탈로그에 저장된 정보와 비교하기 전까지는 <strong>미확인 상태</strong>로 남는다.<br>→ 따라서 컬럼이 DataFrame에 <strong>존재하는지 여부</strong>는 알 수 없다.<br>→ 분석기가 동작하는 단계에서 <strong>컬럼과 테이블이 분석</strong>되며 이 시점에서 DataFrame에서 <strong>컬럼의 존재여부</strong>를 알 수 있다.
  </li>
</ul>

```python
# 1. col과 column 함수로 컬럼 참조 표현식(Column)을 만들기 실습.
from pyspark.sql.functions import col, column

col("someColumnName")
column("someColumnName")
```

<h3>2-1-1. 명시적 컬럼 참조</h3>
<ul>
  <li>
    col 메서드는 <strong>join</strong> 시 유용하다.
  </li>
  <li>
    col 메서드를 사용해 명시적으로 컬럼을 정의하면 Spark는 분석기 실행 단계에서 <strong>컬럼 확인 절차를 생략</strong>한다.
  </li>
</ul>

<br>

<h2>2-2. 표현식</h2>
<ul>
  <li>
    표현식
  </li>
    <ul>
      <li>
        DataFrame record의 여러 값에 대한 <strong>transformation 집합</strong>을 의미한다.
      </li>
      <li>
        여러 컬럼을 입력으로 받아 식별하고, <strong>'단일 값'</strong>으로 만들기 위해 각 record에 적용하는 <strong>함수</strong>라 볼 수도 있다.
      </li>
        <ul>
          <li>
            단일 값에는 Map 혹은 Array와 같은 <strong>복합 데이터 타입</strong>이 포함된다. (복합 데이터 타입은 6장에서).
          </li>
        </ul>
    </ul>
  <li>
    표현식은 <strong>expr 함수</strong>로 간단히 사용할 수 있다.
  </li>
    <ul>
      <li>
        expr 함수를 통해 <strong>DataFrame의 컬럼을 참조</strong>할 수 있다. (expr("someCol") = col("someCol"))
      </li>
      <li>
        보통 <strong>SQL 문</strong>으로 처리를 할 때 expr을 사용한다고 한다.
      </li>
    </ul>
</ul>

<h3>2-2-1. 표현식으로 컬럼 표현</h3>
<ul>
  <li>
    컬럼은 표현식의 일부 기능을 지원한다.
  </li>
  <li>
    <strong>col() 함수</strong>를 통해 컬럼에 transformation을 수행할 경우 반드시 <strong>컬럼 참조</strong>를 사용햐야 한다.
  </li>
  <li>
    <strong>expr 함수</strong>의 인수로 표현식을 사용하는 경우 표현식을 분석하여 <strong>transformation</strong>과 <strong>컬럼 참조</strong>를 알낼 수 있다.
  </li>
    <ul>
      <li>
        이후 transformation의 컬럼 참조를 전달할 수 있다.
      </li>
    </ul>
  <li>
    Spark는 <strong>연산 순서</strong>를 지정하는 <strong>논리적 트리</strong>로 컴파일을 한다.
  </li>
    <ul>
      <li>
        expr("someCol - 5"), col("someCol") - 5, expr("someCol") - 5는 모두 <strong>동일한</strong> transformation 과정을 거친다.
      </li>
    </ul>
  <li>
    <strong>두 가지 핵심</strong>
  </li>
    <ul>
      <li>
        컬럼은 단지 <strong>표현식</strong>일 뿐이다. 
      </li>
      <li>
        <strong>컬럼과 컬럼의 transformation</strong>은 <strong>파싱된 표현식</strong>과 <strong>동일한 논리적 계획</strong>으로 컴파일 된다.
      </li>
    </ul>
  <li>
    DataFrame 코드가 아닌 SQL로 표현식을 작성하더라도 결국 <strong>동일한 논리적 트리로 컴파일</strong> 되기에 <strong>성능 차이는 없다</strong>.
  </li>
</ul>

```python
# 1. 교재 실습 코드
from pyspark.sql.functions import expr

expr("(((someCol + 5) * 200) - 6) < otherCol")
```

<h3>2-2-2. DataFrame 컬럼에 접근하기</h3>
<ul>
  <li>
    <strong>printSchema</strong> 메서드를 통해 DataFrame의 전체 컬럼 정보를 확인할 수 있다.
  </li>
  <li>
    프로그래밍 방식으로 컬럼에 접근할 때에는 DataFrame의 <strong>columns 속성</strong>을 사용한다.
  </li>
</ul>

```python
# 1. 실습 코드
spark.read.format("json").load("/opt/spark-data/data/flight-data/json/2015-summary.json").columns
```

<br><br>

<h1>3. 레코드와 로우</h1>
<ul>
  <li>
    Spark에서 DataFrame의 <strong>각 row</strong>는 <strong>하나의 record</strong>를 의미한다.
  </li>
  <li>
    Spark에서는 <strong>record</strong>를 <strong>Row 객체</strong>로 표현한다.
  </li>
  <li>
    Spark는 값을 생성하기 위해 <strong>컬럼 표현식</strong>으로 <strong>Row 객체</strong>를 다룬다.
  </li>
  <li>
    Row 객체는 내부에 <strong>바이트 배열</strong>을 갖는다.
  </li>
    <ul>
      <li>
        바이트 배열 인터페이스는 오직 <strong>컬럼 표현식</strong>으로만 다룰 수 있다.<br>→ 사용자에게 절대 <strong>노출되지 않는다</strong>.
      </li>
    </ul>
</ul>

```python
# 1. DataFrame의 first 메서드로 row 확인
df.first()
```

<br>

<h2>3-1. 로우 생성하기</h2>
<ul>
  <li>
    각 column에 <strong>해당하는 값</strong>을 사용해 Row 객체를 직접 생성할 수 있다.
  </li>
  <li>
    Row 객체는 Schema 정보를 갖지 않으며 유일하게 <strong>DataFrame</strong>만이 <strong>Schema 정보</strong>를 갖는다.
  </li>
    <ul>
      <li>
        따라서 <strong>Row 객체를 직접 생성</strong>할 경우 <strong>DataFrame의 Schema와 같은 순서</strong>로 값을 명시해야 한다.
      </li>
    </ul>
  <li>
    Row의 데이터에 접근하는 방법은 <strong>해당 위치(index)</strong>를 지정하면 된다.
  </li>
</ul>

```python
# 1. 실습을 위해 Row 객체 생성.
from pyspark.sql import Row

myRow = Row("Hello", None, 1, False)
```

```python
# 2. 생성한 row 확인
myRow[0]
myRow[1]
```

<br><br>

<h1>4. DataFrame의 트랜스포메이션</h1>
<ul>
  <li>
    DataFrame을 다루는 방법들에 대해 바우며 모든 작업은 transformation으로 변환이 가능하다.
  </li>
    <ul>
      <li>
        Row 혹은 column 추가.
      </li>
      <li>
        Row 혹은 column 제거.
      </li>
      <li>
        Row → column 변환 혹은 column → row 변환
      </li>
      <li>
        Column의 값을 기준으로 row 순서 변경.
      </li>
    </ul>
</ul>

<br>

<h2>4-1. DataFrame 생성하기</h2>

```python
# 1. 실습에 필요한 DataFrame 직접 생성.
df = spark.read.format("json").load("/opt/spark-data/data/flight-data/json/2015-summary.json")
```

```python
# 2. SQL의 기본 transformation을 확인하기 위해 임시 뷰로 등록
df.createOrReplaceTempView("dfTable")

# 결과 확인
df.show()
```

<br>

<h2>4-2. select와 selectExpr</h2>
<ul>
  <li>
    select와 selectExpr 메서드를 활용하면 DataFrame을 대상으로 <strong>SQL문</strong>을 사용할 수 있다.
  </li>
  <li>
    <strong>selectExpr 메서드</strong>를 통해 select와 expr을 하나의 메서드로 작성할 수 있다.
  </li>
    <ul>
      <li>
        selectExpr 메서드를 사용하면 매우 간단하게 <strong>새로운 DataFrame</strong>을 생성할 수 있다.
      </li>
    </ul>
</ul>

```python
# 1. 문자열 컬럼명을 인수로 받는 select 메서드 예
df.select("DEST_COUNTRY_NAME").show(2)
```

```python
# 2. select 메서드에 여러 컬럼명을 인수로 넣어 여러 컬럼을 조회
df.select("Dest_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)
```

```python
# 3. SQL 실습 코드. ("""로 감싼다).
spark.sql("""
  SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME
  FROM dfTable 
  LIMIT 2
""").show()
```

```python
# 4. 다양한 컬럼 참조 방식을 사용할 수 있다.
from pyspark.sql.functions import expr, col, column

df.select(
    expr("DEST_COUNTRY_NAME"),
    col("DEST_COUNTRY_NAME"),
    column("DEST_COUNTRY_NAME"))\
    .show()
```

```python
# 5. Column 객체와 문자열을 함께 섞어 쓰는 실수를 조심해야 한다. → 오류 발생
#   - col("DEST_COUNTRY_NAME"): 컬럼 객체
#   - "DEST_COUNTRY_NAME": 문자열
df.select(col("DEST_COUNTRY_NAME"), "DEST_COUNTRY_NAME")
```

```python
# 6. expr을 활용함 참조.
#   - 가장 유연한 참조 방법이다.
#   - 단순 컬럼 참조나 문자열을 이용해 컬럼을 참조할 수 있다.
df.select(expr("DEST_COUNTRY_NAME AS destination")).show(2)

# alias를 통해 다시 되돌리기.
df.select(expr("DEST_COUNTRY_NAME as destination").alias("DEST_COUNTRY_NAME")).show(2)
```

```python
# 7. selectExpr을 통해 select와 expr을 한 번에 처리.
#   - expr을 통해 컬럼을 참조할 필요가 없어진다.
df.selectExpr("DEST_COUNTRY_NAME as newColumnName", "DEST_COUNTRY_NAME").show(2)
```

```python
# 8. selectExpr을 통해 매우 간단하게 새로운 DataFrame 생성.
df.selectExpr(
    # 모든 원본 컬럼을 포함한다.
    "*",
    # 출발지와 도착지가 같은지를 나타내는 withinCountry 컬럼 추가.
    "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withinCountry")\
    .show(2)
```

```python
# 9. select 표현식에 DataFrame의 집계 함수 활용.
df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)
```

<br>

<h2>4-3. 스파크 데이터 타입으로 변환하기</h2>
<ul>
  <li>
    <strong>명시적인 값을 Spark에 전달</strong>할 때에는 <strong>리터럴(literal)</strong>을 사용한다.
  </li>
  <li>
    literal은 프로그래밍 언어의 literal 값을 Spark가 이해할 수 있는 값으로 변환한다.
  </li>
  <li>
    일반적으로 어떤 상수나 프로그래밍으로 생성된 변수의 값이 특정 컬럼의 값보다 <strong>큰지 확인</strong>할 때 사용한다.
  </li>
</ul>

```python
# 1. literal을 통해 값을 Spark에 전달.
from pyspark.sql.functions import lit

# 새로운 DataFrame이 반환된다.
#   - expr("*"): 모든 컬럼을 포함한다.
#   - lit(1).alias("One")): One라는 컬럼을 생성하고, 값으로 1을 전달한다.
df.select(expr("*"), lit(1).alias("One")).show(2)
```

<br>

<h2>4-4. 컬럼 추가하기</h2>
<ul>
  <li>
    DataFrame의 <strong>withColumn</strong> 메서드를 사용하여 신규 컬럼을 추가할 수 있다.
  </li>
  <li>
    <strong>withColumn(<컬럼명>, <값을 생성할 표현식>)</strong>
  </li>
    <ul>
      <li>
        <값을 생성할 표현식>에 <strong>기존의 컬럼명</strong>을 전달하면 <strong>컬렴명을 변경</strong>한다.
      </li>
    </ul>
</ul>

```python
# 1. 컬럼 추가 실습
df.withColumn("numberOne", lit(1)).show(2)
```

```python
# 2. 출발지와 도착지가 같은지 여부를 불리언 타입으로 생성.

# withColumn(컬럼명, 값을 생성할 표현식)
df.withColumn("withinCountry", expr("ORIGIN_COUNTRY_NAME == DEST_COUNTRY_NAME"))\
.show(2)
```

```python
# 3. withColumn을 사용하여 컬럼명 변경
df.withColumn("Destination", expr("DEST_COUNTRY_NAME")).columns
```

<br>

<h2>4-5. 컬럼명 변경하기</h2>
<ul>
  <li>
    withColumn 메서드 대신 <strong>withColumnRenamed 메서드</strong>를 활용하여 컬럼명을 변경할 수도 있다.
  </li>
  <li>
    <strong>withColumnRenamed(<기존 컬럼명>, <변경할 컬럼명>)</strong>
  </li>
</ul>

```python
# 1. withColumnRenamed를 통한 컬럼명 변경
df.withColumnRenamed("DEST_COUNTRY_NAME", "dest").columns
```

<br>

<h2>4-6. 예약 문자와 키워드</h2>
<ul>
  <li>
    공백이나 하이픈(-) 등의 <strong>예약 문자</strong>를 컬럼에 사용하기 위해서는 <strong>백틱(`)</strong>을 통해 <strong>이스케이핑(escaping)</strong> 해야한다.
  </li>
</ul>

```python
# 1. 실습을 위해 하이픈을 포함한 컬럼명으로 컬럼 생성.
dfWithLongColName = df.withColumn(
    "This Long Column-Name",
    expr("ORIGIN_COUNTRY_NAME"))
```

```python
# 2. 백틱(`)을 이용해 생성한 This Long Column-Name 컬럼을 참조.
dfWithLongColName.selectExpr(
    "`This Long Column-Name`",
    "`This Long Column-Name` as `new col`")\
    .show(2)
```

```python
# 3. 백틱(`)을 통한 컬럼 조회 예.
dfWithLongColName.select(expr("`This Long Column-Name`")).columns
```

<br>

<h2>4-7. 대소문자 구분</h2>
<ul>
  <li>
    기본적으로 Spark는 대소문자를 구분하지 않지만 다음의 세팅 등을 사용하여 대소문자를 구분하게 할 수 있다.
  </li>
</ul>

```SQL
-- 대소문자 구분 설정
set spark.sql.caseSensitive true
```

<br>

<h2>4-8. 컬럼 제거하기</h2>
<ul>
  <li>
    컬럼을 제거할 때에는 <strong>select</strong> 혹은 <strong>drop</strong> 메서드를 사용한다.
  </li>
</ul>

```python
# 1. drop 메서드를 통한 컬럼 제거
df.drop("ORIGIN_COUNTRY_NAME").columns
```

<br>

<h2>4-9. 컬럼의 데이터 타입 변경하기</h2>
<ul>
  <li>
    <strong>cast 메서드</strong>를 사용하여<strong> 데이터 타입을 변환</strong>할 수 있다.
  </li>
</ul>

```python
# 1. cast 메서드를 활용한 데이터 타입 변경. (Integer → String)
df.withColumn("count2", col("count").cast("string"))
```

<br>

<h2>4-10. 로우 필터링하기</h2>
<ul>
  <li>
    Row를 필터링하기 위해서는 <strong>참과 거짓을 판별하는 표현식</strong>을 만들어야 한다. (false인 row는 걸러진다).
  </li>
  <li>
    DataFrame은 <strong>where 메서드</strong>나 <strong>filter 메서드</strong>를 통해 필터링을 할 수 있다.
  </li>
    <ul>
      <li>
        두 메서드는 모두 같은 연산을 수행하며 같은 파라미터 타입을 사용하기에 차이가 없다.
      </li>
    </ul>
  <li>
    여러 개의 필터를 적용할 경우 Spark는 필터의 순서와 상관없이 <strong>동시에 모든 필터링을 수행</strong>한다.<br>→ 여러 개의 AND 필터링을 적용할 경우 <strong>판단은 Spark</strong>에 맡겨야 한다.
  </li>
</ul>

```python
# 1. filter와 where를 통한 데이터 필터링
df.filter(col("count") < 2).show(2)
df.where("count < 2").show(2)
```

```python
# 2. 여러 조건을 통한 필터링
df.where(col("count") < 2).where(col("ORIGIN_COUNTRY_NAME") != "Croatia")\
.show(2)
```

<br>

<h2>4-11. 고유한 로우 얻기</h2>
<ul>
  <li>
    DataFrame의 모든 row에서 중복 데이터를 제거할 수 있는 <strong>distinct</strong> 메서드를 사용하여 <strong>고윳값</strong>을 찾을 수 있다.
  </li>
  <li>
    distinct 메서드는 중복되지 않는 row를 갖는 <strong>새로운 DataFrame을 반환</strong>한다.
  </li>
</ul>

```python
# 1. 출발지와 도착지가 중복되지 않는 고유 행의 수 구하기.
df.select("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME").distinct().count()
```

```python
# 2. 출발지만 중복되지 않는 고유 행의 수 구하가.
df.select("ORIGIN_COUNTRY_NAME").distinct().count()
```

<br>

<h2>4-12. 무작위 샘플 만들기</h2>
<ul>
  <li>
    <strong>sample 메서드</strong>를 통해 DataFrame에서 <strong>무작위 샘플 데이터</strong>를 얻을 수 있다.
  </li>
    <ul>
      <li>
        표본 데이터 <strong>추출 비율</strong>을 지정할 수 있다.
      </li>
      <li>
        <strong>복원 추출(sample with replacement)</strong>과 <strong>비복원 추출(smaple without replacement)</strong>의 사용 여부를 지정할 수 있다.
      </li>
    </ul>
</ul>

```python
# 1. sample을 통한 무작위 샘플 데이터 추출.
seed = 5
withReplacement = False
fraction = 0.5
df.sample(withReplacement, fraction, seed).count()
```

<br>

<h2>4-13. 임의 분할하기</h2>
<ul>
  <li>
    <strong>임의 분할(random split)</strong>은 원본 DataFrame을 <strong>임의 크기로 분할</strong>할 때 사용한다.
  </li>
  <li>
    메서드는 <strong>임의성(randomized)</strong>을 갖도록 설계되었기에 <strong>seed 값</strong>을 설정해야 한다.
  </li>
</ul>

```python
# 1. 분할 가중치와 seed를 전달하여 데이터 분할.
dataFrames = df.randomSplit([0.25, 0.75], seed)
dataFrames[0].count() > dataFrames[1].count()
```

<br>

<h2>4-14. 로우 합치기와 축가하기</h2>
<ul>
  <li>
    DataFrame은 불변성을 갖기 때문에 <strong>record를 추가</strong>하기 위해서는 원본 DataFrame을 <strong>새로운 DataFrame</strong>과 <strong>통합(union)</strong> 해야한다.
  </li>
  <li>
    통합되는 두 DataFrame은 <strong>동일한 Schema</strong>와 <strong>컬럼 수</strong>를 가져야 한다.
  </li>
    <ul>
      <li>
        <strong>union 메서드</strong>는 현재 스키마가 아닌 <strong>컬럼의 위치</strong>를 기반으로 동작하기에 생각대로 정렬되지 않을 수 있다.
      </li>
    </ul>
  <li>
    <strong>Row가 추가된 DataFrame을 참조</strong>하려면 <strong>새롭게 만들어진 DataFrame 객체</strong>를 사용해야 한다.
  </li>
  <li>
    DataFrame을 <strong>뷰</strong>로 만들거나 <strong>테이블</strong>로 등록하면 DataFrame 변경 작업과 관계없이 <strong>동적으로 참조</strong>할 수 있다.
  </li>
</ul>

```python
from pyspark.sql import Row

# 1. 통합을 위한 새로운 DataFrame을 생성
schema = df.schema
newRows = [
    Row("New Country", "Other Country", 5),
    Row("New Country 2", "Other Country 3", 1)
]
parallelizedRows = spark.sparkContext.parallelize(newRows)
newDF = spark.createDataFrame(parallelizedRows, schema)
```

```python
# 2. 생성한 DataFrame과 병합
df.union(newDF)\
.where("count = 1")\
.where(col("ORIGIN_COUNTRY_NAME") != "United Status")\
.show()
```

<br>

<h2>4-15. 로우 정렬하기</h2>