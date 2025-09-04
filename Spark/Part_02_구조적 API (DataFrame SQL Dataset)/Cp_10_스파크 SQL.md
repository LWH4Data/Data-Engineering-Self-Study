<ul>
  <li>
    DataFrame 코드와 SQL 코드를 비교해볼 수 있도록 최대한 함께 제공.
  </li>
  <li>
    <strong>Spark SQL</strong>을 사용해 데이터베이스에 생성된 뷰(view)나 테이블에 SQL 쿼리를 실행할 수 있다.
  </li>
  <li>
    <strong>시스템 함수</strong>를 사용하거나 <strong>사용자 정의 함수</strong>를 정의할 수 있다.
  </li>
  <li>
    워크로드를 최적화하기 위해 <strong>쿼리 실행 계획을 분석</strong>할 수 있다.
  </li>
  <li>
    Spark SQL은 <strong>DataFrame</strong>과 <strong>Dataset API</strong>가 통합되어 있다. 따라서 데이터 변환 시 SQL과 DataFrame의 기능을 모두 활용할 수 있다.
  </li>
</ul>

<br><br>

<h1>1. SQL이란</h1>
<ul>
  <li>
    <strong>SQL</strong> 또는 <strong>구조적 질의 언어(Structured Query Language)</strong>는 데이터에 대한 <strong>관계형 연산</strong>을 표현하기 위한 <strong>도메인 특화 언어</strong>이다.
  </li>
</ul>

<br><br>

<h1>2. 빅데이터와 SQL: 아파치 하이브</h1>
<ul>
  <li>
    Spark 이전에는 페이스북에서 개발한 하이브가 표준 이었으나 이제는 많은 사용자가 Spark SQL을 사용한다.
  </li>
</ul>

<br><br>

<h1>3. 빅데이터와 SQL: 스파크 SQL</h1>
<ul>
  <li>
    <strong>SQL 분석가</strong>들은 thrift server나 SQL 인터페이스에 접속하여 Spark 연산 능력을 활용할 수 있다.
  </li>
  <li>
    <strong>데이터 엔지니어</strong>와 <strong>과학자</strong>는 <strong>전체 데이터 파이프라인</strong>에 Spark SQL을 사용할 수 있다.
  </li>
    <ul>
      <li>
        통합형 API는 <strong>SQL</strong>로 데이터를 조회하고 <strong>DataFrame으로 변환</strong>한 다음 Spark의 MLlib이 제공하는 <strong>머신러닝을 수행</strong>하고 결과를 <strong>데이터소스에 저장</strong>하는 <strong>전체 과정</strong>을 가능하게 한다.
      </li>
    </ul>
</ul>

<h2>3-1. 스파크와 하이브의 관계</h2>
<ul>
  <li>
    Spark SQL은 <strong>하이브 메타스토어</strong>를 사용하기에 <strong>하이브와 잘 연동</strong>할 수 있다.
  </li>
  <li>
    Spark SQL은 하이브 메타 스토어에 접속한 뒤 조회할 파일 수를 최소화하기 위해 <strong>메타데이터를 참조</strong>한다. (Hadoop에서 Spark로 이전하려는 이용자에게 인기가 있다).
  </li>
</ul>

<h3>3-1-1. 하이브 메타스토어</h3>
<ul>
  <li>
    하이브 메타스토어에 접근하기 위해 하이브 메타 스토어에 적합한 버전을 spark.sql.hive.metastore.version에 설정해야 한다.
  </li>
  <li>
    HiveMetastoreClient가 초기화되는 방식을 변경하려면 spark.sql.hive.metastore.jars를 설정한다.
  </li>
  <li>
    하이브 메타스토어가 저장된 다른 데이터베이스에 접속하려면 적합한 접두사를 정의한다.
  </li>
  <li>
    Spark와 Hive에서 공유할 수 있도록 클래스 접두사를 spark.sql.hive.metastore.sharedPrefixes 속성에 설정한다.
  </li>
</ul>

<br><br>

<h1>4. 스파크 SQL 쿼리 실행 방법</h1>
<h2>4-1. 스파크 SQL CLI</h2>
<ul>
  <li>
    Spark SQL CLI는 <strong>로컬 환경의 명령행</strong>에서 기본 Spark SQL 쿼리를 실행할 수 있는 도구이다.
  </li>
  <li>
    Spark CLI는 쓰리프트 JDBC 서버와 통신할 수 없으며 Spark SQL CLI를 사용하려면 Spark 디렉터리에서 <strong>./bin/spark.sql</strong> 명령을 실행해야 한다.
  </li>
  <li>
    Spark가 설치된 경로의 conf 디렉토리에 hive-site.xml, core-site.xml, hdfs-site.xml 파일을 배치해 하이브를 사용할 수 있는 환경을 구성할 수 있다.
  </li>
  <li>
    사용 가능한 전체 옵션을 보려면 <strong>./bin/spark-sql --help</strong> 명령을 사용한다.
  </li>
</ul>

<br>

<h2>4-2. 스파크의 프로그래밍 SQL 인터페이스</h2>
<ul>
  <li>
    Spark에서 지원하는 언어 API로 <strong>비정형 SQL</strong>을 실행할 수 있다. 이를 위해서는 <strong>SparkSession 객체의 sql 메서드</strong>를 사용한다.
  </li>
    <ul>
      <li>
        처리된 결과는 <strong>DataFrame을 반환</strong>한다.
      </li>
    </ul>
  <li>
    DataFrame을 사용하는 것보다 SQL 코드로 표현하기 쉬운 transformation이기 때문에 강력한 인터페이스이다.
  </li>
  <li>
    함수에 여러 줄로 구성된 문자열을 전달할 수 있기 때문에 <strong>여러 줄로 구성된 쿼리</strong>를 간단히 표현할 수 있다.
  </li>
  <li>
    SQL과 DataFrame을 완벽하게 연동할 수 있다.
  </li>
</ul>

```python
# 1. SQL을 사용해 처리하고 결과를 다시 DataFrame으로 반환.
spark.read.json("/opt/spark-data/data/flight-data/json/2015-summary.json")\
    .createOrReplaceTempView("some_sql_view")

spark.sql("""
SELECT DEST_COUNTRY_NAME, sum(count)
FROM some_sql_view GROUP BY DEST_COUNTRY_NAME
""")\
    .where("DEST_COUNTRY_NAME like 'S%'").where("`sum(count)` > 10")\
    .count()
```

<br>

<h2>4-3. 스파크 SQL 쓰리프트 JDBC/ODBC 서버</h2>
<ul>
  <li>
    Spark는 <strong>자바 데이터베이스 연결(Java Database Connectivity, JDBC) 인터페이스</strong>를 제공한다.
  </li>
  <li>
    사용자가 해당 인터페이스로 <strong>Spark 드라이버에 접속할 때</strong> 사용되며 태블로 또한 대표적인 예이다.
  </li>
  <li>
    JDBC/ODBC 서버를 시작하려면 Spark 디렉터리에 <strong>./sbin/start-thriftserver.sh</strong> 명령을 실행한다.
  </li>
    <ul>
      <li>
        해당 스크립트는 <strong>bin/spark-submit</strong> 스크립트에서 사용할 수 있는 모든 명령어 옵션을 지원한다.
      </li>
      <li>
        쓰리프트 서버 전체 옵션은 <strong>./sbin/start-thriftserver.sh --help </strong>명령을 통해 확인한다.
      </li>
      <li>
        쓰리프트 서버는 기본적으로 <strong>localhost:10000</strong> 주소를 사용한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>5. 카탈로그</h1>
<ul>
  <li>
    Spark SQL에서 <strong>가장 높은 추상화 단계</strong>는 카탈로그(Catalog)이다. 
  </li>
  <li>
    Catalog는 테이블에 저장된 데이터에 대한 <strong>메타데이터, 데이터베이스, 테이블, 함수 그리고 뷰</strong>에 대한 정보를 추상화한다.
  </li>
  <li>
    Catalog는 <strong>org.apache.spark.sql.catalog.Catalog</strong> 패키지로 사용할 수 있다.
  </li>
  <li>
    테이블, 데이터베이스 그리고 함수를 조회하는 등 여러 <strong>유용한 함수</strong>를 제공한다.
  </li>
</ul>

<br><br>

<h1>6. 테이블</h1>
<ul>
  <li>
    Spark SQL을 사용해 작업을 수행하려면 먼저 <strong>테이블을 정의</strong>해야 한다. 테이블은 <strong>명령을 실행할 데이터의 구조</strong>라는 점에서 <strong>DataFrame과 논리적으로 동일</strong>하다.
  </li>
  <li>
    DataFrame은 프로그래밍 언어로 정의하지만 <strong>테이블</strong>은 <strong>데이터베이스</strong>에서 정의한다.
  </li>
  <li>
    Spark에서 테이블을 생성하면 <strong>defaul 데이터베이스</strong>에 등록된다.
  </li>
  <li>
    Spark 2.x 버전에서 테이블은 항상 <strong>데이터</strong>를 갖고 있다.
  </li>
    <ul>
      <li>
        임시 테이블 개념이 없으며 <strong>데이터를 갖지 않는 뷰</strong>만 존재한다.
      </li>
      <li>
        테이블을 제거하면 <strong>모든 데이터가 제거</strong>되기에 조심해야 한다.
      </li>
    </ul>
</ul>

<br>

<h2>6-1. 스파크 관리형 테이블</h2>
<ul>
  <li>
    <strong>관리형 테이블</strong>과 <strong>외부 테이블</strong>은 반드시 기억해야할 개념이다.
  </li>
  <li>
    테이블은 두 가지 중요 정보를 저장한다. 하나는 <strong>테이블의 데이터</strong>이고 다른 하나는 테이블에 대한 <strong>메타데이터</strong>이다.
  </li>
  <li>
    <strong>디스크에 저장된 파일</strong>을 이용해 테이블을 정의하면 <strong>외부 테이블을 정의</strong>할 수 있다.
  </li>
  <li>
    DataFrame의 <strong>saveAsTable 메서드</strong>는 Spark가 관련된 모든 정보를 추적할 수 있는 <strong>관리형 테이블</strong>을 만들 수 있다.
  </li>
    <ul>
      <li>
        saveAsTable 메서드는 <strong>테이블을 읽고</strong>, 데이터를 <strong>Spark 포맷으로 변환</strong> 후 <strong>새로운 경로에 저장</strong>한다.
      </li>
      <li>
        <strong>하이브의 기본 웨어하우스 경로</strong>에 데이터를 저장한다. 데이터 저장 경로를 바꾸고 싶다면 <strong>SparkSession을 생성</strong>할 때 <strong>spark.sql.warehouse.dir 속성</strong>에 원하는 디렉터리 경로를 설정한다. (기본 저장 경로는 /user/hive/warehouse이다).
      </li>
      <li>
        지정 경로 하위에서 <strong>데이터베이스 목록</strong>을 확인할 수 있다.
      </li>
      <li>
        Spark는 <strong>데이터베이스 개념</strong>이 존재하며 <strong>show tables IN <databaseName> 쿼리</strong>를 통해 특정 데이터베이스의 테이블을 확인할 수도 있다.
      </li>
    </ul>
</ul>

<br>

<h2>6-2. 테이블 생성하기</h2>
<ul>
  <li>
    Spark는 SQL에서 전체 데이터소스 API를 <strong>재사용</strong>할 수 있는 기능을 지원한다. 따라서 테이블을 정의한 뒤에 테이블에 <strong>데이터를 적재</strong>할 필요가 없다.
  </li>
  <li>
    파일에서 데이터를 읽을 때에는 <strong>모든 종류의 정교한 옵션</strong>을 지정할 수도 있다. 
  </li>
  <li>
    Spark에 접속한 세션에서도 생성된 테이블을 사용할 수 있다. 임시 테이블 개념은 존재하지 않으며 대신 <strong>임시 뷰</strong>를 만들어 사용한다.
  </li>
</ul>

```python
# 1. 테이블 생성 후 파일을 받아와 데이터를 적재.
spark.sql("""
    CREATE TABLE flights (
        DEST_COUNTRY_NAME STRING,
        ORIGIN_COUNTRY_NAME STRING,
        count LONG
    )
    USING json
    OPTIONS (path '/opt/spark-data/data/flight-data/json/2015-summary.json')
""")

# 확인
spark.sql("SELECT * FROM flights LIMIT 5").show()

# < USING >
#   - USING으로 포맷을 지정하지 않으면 Spark는 기본적으로 하이브 SerDe 설정을 사용한다.
#   - 하이브 SerDe는 Spark 자체 직렬화보단 느리기 때문에 STORED AS 구문으로 하이브 테이
#     블을 생성할 수 있다.
```

```python
# 2. 특정 컬럼에 코멘트를 추가해 테이블을 생성.
spark.sql("""
    CREATE TABLE flights_csv (
        DEST_COUNTRY_NAME STRING,
        ORIGIN_COUNTRY_NAME STRING COMMENT "remember, the US will be most prevalent",
        count LONG)
    USING csv OPTIONS (header true, path '/opt/spark-data/data/flight-data/csv/2015-summary.csv')
""")
```

```python
# 3. SELECT 쿼리를 활용한 테이블 생성.
#   - 테이블이 없는 경우에만 생성하도록 지정할 수도 있다.
spark.sql("""
  CREATE TABLE flights_from_select
  USING parquet
  AS
  SELECT * FROM flights
""")

# 확인
spark.sql("SELECT * FROM flights_from_select LIMIT 5").show()
```

```python
# 4. 파티셔닝된 데이터셋을 저장해 데이터 에이아웃을 제어할 수 있다.
spark.sql("""
  CREATE TABLE partitioned_flights
  USING parquet
  PARTITIONED BY (DEST_COUNTRY_NAME)
  AS 
  SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME, count
  FROM flights
  LIMIT 5
""")

spark.sql("SELECT * FROM partitioned_flights LIMIT 5").show()
```

<br>

<h2>6-3. 외부 테이블 생성하기</h2>
<ul>
  <li>
    <strong>하이브 쿼리문을 Spark SQL로 변환</strong>해야하는 등의 상황에 <strong>외부 테이블</strong>을 생성하여 활용할 수 있다.
  </li>
  <li>
    Spark는 외부 테이블의 <strong>메타 데이터</strong>를 관리하지만 <strong>데이터 파일</strong>은 관리하지 않는다.
  </li>
  <li>
    <strong>CREATE EXTERNAL TABLE</strong> 구문을 통해 외부 테이블을 생성할 수 있다.
  </li>
</ul>

```python
# 1) 외부 테이블 생성 (Hive 구문)
spark.sql("""
  CREATE EXTERNAL TABLE IF NOT EXISTS hive_flights (
    DEST_COUNTRY_NAME STRING,
    ORIGIN_COUNTRY_NAME STRING,
    count LONG
  )
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  LOCATION 'file:/opt/spark-data/data/flights-data-hive/'
""")
```

```python
# 2) CTAS 외부 테이블 생성 (Hive 구문)
spark.sql("""
  CREATE EXTERNAL TABLE IF NOT EXISTS hive_flights_2
  ROW FORMAT DELIMITED
  FIELDS TERMINATED BY ','
  LOCATION 'file:/opt/spark-data/data/flight-data-hive/'
  AS
  SELECT * FROM flights
""")
```

<br>

<h2>6-4. 테이블에 데이터 삽입하기</h2>

```python
# 1. 데이터 삽입
spark.sql("""
    INSERT INTO flights_from_select
    SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME, count
    FROM flights
    LIMIT 20
""")
```

```python
# 2. 파티션 명세를 추가하여 특정 파티션에만 저장.
spark.sql("""
    PARTITION (DEST_COUNTRY_NAME=" UNITED STATES ")
    SELECT count, ORIGIN_COUNTRY_NAME 
    FROM flights
    WHERE DEST_COUNTRY_NAME=' UNITED STATES '
    LIMIT 12
""")
```

<br>

<h2>6-5. 테이블 메타데이터 확인하기</h2>
<ul>
  <li>
    테이블과 관련된 메타 데이터는 DESCRIBE 구문을 통해 확인할 수 있다.
  </li>
</ul>

```python
# 1. DESCRIBE를 통해 메타데이터 확인.
spark.sql("DESCRIBE TABLE flights_csv").show(truncate=False)
```

```python
# 2. 파티셔닝 스키마까지 확인.
spark.sql("SHOW PARTITIONS partitioned_flights").show(truncate=False)
```

<br>

<h2>6-6. 테이블 메타데이터 갱신하기</h2>
<ul>
  <li>
    테이블의 메타데이터를 유지하는 것은 가장 최신의 데이터셋을 읽고 있다는 것을 보장하는 중요한 작업이다.
  </li>
  <li>
    테이블의 메타데이터를 갱신할 수 있는 방법은 두 가지가 있다.
  </li>
    <ul>
      <li>
        REFRESH TABLE: 주로 변경할 때 사용.
      </li>
      <li>
        REPAIR TABLE: 주로 새로운 파티션을 생성할 때 사용.
      </li>
    </ul>
</ul>

```python
# 1. REGRESH TABLE을 통한 메타데이터 갱신
#   - 테이블과 관련된 모든 캐싱된 항복(기본적으로 파일)을 갱신한다.
#     - 이미 캐싱이 되어 있는 경우 다음번 스캔이 동작하는 시점에 다시 캐싱한다.
spark.sql("REFRESH TABLE partitioned_flights")
```

```python
# 2. REPAIR TABLE을 통한 메타데이터 갱신
#   - 카탈로그에서 관리하는 테이블의 파티션 정보를 새로 고친다.
#   - 새로운 파티션 정보를 수집하는 데 초점을 둔다.
#     - 예를 들어 신규 파티션을 만들 때 테이블을 수리(repair) 한다.
spark.sql("MSCK REPAIR TABLE partitioned_flights")
```

<br>

<h2>6-7. 테이블 제거하기</h2>
<ul>
  <li>
    테이블은 삭제(delete)할 수 없고, 오로지 <strong>제거(drop)</strong>할 수만 있다. 즉, 테이블 안의 데이터만 제거하는 것은 불가하고 <strong>테이블 자체</strong>만 삭제할 수 있다.
  </li>
</ul>

```python
# 1. 테이블 제거
spark.sql("DROP TABLE flights_csv")
```

```python
# 2. 테이블이 존재하는 경우에만 제거하도록 설정하여 제거.
spark.sql("DROP TABLE IF EXISTS flights_csv")
```

<h3>6-7-1. 외부 테이블 제거하기</h3>
<ul>
  <li>
    외부 테이블을 제거하면 <strong>데이터는 삭제되지 않지만</strong>, 더는 <strong>외부 테이블명</strong>을 이용해 <strong>데이터를 조회</strong>할 수 없다.
  </li>
</ul>

<br>

<h2>6-8. 테이블 캐싱하기</h2>

```python
# 1. 테이블을 캐시
spark.sql("CACHE TABLE flights")
```

```python
# 2. 캐시에서 제거
spark.sql("UNCACHE TABLE flights")
```

<br><br>

<h1>7. 뷰</h1>
<ul>
  <li>
    View는 기존 테이블에 여러 <strong>transformation</strong> 작업을 지정한다.
  </li>
  <li>
    기본적으로 View는 <strong>단순 쿼리 실행 계획</strong>일 뿐이다.
  </li>
  <li>
    View를 사용하면 쿼리 로직을 <strong>체계화</strong>하거나 <strong>재사용</strong>하기 편하게 만들 수 있다.
  </li>
  <li>
    View는 데이터베이스에서 설정하는 <strong>전역 뷰</strong>나 <strong>세션별 뷰</strong>가 될 수 있다.
  </li>
</ul>

<br>

<h2>7-1. 뷰 생성하기</h2>
<ul>
  <li>
    View는 결국 쿼리 정의(SQL 로직)만 저장하는 <strong>논리적 객체</strong>이다. 따라서 물리적으로 조회를 하면 <strong>DataFrame으로 반환</strong>된다.
  </li>
  <li>
    최종 사용자에게 뷰는 <strong>테이블</strong>처럼 보인다.
  </li>
  <li>
    신규 경로에 모든 데이터를 다시 저장하는 대신 단순하게 <strong>쿼리 시점</strong>에 데이터소스에 transformation을 수행한다.
  </li>
    <ul>
      <li>
        filter, select 또는 대규모 GROUP BY, ROLLUP 같은 transformation이 해당한다.
      </li>
    </ul>
</ul>

```python
# 1. 다음 목적지가 United States인 항공운항 데이터를 보기 위한 뷰 생성.
spark.sql("""
    CREATE VIEW just_usa_view AS
    SELECT *
    FROM flights
    WHERE DEST_COUNTRY_NAME = 'United States'
""")
```

```python
# 2. 데이터베이스에 등록하지 않고 현재 세션에서만 사용할 수 있는 임시 뷰 생성.
spark.sql("""
    CREATE TEMP VIEW just_usa_view_temp AS
    SELECT *
    FROM flights
    WHERE DEST_COUNTRY_NAME = 'United States'
""")
```

```python
# 3. 전역적 입시 뷰(global temp view) 생성
#   - 데이터베이스에 상관없이 사용할 수 있어 전체 Spark 애플리케이션에서 볼 수 있다.
#   - 세션이 종료되면 뷰도 사라진다.
spark.sql("""
    CREATE GLOBAL TEMP VIEW just_usa_global_view_temp AS
    SELECT *
    FROM flights
    WHERE DEST_COUNTRY_NAME = 'United States'
""")

# 현재 스키마의 테이블/뷰 목록 확인
spark.sql("SHOW TABLES").show(truncate=False)

# 글로벌 뷰는 항상 global_temp 스키마 아래에 저장됨
spark.sql("SHOW TABLES IN global_temp").show(truncate=False)
```

```python
# 4. keyword를 사용해 생성된 뷰 덮어쓰기.
#   - 임시 뷰와 일반 뷰 모두 덮어쓸 수 있다.
spark.sql("""
    CREATE OR REPLACE TEMP VIEW just_usa_view_temp AS
    SELECT *
    FROM flights
    WHERE DEST_COUNTRY_NAME = 'United States'
""")
```

```python
# 5. 생성한 뷰를 통해 다른 테이블과 동일하게 사용할 수 있다.
spark.sql("SELECT * FROM just_usa_view_temp").show()
```

```python
# 6. Spark DataFrame과 Spark SQL로 생성된 쿼리 실행 계획이 동일함을 확인.

# 6-1. DataFrame API===================
flights = (spark.read.format("json")
    .load("/opt/spark-data/data/flight-data/json/2015-summary.json"))
# DataFrame API로 필터링 (주의: 'United States' 오타 수정)
just_usa_df = flights.where("DEST_COUNTRY_NAME = 'United States'")
# 실행 계획 확인
just_usa_df.selectExpr("*").explain()

# 6-2. SQL Query
spark.sql("SELECT * FROM just_usa_view").explain()
spark.sql("SELECT * FROM flights WHERE dest_country_name = \
'United Status'").explain()
```

<br>

<h2>7-2. 뷰 제거하기</h2>
<ul>
  <li>
    테이블을 제거하는 방식과 동일하며 제거 대상을 테이블이 아닌 <strong>뷰</strong>로 지정만 하면 된다.
  </li>
</ul>

```python
spark.sql("DROP VIEW IF EXISTS just_usa_view")
```

<br><br>

<h1>8. 데이터베이스</h1>
<ul>
  <li>
    데이터베이스는 <strong>여러 테이블을 조직화</strong>하기 위한 도구이다.
  </li>
  <li>
    데이터베이스를 정의하지 않으면 Spark는 기본 데이터베이스를 사용한다.
  </li>
  <li>
    실행하는 모든 SQL 명령문은 <strong>사용 중인 데이터베이스 범위</strong>에서 실행된다.
  </li>
    <ul>
      <li>
        데이터베이스를 <strong>변경</strong>하고 <strong>기존 데이터를 조회</strong>하려면 <strong>다르게 쿼리</strong>를 해야한다.
      </li>
      <li>
        동료와 동일한 컨텍스트나 세션을 공유하는 경우 혼란을 일으킬 수 있기에 데이터베이스를 설정하는 것이 좋다.
      </li>
    </ul>
</ul>

```python
# 1. 전체 데이터베이스 목록 확인.
spark.sql("SHOW DATABASES").show(truncate=False)
```

```python
# 2. 데이터베이스 생성하기.
spark.sql("CREATE DATABASE some_db")
```

<br>

<h2>8-2. 데이터베이스 설정하기</h2>

```python
# 2. USE 
```