<ul>
  <li>
    Spark의 <strong>저수준 API</strong>는 <strong>RDD</strong>, <strong>SparkContext</strong> 그리고 accumulator와 broadcast variable과 같은 <strong>분산형 공유 변수(distributed shared variables)</strong> 등을 의미한다.
  </li>
</ul>

<br><br>

<h1>1. 저수준 API란</h1>
<ul>
  <li>
    Spark에는 두 종류의 저수준 API가 있다.
  </li>
    <ul>
      <li>
        분산 데이터 처리를 위한 <strong>RDD</strong>
      </li>
      <li>
        broadcast와 accumulator처럼 <strong>분산형 공유 변수</strong>를 배포하고 다루기 위한 API
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 저수준 API는 언제 사용할까</h2>
<ul>
  <li>
    다음과 같은 상황에서 저수준 API를 사용한다.
  </li>
    <ul>
      <li>
        <strong>고수준 API에서 제공하지 않는 기능</strong>이 필요한 경우. (e.g. 클러스터의 물리적 데이터의 배치를 아주 세밀하게 제어해야하는 등).
      </li>
      <li>
        <strong>RDD</strong>를 사용해 개발된 <strong>기존 코드를 유지</strong>해야 하는 경우.
      </li>
      <li>
        사용자가 정의한 <strong>공유 변수</strong>를 다뤄야하는 경우.
      </li>
    </ul>
  <li>
    Spark의 모든 워크로드는 저수준 기능을 사용하는 <strong>기초적인 형태로 컴파일</strong> 되기에 이해해 두는 것이 좋다.
  </li>
  <li>
    하지만 Spark를 잘 아는 개발자라 하더라도 <strong>구조적 API 위주</strong>로 사용하는 것이 좋다.
  </li>
    <ul>
      <li>
        저수준 API는 세밀한 제어 방법을 제공하여 개발자가 치명적인 실수를 하지 않도록 도와준다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 저수준 API는 어떻게 사용할까</h2>
<ul>
  <li>
    <strong>SparkContext</strong>는 저수준 API 기능을 사용하기 위한 <strong>진입점</strong>이다.
  </li>
  <li>
    스파크 클러스터에서 연산을 수행하는 데 필요한 도구인 <strong>SparkSession</strong>을 이용해 SparkContext에 접근할 수 있다.
  </li>
</ul>

```python
spark.sparkContext
```

<br><br>

<h1>2. RDD 개요</h1>
<ul>
  <li>
    RDD는 Spark 1.x 버전의 핵심 API이다. 2.x에서는 사용할 수는 있지만 잘 사용하지는 않는다.
  </li>
  <li>
    사용자가 실행한 모든 DataFrame이나 Dataset 코드는 <strong>RDD로 컴파일</strong> 된다. (Job도 포함).
  </li>
  <li>
    RDD는 <strong>불변성</strong>을 가지며 <strong>병렬</strong>로 처리할 수 있는 <strong>파티셔닝된 레코드의 모음</strong>이다.
  </li>
  <li>
    DataFrame의 각 레코드는 스키마를 알고 있는 필드로 구성된 <strong>구조화된 로우</strong>인 반면, RDD의 레코드는 프로그래머가 선택하는 Java, Scala, python의 <strong>객체</strong>일 뿐이다.
  </li>
  <li>
    RDD의 모든 레코드는 Java 혹은 python <strong>객체</strong>이기에 <strong>완벽히 제어</strong>할 수 있다.
  </li>
    <ul>
      <li>
        개발자는 제어권을 갖을 수 있지만 모든 값을 다루거나 값 사이의 상호작용 과정을 수동으로 정의해야한다. 즉, 어떤 처리를 하더라도 <strong>바퀴를 다시 발명</strong> 해야한다.
      </li>
    </ul>
  <li>
    구조적 API와는 다르게 레코드 내부 구조를 Spark가 파악할 수 없어 <strong>최적화에도 많은 수작업</strong>이 필요하다. (약간 python을 사용하다 C를 쓰는 느낌).
  </li>
  <li>
    RDD API는 Dataset과 유사하지만 <strong>데이터를 저장하거나 다루지 않는다</strong>.
  </li>
  <li>
    RDD와 Dataset 사이의 전환은 쉽기 때문에 <strong>두 API를 모두 사용</strong>해 각 API의 장점을 활용할 수 있다.
  </li>
</ul>

<br>

<h2>2-1. RDD 유형</h2>
<ul>
  <li>
    사용자는 두 가지 타입의 RDD를 만들 수 있다. 하나는 <strong>제네릭 RDD 타입</strong>이고, 다른 하나는 키 기반의 집계 가능한 <strong>key-value RDD</strong> 이다.
  </li>
  <li>
    두 RDD 타입 모두 객체의 컬렉션을 표현하지만 <strong>key-value RDD</strong>는 <strong>특수 연산</strong>뿐만 아니라 <strong>key를 이용한 사용자 지정 파티셔닝 개념</strong>을 포함하고 있다.
  </li>
  <li>
    RDD는 다섯 가지 주요 속성이 있으며 <strong>각 속성에 대한 구현체</strong>를 갖고 있다.
  </li>
    <ul>
      <li>
        <strong>파티션의 목록</strong>
      </li>
      <li>
        <strong>각 조각을 연산하는 함수</strong>
      </li>
      <li>
        <strong>다른 RDD와의 의존성 목록</strong>
      </li>
      <li>
        <strong>부가적으로 key-value RDD를 위한 Partitioner (RDD는 해시 파티셔닝 되어 있음)</strong>
      </li>
      <li>
        <strong>부가적으로 각 조각을 연산하기 위한 기본 위치 목록 (하둡 분산 파일 시스템 파일의 블록 위치)</strong>
      </li>
    </ul>
  <li>
    RDD 또한 데이터를 다루는 데 필요한 <strong>지연 처리 방식의 transformation</strong>과 <strong>즉시 실행 방식의 action</strong>을 제공한다.
  </li>
    <ul>
      <li>
        동작 방식은 동일하지만 <strong>row의 개념이 없다</strong>.
      </li>
      <li>
        개별 레코드는 <strong>Java, Scala, python 객체</strong>일 뿐이며 구조적 API에서 제공하는 여러 함수를 사용할 수 없어 <strong>수동처리</strong>해야 한다.
      </li>
    </ul>
  <li>
    RDD API는 python에서도 사용할 수 있다. 단, <strong>Java와 Scala가 아닌 경우</strong>, <strong>원형(순환 참조) 객체</strong>를 다루는 경우, <strong>python을 사용하는 경우</strong> 성능 하락이 발생한다. 따라서 가능한 <strong>구조적 API</strong>를 사용하는 것이 좋다.
  </li>
</ul>

<br>

<h2>2-2. RDD는 언제 사용할까</h2>
<ul>
  <li>
    정말 필요한 경우가 아니라면 수동으로 RDD를 생성하면 안 된다.
  </li>
    <ul>
      <li>
        RDD의 강점에도 불구하고 구조적 API가 제공하는 <strong>최적화 기법</strong>을 사용할 수 없다.
      </li>
      <li>
        <strong>DataFrame</strong>이 RDD보다 <strong>효울적이고 안정적이며 표현력</strong>이 좋다.
      </li>
    </ul>
  <li>
    <strong>물리적으로 분산된 데이터(자체 구성 데이터 파티셔닝)</strong>에 세부적인 제어가 필요할 때 RDD를 사용.
  </li>
</ul>

<br>

<h2>2-3. Dataset과 RDD의 케이스 클래스</h2>
<ul>
  <li>
    <strong>Dataset</strong>은 RDD와 다르게 구조적 API가 제공하는 많은 <strong>기능</strong>과 <strong>최적화 기법</strong>을 제공한다는 차이가 존재한다.
  </li>
</ul>

<br><br>

<h1>3. RDD 생성하기</h1>
<h2>3-1. DataFrame, Dataset으로 RDD 생성하기</h2>
<ul>
  <li>
    <strong>기존에 사용하던</strong> DataFrame이나 Dataset의 <strong>rdd 메서드를 호출</strong>하면 쉽게 RDD로 변활할 수 있다.
  </li>
  <li>
    <strong>Row 타입</strong>은 Spark가 <strong>구조적 API</strong>에서 <strong>데이터를 표현</strong>하는 데 사용하는 <strong>내부 카탈리스트 포맷</strong>이다.
  </li>
  <li>
    <strong>rdd 메서드</strong>는 <strong>Row 타입을 갖는 RDD</strong>를 생성한다. 해당 기능을 사용하여 상황에 따라 구조적 API와 저수준 API를 오고가게 만들 수 있다.
  </li>
  <li>
    RDD API와 Dataset API는 편리한 기능을 제공하지 않는 인터페이스로 유사하게 느껴질 수 있다.
  </li>
</ul>

```python
# 1. rdd 메서드를 통해 RDD 반환.
#   - python은 DataFrame만 존재하기에 Row 타입의 RDD가 된다.
spark.range(10).rdd
```

```python
# 2. 1번에서 만들어진 데이터 처리하는 두 가지 방법
#   - Row 객체를 올바른 데이터 타입으로 변환
#   - Row 객체에서 값을 추출
spark.range(10).toDF("id").rdd.map(lambda row: row[0])

# Row 타입을 갖는 RDD 반환
```

```python
# 3. RDD를 사용해 DataFrame이나 Dataset을 생성할 때에도 RDD의 toDF 메서드를 호출한다.
spark.range(10).rdd.toDF()
```

<br>

<h2>3-2. 로컬 컬렉션으로 RDD 생성하기</h2>
<ul>
  <li>
    컬렉션 객체를 <strong>RDD</strong>로 만들기 위해서는 (SparkSession 내부의) sparkContext의 <strong>parallelize 메서드</strong>를 호출해야 한다.
  </li>
  <li>
    <strong>parallelize 메서드</strong>는 단일 노드에 있는 컬렉션을 <strong>병렬 컬렉션</strong>으로 전환하며 <strong>파티션 수</strong>를 명시적으로 지정할 수 있다.
  </li>
</ul>

```python
# 1. 두 개의 파티션을 갖는 컬렉션 객체 생성.
myCollection = "Spark The Definitive Guide : Big Data Processing Mode Simple"\
    .split(" ")
words = spark.sparkContext.parallelize(myCollection, 2)
```

```python
# 2. RDD에 이름을 지정하면 Spark UI에 지정한 이름으로 RDD가 표시된다.
words.setName("myWords")
words.name()
```

<br>

<h2>3-3. 데이터소스로 RDD 생성하기</h2>
<ul>
  <li>
    데이터소스를 통해 RDD를 생성할 때에는 DataSource API를 사용하는 것이 바람직하다.
  </li>
    <ul>
      <li>
        데이터소스<br>
        → DataSource API(DataFrame으로 읽기)<br>
        → .rdd 변환<br>
        → RDD 연산(map, flatMap, ...)<br>
        → 최적화 반영
      </li>
    </ul>
  <li>
    생성된 RDD에서 <strong>파일명</strong>은 첫 번째 객체인 <strong>RDD의 key</strong>가 되고, <strong>텍스트 파일의 value</strong>는 두 번째 문자열 객체인 <strong>RDD의 value</strong>가 된다.
  </li>
</ul>

```python
# 1. sparkContext를 사용해 데이터를 RDD로 읽기.
#    - 줄 단위로 텍스트 파일을 읽는다.
spark.sparkContext.textFile("/some/path/withTextFiles")
```

```python
# 2. 텍스트 파일 하나를 레코드로 읽는 경우
spark.sparkContext.wholeTextFiles("/some/path/withTextFiles")
```

<br><br>

<h1>4. RDD 다루기</h1>
<ul>
  <li>
    RDD는 DataFrame과 다루는 방식이 비슷하다. 그러나 RDD는 Java 혹은 Scala의 객체를 다루고, 헬퍼 메서드나 함수도 DataFrame에 비해 많이 부족하기에 <strong>사용자가 직접 정의할 것들</strong>이 많다.
  </li>
</ul>

<br><br>

<h1>5. 트랜스포메이션</h1>
<ul>
  <li>
    대부분의 RDD transformation은 <strong>구조적 API</strong>에서 사용할 수 있는 기능 갖고 있다.
  </li>
  <li>
    DataFrame이나 Dataset과 동일하게 RDD에 <strong>transformation을 지정</strong>해 <strong>새로운 RDD</strong>를 생성할 수 있다.
  </li>
  <li>
    RDD를 생성할 때 RDD에 포함된 데이터를 다루는 함수에 따라 <strong>다른 RDD에 대한 의존성</strong>도 함께 정의한다.
  </li>
</ul>

<br>

<h2>5-1. distinct</h2>

```python
# 1. RDD의 distinct 메서드를 호출하면 RDD에서 중복된 데이터를 제거한다.
#   - 정확히는 RDD에 중복제거 설계도를 넣는 것 (RDD는 데이터를 저장하지 않기 때문).
words.distinct().count()
```

<br>

<h2>5-2. filter</h2>
<ul>
  <li>
    필터링은 <strong>SQL의 where 조건절</strong>을 생성하는 것과 비슷하다. RDD의 <strong>레코드를 모두 확인</strong>하고 <strong>조건 함수를 만족</strong>하는 레코드만 반환하다.
  </li>
  <li>
    조건 함수는 필터 함수로 동작하기에 <strong>불리언 타입을 반환</strong>해야 한다.
  </li>
  <li>
    <strong>모든 row</strong>는 어떤 경우라도 <strong>입력값</strong>을 갖고 있어야 한다.
  </li>
</ul>

```python
# 1. 문자 'S'로 시작하는 단어만 남도록 RDD를 필터링
def startsWithS(individual):
    return individual.startwith("S")
```

```python
# 2. 함수는 RDD의 각 레코드를 개별적으로 처리한다.
#   - RDD의 각 레코드를 개별적으로 처리한다.
words.filter(lambda word: startsWithS(word)).collect()

# 결과는 Spark를 사용한 데이터 타입으로 반환된다.
#   - 데이터를 Row 타입으로 강제 변환하거나 데이터를 수집한 다음 변환할 필요가 없기 때문.
```

<br>

<h2>5-3. map</h2>
<ul>
  <li>
    11장과 동일한 작업을 한다. 주어진 입력을 <strong>원하는 값으로 변환</strong>하는 함수를 명시하고 <strong>레코드별로 적용</strong>한다.
  </li>
</ul>

```python
# 1. 매핑 함수 설정.
#   - word: 단어
#   - word[0]: 단어의 시작 문자
#   - word.startswith("S"): 첫 문자가 S인지 아닌지
words2 = words.map(lambda word: (word, word[0], word.startswith("S")))
```

```python
# 2. 매핑 적용
words2.filter(lambda record: record[2]).take(5)
```

<h3>5-3-1. flatMap</h3>
<ul>
  <li>
    map은 단일 row를 반환하는 반면 <strong>flatMap</strong>은 <strong>여러 row를 반환</strong>할 때 사용한다.
  </li>
  <li>
    flatMap은 확장 가능한 <strong>map 함수의 출력</strong>을 <strong>반복 처리</strong>할 수 있는 형태로 반환한다.
  </li>
</ul>

```python
# 1. flatMap을 활용한 함수 적용
words.flatMap(lambda word: list(word)).take(5)
```

<br>

<h2>5-4. sortBy</h2>
<ul>
  <li>
    다른 RDD 작업과 마찬가지로 함수를 지정해 RDD의 데이터 객체에서 값을 추출한 뒤 값을 기준으로 정렬한다.
  </li>
</ul>

```python
# 1. sortBy를 통한 값 정렬
words.sortBy(lambda word: len(word) * -1).take(2)
```

<br>

<h2>5-5. randomSplit</h2>
<ul>
  <li>
    RDD를 임의로 분할해 <strong>RDD 배열을 생성</strong>한다. 가중치와 난수 시드(random seed)로 구성된 <strong>배열을 파라미터</strong>로 사용한다.
  </li>
</ul>

```python
# 2. randomSplit을 활용하여 RDD 배열 생성.

# randomSplit은 여러 개의 RDD를 리스트로 반환
fiftyFiftySplit = words.randomSplit([0.5, 0.5])

# 첫 번째 분할 RDD
rdd1 = fiftyFiftySplit[0]

# 두 번째 분할 RDD
rdd2 = fiftyFiftySplit[1]
```

<br><br>

<h1>6. 액션</h1>
<ul>
  <li>
    RDD 또한 transformation 연산을 시작하기 위해 <strong>action</strong>을 사용한다.
  </li>
  <li>
    Action은 데이터를 <strong>드라이버로 모으</strong>거나 <strong>외부 데이터소스</strong>로 내보낼 수 있다.
  </li>
</ul>

<br>

<h2>6-1. reduce</h2>
<ul>
  <li>
    RDD의 모든 값을 <strong>하나의 값</strong>으로 만들 때에는 <strong>reduce 메서드</strong>를 사용한다.
  </li>
</ul>

```python
# 1. 두 수 입력값을 하나로 줄이는 함수로 합계 구하기.
spark.sparkContext.parallelize(range(1, 21)).reduce(lambda x, y: x + y)
```

```python
# 2. 단어 집합에서 가장 긴 단어 찾기.
def wordLengthReducer(leftWord, rightWord):
    if len(leftWord) > len(rightWord):
        return leftWord
    else:
        return rightWord

words.reduce(wordLengthReducer)
```

<br>

<h2>6-2. count</h2>

```python
# 1. count 함수를 통해 RDD의 전체 로우 확인.
words.count()
```

<h3>6-2-1. countApprox</h3>
<ul>
  <li>
    <strong>count 함수의 근가치</strong>를 <strong>제한 시간 내에</strong> 계산하는 함수이다. (제한 시간을 초과하면 불완전한 결과를 반환할 수도 있다).
  </li>
  <li>
    <strong>신뢰도(confidence)</strong>는 실제로 연산한 결과와의 <strong>오차율</strong>을 의미하며 countApprox 메서드의 <strong>신뢰도를 0.9</strong>로 설정하고 반복하면 실제 연산과 동일한 값이 <strong>90% 이상 포함</strong>될 것으로 기대할 수 있다.
  </li>
  <li>
    신뢰도는 0과 1사이의 값이어야하며 범위를 벗어나면 오류를 예외가 발생한다.
  </li>
</ul>

```python
# 2. countApprox를 통한 count 함수의 근사치 출력.
confidence = 0.95
timeoutMilliseconds = 400

# countApprox(timeout, confidence)
approx_count = words.countApprox(timeoutMilliseconds, confidence)

print(approx_count)
```

<h3>6-2-2. countApproxDistinct</h3>
<ul>
  <li>
    버전 차이로 인해 내용과 실습 코드에 차이가 있다. <strong>실습 코드가 최신 버전</strong>이다.
  </li>
  <li>
    countApproxDistinct 메서드에는 두 가지 구현체가 있다.
  </li>
  <li>
    <strong>첫 번째 구현체</strong>는 <strong>상대 정확도(relative accuracy)</strong>를 파라미터로 사용한다.
  </li>
    <ul>
      <li>
        값을 <strong>작게</strong> 설정하면 <strong>더 많은 메모리 공간을 사용</strong>하는 카운터가 생성된다.
      </li>
      <li>
        설정값은 반드시 <strong>0.000017</strong>보다 커야한다.
      </li>
    </ul>
  <li>
    <strong>두 번째 구현체</strong>를 사용하면 동작을 <strong>세부적</strong>으로 제어할 수 있다.
  </li>
    <ul>
      <li>
        상대 정확도를 지정할 때 <strong>두 개의 파라미터</strong>를 사용한다.
      </li>
      <li>
        하나는 <strong>일반(regular) 데이터</strong>를 위한 파라미터이고, 다른 하나는 <strong>희소 표현</strong>을 위한 파라미터이다.
      </li>
      <li>
        <strong>p는 정밀도</strong>를, <strong>sp는 희소 정밀도</strong>를 의미한다.
      </li>
      <li>
        <strong>카디널리티가 작을 때 0이 아닌 값(sp > p)</strong>을 설정하면 <strong>메모리 소비</strong>를 줄이면서 <strong>정확도</strong>를 증가시킬 수 있다.
      </li>
      <li>
        두 파라미터 모두 <strong>정수 데이터 타입</strong>을 사용한다.
      </li>
    </ul>
</ul>

```python
# RDD API → 정수 precision만
words.countApproxDistinct(10)

# DataFrame API → rsd(실수) 전달 가능
df.select(F.approx_count_distinct("word", 0.05)) 
```

<h3>6-2-3. countByValue</h3>
<ul>
  <li>
    countByValue 메서드는 RDD 값의 개수를 반환한다.
  </li>
  <li>
    결과 데이터셋을 드라이버 메모리로 읽어들여 처리한다. 따라서 결과가 작은 경우에만 사용해야 한다. (전체 row 수나 고유 아이템의 수가 적은 경우).
  </li>
</ul>

```python
# 1. countByValue로 RDD 값의 수 반환
words.countByValue()
```

<h3>6-2-4. countByValueApprox</h3>
<ul>
  <li>
    count 함수와 동일한 연산을 수행하지만 근사치를 계산한다.
  </li>
  <li>
    countByValueApprox는 count 함수와 동일한 연산을 수행하지만 근사치 계산을 반환한다.
  </li>
  <li>
    countByValueApprox 함수는 지정된 제한 시간(첫 번째 파라미터) 내에 처리하지 못한다면 불완전한 값을 반환한다.
  </li>
  <li>
    countByValueApprox 함수는 신뢰도를 인자로 줄 수 있다. 신뢰도는 [0, 1] 범위를 갖는다.
  </li>
</ul>

```python
# 1. countByValueApprox를 count 함수의 근사치 반환
# (pyspark에서는 다른 방식으로 해야 한다).
words.countByValueApprox(1000, 0.95)
```

<br>

<h2>6-3. first</h2>

```python
# 1. first 메서드는 데이터 셋의 첫 번째 값을 반환한다.
words.first()
```

<br>

<h2>6-4. max와 min</h2>

```python
# 1. max()를 통해 최댓값 반환.
rdd = spark.sparkContext.parallelize(range(1, 21))
result = rdd.max()
print(result)
```

```python
# 2. min()을 통한 최솟값 반환.
rdd = spark.sparkContext.parallelize(range(1, 21))
result = rdd.min()
print(result)
```

<br>

<h2>6-5. take</h2>
<ul>
  <li>
    take와 take의 파생 메서드는 <strong>RDD에서 가져올 값의 개수</strong>를 파라미터로 사용한다.
  </li>
  <li>
    take는 <strong>하나의 파티션</strong>을 스캔한 뒤 해당 파티션의 <strong>결과 수</strong>를 이용해 <strong>파라미터로 지정된 값</strong>을 만족하는 데 필요한 <strong>추가 파티션 수를 예측</strong>한다.
  </li>
  <li>
    takeOrdered, takeSample 그리고 top과 같은 <strong>유사 함수</strong>들이 존재한다.
  </li>
</ul>

```python
# 1. words: RDD

# 앞에서 5개
print(words.take(5))

# 정렬된 상태로 앞 5개
print(words.takeOrdered(5))

# 정렬된 상태로 뒤 5개 (내림차순 기준)
print(words.top(5))

# 샘플링
withReplacement = True
numberToTake = 6
randomSeed = 100

print(words.takeSample(withReplacement, numberToTake, randomSeed))
```

<br><br>

<h1>7. 파일 저장하기</h1>
<ul>
  <li>
    파일 저장은 <strong>데이터 처리 결과</strong>를 <strong>일반 텍스트 파일</strong>로 쓰는 것을 의미한다.
  </li>
  <li>
    RDD를 사용하면 일반적인 의미의 데이터소스를 저장할 수 없다. 각 파티션의 내용을 저장하기 위해서는 <strong>전체 파티션을 순회</strong>하면서 <strong>외부 데이터베이스에 저장</strong>해야 한다.
  </li>
    <ul>
      <li>
        해당 방식은 고수준 API의 내부 처리를 저수준 API로 구현하는 접근법이다.
      </li>
    </ul>
  <li>
    Spark는 각 파티션의 데이터를 <strong>파일</strong>로 저장한다.
  </li>
</ul>

<br>

<h2>7-1. savaAsTextFile</h2>

```scala
// 1. 경로를 지정하여 텍스트 파일로 저장.
words.saveAsTextFile("file:/tmp/bookTitle")
```

```scala
// 2. 압축 코덱을 활용하여 텍스트 파일로 저장.
import org.apache.hadoop.io.compress.BZip2Codec\

words.saveAsFile("file:/tmp/bookTitleCompressed", classOf[BZip2Codec])
```

<br>

<h2>7-2. 시퀀스 파일</h2>
<ul>
  <li>
    Spark는 <strong>하둡 에코시스템</strong>을 기반으로 했기에 다양한 하둡 기능과 잘 호환된다.
  </li>
  <li>
    시퀀스 파일은 <strong>바이너리 key-value</strong>로 구성된 플랫 파일이며, <strong>MapReduce의 입출력 포맷</strong>으로 널리 사용된다.
  </li>
</ul>

```scala
// 1. saveAsObjectFile 메서드로 시퀀스 파일 작성.
words.saveAsObjectFile("/tmp/my/sequenceFilePath")
```

<br>

<h2>7-3. 하둡 파일</h2>
<ul>
  <li>
    데이터를 저장하는 데 사용할 수 있는 여러 <strong>하둡 파일 포맷</strong>이 존재하고, 하둡 파일 포맷을 사용하면 <strong>클래스</strong>, <strong>출력 포맷</strong>, <strong>하둡 설정</strong> 그리고 <strong>압축 방식</strong>을 지정할 수 있다.
  </li>
  <li>
    하둡 파일 포맷은 <strong>하둡 에코시스템</strong>이나 기존의 <strong>MapReduce Job</strong>을 깊이 있게 다루는 경우가 아니라면 크게 의미 없다.
  </li>
</ul>

<br><br>

<h1>8. 캐싱</h1>
<ul>
  <li>
    RDD 캐싱에도 <strong>DataFrame이나 Dataset의 캐싱과 동일한 원칙</strong>이 적용되며 RDD를 <strong>캐시</strong>하거나 <strong>저장(persist)</strong>할 수 있다.
  </li>
  <li>
    기본적으로 캐시와 저장은 <strong>메모리</strong>에 있는 데이터만을 대상으로 한다.
  </li>
</ul>

```scala
// 1. RDD 캐시
words.cache()
```

```python
// 2. org.apache.spark.storage.StorageLevel 속성을 통해 저장소 수준을 지정하여 활용.
words.getStorageLevel()
```

<br><br>

<h1>9. 체크포인팅</h1>
<ul>
  <li>
    체크포인팅(checkpointing)은 DataFrame API에서 사용할 수 없는 중 하나이다.
  </li>
  <li>
    체크 포인팅은 RDD를 <strong>디크스에 저장</strong>하는 방식이다. 따라서 나중에 저장된 RDD를 참조할 때 디스크에 저장된 <strong>중간 결과 파티션</strong>을 참조한다.
  </li>
  <li>
    메모리에 저장하지 않고 <strong>디스크에 저장</strong>한다는 사실만 제외하면 <strong>캐싱과 유사</strong>하다.
  </li>
  <li>
    해당 기능은 <strong>반복적인 연산</strong> 수행 시 매우 유용하다.
  </li>
</ul>

```scala
// 1. 체크포인팅 활용.
spark.sparkContext.setCheckpointDir("/some/path/for/checkpointing")
words.checkpoint()

// 이제 words RDD를 참조하면 데이터소스 대신 체크포인트에 저장된 RDD를 사용한다.
```

<br><br>

<h1>10. RDD를 시스템 명령으로 전송하기</h1>
<ul>
  <li>
    <strong>pipe 메서드</strong>를 사용하면 <strong>파이핑 요소로 생성된 RDD</strong>를 <strong>외부 프로세스로 전달</strong>할 수 있다.
  </li>
  <li>
    외부 프로세스는 파티션마다 <strong>한 번씩</strong> 처리해 결과 RDD를 생성한다.
  </li>
  <li>
    각 입력 파티션의 모든 요소는 <strong>개행 문자 단위</strong>로 분할되어 <strong>여러 줄의 입력 데이터</strong>로 변경된 후 프로세스의 <strong>표준 입력(stdin)에 전달</strong>된다.
  </li>
  <li>
    결과 파티션은 프로세스의 <strong>표준 출력(stdout)으로 생성</strong>된다. 표준 출력의 각 줄은 <strong>파티션 하나의 요소</strong>가 되며 <strong>비어 있는 파티션</strong>을 처리할 때도 프로세스는 실행된다.
  </li>
  <li>
    사용자가 정의한 두 함수를 인수로 전달하면 <strong>출력 방식</strong>을 원하는 대로 변경할 수 있다.
  </li>
</ul>

```scala
// 1. 각 파티션을 wc 명령에 연결. 
//   - 각 row는 신규 row로 전달되므로 row 수를 세면 각 파이션 별 row 수를 알 수 있다.
words.pipe("wc -l").collect()
```

<br>

<h2>10-1. mapPartition</h2>
<ul>
  <li>
    <strong>mapPartitions</strong>는 클러스터에서 <strong>물리적인 단위로 개별 파티션을 처리</strong>하기 때문에 <strong>개별 파티션에 대해 map 연산</strong>을 수행할 수 있다.
  </li>
  <li>
    <strong>mapPartition</strong> 메서드는 기본적으로 <strong>파티션 단위</strong>로 작업을 수행한다.
  </li>
    <ul>
      <li>
        파티션 단위로 작업을 수행하기에 <strong>전체 파티션에 대한 연산</strong>을 수행할 수 있다. (RDD의 전체 하위 데이터셋에 원하는 연사이 가능하기에 매우 유용).
      </li>
      <li>
        파티션 그룹의 전체 값을 단일 파티션으로 모든 <strong>다음 임의의 함수</strong>를 적용하고 제어할 수 있다.
      </li>
    </ul>
  <li>
    <strong>mapPartitionsWithIndex</strong> 같이 mapPartitions와 유사한 기능을 제공하는 함수가 있다.
  </li>
    <ul>
      <li>
        해당 함수를 사용하기 위해서는 <strong>Index</strong>와 <strong>partition의 모든 아이템</strong>을 순회하는 이터레이터를 가진 함수를 인수로 지정해야 한다.
      </li>
      <li>
        Partition의 index는 <strong>RDD의 파티션 번호</strong>이다.
      </li>
      <li>
        <strong>파티션 인덱스</strong>를 사용해 각<strong>레코드가 속한 데이터셋</strong>이 어디에 있는지 알아 낼 수 있으며 <strong>디버깅</strong>에 정보를 활용할 수 있다.
      </li>
      <li>
        <strong>map 함수가 정상적으로 동작</strong>하는지 시험해 볼 수 있다.
      </li>
    </ul>
</ul>

```python
# 1. 모든 파티션에 '1' 값을 생성하고, 표현식에 따라 파티션 수를 카운트하여 합산.
words.mapPartitions(lambda part: [1]).sum()
```

```python
# 2. mapPartitionsWithIndex를 활용하여 map 연산 수행
def indexedFunc(partitionIndex, withinPartIterator):
    return ["partition: {} => {}".format(partitionIndex, x) for x in withinPartIterator]

words.mapPartitionsWithIndex(indexedFunc).collect()
```

<br>

<h2>10-2. foreachPartition</h2>
<ul>
  <li>
    foreachPartition 함수는 파티션의 모든 데이터를 순회만하고 결과를 반환하지 않는다. (mapPartitions는 결과를 반환).
  </li>
  <li>
    foreachPartition은 개별 파티션에서 특정 작업을 수행하는 데 매우 적합하다.
  </li>
</ul>

```scala
// 1. 임의로 생성한 ID를 이용해 임시 디렉터리에 결과를 저장하는 텍스트 파일 소스 구현.
words.foreachPartition { iter => 

  import java.io._
  import scala.util.Random
  
  val randomFileName = new Random().nextInt()
  val pw = new PrintWrtier(new File(s"/tmp/random-flie-${randomFileName}.txt"))
  
  while (iter.hasNext) {
    pw.write(iter.next())
  }
  pw.close()
}
```

<br>

<h2>10-3. glom</h2>
<ul>
  <li>
    glom 함수는 데이터섯의 모든 파티션을 <strong>배열</strong>로 변환한다.
  </li>
  <li>
    데이터를 <strong>드라이버로 모으고</strong> 데이터가 존재하는 파티션이 <strong>배열이 필요한 경우</strong> 유용하다.
  </li>
    <ul>
      <li>
        단, 파티션이 <strong>크거나</strong> 파티션의 <strong>수가 많다면</strong> 드라이버가 비정상적으로 종료될 수 있다.
      </li>
    </ul>
</ul>

```python
# 1. 입력된 단어를 두 개의 파티션에 개별적으로 할당.
spark.sparkContext.parallelize(["Hello", "World"], 2).glom().collect()
```