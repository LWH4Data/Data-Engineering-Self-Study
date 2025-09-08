<ul>
  <li>
    key-value 형태의 RDD를 중심으로 RDD 고급 연산을 배운다.
  </li>
  <li>
    사용자 정의 파티션에 대해 배우며, 사용자 정의 파티션을 사용할 경우 클러스터에 데이터가 배치괴는 방식을 정확히 제어할 수 있고 개별 파티션을 다룰 수 있다.
  </li>
  <li>
    세 가지 중심 주제
  </li>
    <ul>
      <li>
        집계와 key-value 형태의 RDD
      </li>
      <li>
        사용자 정의 파티셔닝
      </li>
      <li>
        RDD 조인
      </li>
    </ul>
</ul>

```python
# 1. 이번 장의 실습 또한 이전 장의 데이터를 그대로 활용한다.
myCollection = "Spark The Definitive Guide : Big Data Processing Made Simple"\
    .split(" ")
words = spark.sparkContext.parallelize(myCollection, 2)
```

<br><br>

<h1>1. 키-값 형태의 기초(키-값 형태의 RDD)</h1>
<ul>
  <li>
    RDD에는 데이터를 key-value 형태로 다룰 수 있는 다양한 메서드가 있으며 이런 메서드는 <strong><연산명>ByKey</strong> 형태의 이름을 갖는다.
  </li>
  <li>
    메서드 이름에 ByKey가 있다면 <strong>PairRDD 타입</strong>만 사용할 수 있다.
  </li>
  <li>
    PairRDD 타입을 만드는 가장 쉬운 방법은 RDD에 <strong>map 연산</strong>을 수행해 <strong>key-value 구조</strong>로 만드는 것이다.
  </li>
</ul>

```python
# 1. map 연산을 통해 PairRDD 구조 생성.
words.map(lambda word: (word.lower(), 1))
```

<br>

<h2>1-1. keyBy</h2>
<ul>
  <li>
    <strong>현재 값</strong>으로부터 <strong>key를 생성</strong>하는 <strong>KeyBy 함수</strong>를 사용하면 <strong>ByKey와 동일한 결과</strong>를 얻을 수 있다.
  </li>
</ul>

```python
# 1. 단어의 첫 번째 문자를 key로 만들어 RDD를 생성.
#   - Spark는 원본 단어를 생성된 RDD의 값으로 유지한다.
keyword = words.keyBy(lambda word: word.lower()[0])
```

<br>

<h2>1-2. 값 매핑하기</h2>
<ul>
  <li>
    <strong>튜플 형태</strong>의 데이터를 사용하는 경우 Spark는 튜플의 <strong>첫 번째 요소를 key</strong>로, <strong>두 번째 요소를 value</strong>로 추정한다.
  </li>
  <li>
    튜플 형태의 데이터에서 key를 제외하고 <strong>value만</strong> 추출할 수도 있다.
  </li>
</ul>

```python
# 1. mapValues 메서드를 사용하여 값만 추출
#   - 값 수정 시 발생할 수 있는 오류를 미리 방지.
#   - key는 그대로 두고 value에만 upper()를 수행.
keyword.mapValues(lambda word: word.upper()).collect()
```

```python
# 2. flatMap 함수를 사용하여 반환되는 결과의 각 row가 문자를 나타내도록 확장.
keyword.flatMapValues(lambda word: word.upper()).collect
```

<br>

<h2>1-3. 키와 값 추출하기</h2>

```python
# 1. 키와 값 전체 추출

# Key
keyword.keys().collect()

# Value
keyword.values().collect()
```

<br>

<h2>1-4. lookup</h2>
<ul>
  <li>
    <strong>특정 key</strong>에 관한 결과를 찾는다.
  </li>
  <li>
    오직 하나의 key만 찾을 수 있도록 강제하지 않기 때문에 <strong>key가 일치하는 여러 값</strong>이 출력된다.
  </li>
</ul>

```python
# 1. lookup을 통한 조회
keyword.lookup["s"]
```

<br>

<h2>1-5. sampleByKey</h2>
<ul>
  <li>
    근사치나 정확도를 이용해 <strong>key를 기반</strong>으로 <strong>RDD 샘플을 생성</strong>할 수 있다.
  </li>
  <li>
    근사치와 정확도를 사용하는 두 작업 모두 key를 <strong>부분 샘플링</strong> 할 수 있으며 선택에 따라 <strong>비복원 추출</strong>을 사용할 수도 있다.
  </li>
  <li>
    <strong>sampleByKeyExact</strong>는 <strong>99.99% 신뢰도</strong>를 갖는 <strong>모든 key</strong>에 대해 <strong>RDD를 추가로 처리</strong>한다.
  </li>
    <ul>
      <li>
        math.ceil(numItems * samplingRate)의 합과 <strong>완전히 동일한 크기</strong>의 샘플 데이터를 생성한다는 점이 sampleByKey 함수와는 다르다.
      </li>
      <li>
        <strong>비복원 추출</strong>을 사용할 경우 샘플 크기를 보장하기 위해 RDD를 <strong>한 번 더</strong> 통과해야 한다. 반면 <strong>복원 추출</strong>을 사용할 경우 RDD를 <strong>두 번 더</strong> 통과해야 한다.
      </li>
    </ul>
</ul>

```python
# 1. sampleByKey 메서드로 샘플링.
#   - RDD를 한 번만 처리하며 간단한 무작위 샘플링을 한다.
import random

# 첫 번째 글자를 key로
distinctChars = words.flatMap(lambda word: list(word.lower())).distinct()\
    .collect()

# distincChars의 각 문자에 대해 0 ~ 1 사이의 확률을 매핑.
sampleMap = dict(map(lambda c: (c, random.random()), distinctChars))

# key 별로 확률을 기반으로한 복원 샘플링
words.map(lambda word: (word.lower()[0], word))\
    .sampleByKey(True, sampleMap, 6).collect()
```

```scala
// 2. sampleByKeyExact 메서드를 통한 샘플링.
words.map(word => (word.toLowerCase.toSeq(0), word))
  .sampleByKeyExact(true, sampleMap, 6L).collect()
```

<br><br>

<h1>2. 집계</h1>

```python
# 1. RDD와 PairRDD
#   - PairRDD란 튜플을 원소로 갖는 RDD를 의미한다.

# 일반적인 RDD
chars = words.flatMap(lambda word: word.lower())

# (letter, 1)의 튜플 형식을 원소로 갖는 PairRDD
KVcharacters = chars.map(lambda letter: (letter, 1))

def maxFunc(left, right):
    return max(left, right)
def addFunc(left, right):
    return left + right

# 다섯 개의 파티션으로 나누 RDD 생성.
nums = sc.parallelize(range(1, 31), 5)
```

<br>

<h2>2-1. countByKey</h2>
<ul>
  <li>
    countByKey 메서드는 <strong>각 key의 아이템 수</strong>를 구하고 <strong>로컬 map</strong>으로 <strong>결과를 수집</strong>한다.
  </li>
    <ul>
      <li>
        <strong>아이템</strong>: RDD 안에 들어 있는 <strong>(key, value) 쌍 하나</strong>를 의미한다.
      </li>
    </ul>
  <li>
    Scala 혹은 Java를 사용할 경우 제한 시간(timeout)과 신뢰도를 인수로 지정해 근사치를 구할 수 있다.
  </li>
</ul>

```python
# 1. 바로 이전 주제에 생성했던 KVcharacters에 메서드 적용.
KVcharacters.countByKey()
```

<br>

<h2>2-2. 집계 연산 구현 방식 이해하기</h2>
<ul>
  <li>
    key-value 형태의 <strong>PairRDD를 생성</strong>하는 데에는 몇 가지 방식이 있으며 구현 방식은 <strong>Job의 안정성</strong>을 위해 매우 중요하다.
  </li>
</ul>

<h3>2-2-1. groupByKey</h3>
<ul>
  <li>
    API 문서의 내용대로면 <strong>각 key의 총 record 수</strong>를 구하는 경우 <strong>roupByKey의 결과로 만들어진 그룹</strong>에 <strong>map 연산</strong>을 수행하는 방식이 가장 좋아보이지만 잘못된 접근인 경우가 많다.
  </li>
    <ul>
      <li>
        문제는 모든 익스큐터에 함수를 적용하기 전 <strong>해당 key와 관련된 모든 값</strong>을 <strong>메모리</strong>로 읽어 들여야 한다는 것이다.
      </li>
      <li>
        메모리로 읽어 들여야하는 이유는 <strong>심각하게 치우쳐진 key</strong>가 있다면 <strong>일부 파티션이 엄청난 양의 값</strong>을 가져 <strong>OutOfMemoryError</strong>가 발생하기 때문이다.
      </li>
    </ul>
  <li>
    따라서 groupByKey 메서드를 사용하는 경우는 <strong>각 key에 대한 값의 크기가 일정</strong>하고, 익스큐터에 <strong>할당된 메모리</strong>에서 처리 가능할 정도일 때이다.
  </li>
</ul>

```python
# 1. groupByKey를 통한 집계
from functools import reduce

KVcharacters.groupByKey().map(lambda row: (row[0], reduce(addFunc, row[1])))\
    .collect()
```

<h3>reduceByKey</h3>
<ul>
  <li>
    <strong>reduceByKey 메서드</strong>를 사용하면 <strong>각 파티션</strong>에서 reduce 작업을 수행하기 때문에 <strong>안정적</strong>이며 모든 값을 <strong>메모리에 유지하지 않아도 된다</strong>.
  </li>
  <li>
    최종 reduce 과정을 제외하면 모든 작업이 <strong>개별 워커</strong>에서 처리되기 때문에 연산 중에 <strong>셔플이 발생하지 않는다</strong>.
  </li>
  <li>
    reduceByKey 메서드는 <strong>key 별 그룹 RDD</strong>를 반환하며 <strong>안정성</strong>과 <strong>수행 속도</strong>에서 크게 이득을 볼 수 있다.
  </li>
  <li>
    그러나 반환된 RDD의 개별 요소들은 <strong>정렬</strong>되어 있지 않기에 결과의 <strong>순서가 중요한 경우에는 적합하지 않다</strong>.
  </li>
</ul>

```python
# 1. reductByKey를 활용한 결과 조회
KVcharacters.reduceByKey(addFunc).collect()
```

<br>

<h2>2-3. 기타 집계 메서드</h2>
<ul>
  <li>
    <strong>구조적 API</strong>를 사용하면 훨씬 간단하게 집계를 수행할 수 있기 때문에 굳이 고급 집계 함수를 사용할 필요가 없다.
  </li>
  <li>
    그럼에도 <strong>고급 집계 함수</strong>를 사용하면 <strong>클러스터 노드</strong>에서 수행하는 집계를 아주 구체적이고 매우 세밀하게 제어할 수 있다.
  </li>
</ul>

<h3>2-3-1. aggregate</h3>
<ul>
  <li>
    <strong>aggregate 함수</strong>는 <strong>null 값이나 집계의 시작값</strong>과 <strong>두 개의 함수</strong>를 파라미터로 받는다.
  </li>
  <li>
    <strong>첫 번째 함수</strong>는 <strong>파티션 내</strong>에서 실행되고, <strong>두 번째 함수</strong>는 <strong>모든 파티션</strong>에 걸쳐 수행된다. (두 함수는 모두 시작값을 사용한다).
  </li>
  <li>
    aggregate 함수는 <strong>드라이버에서 최종 집계</strong>를 수행하기 때문에 <strong>성능</strong>에 약간의 영향이 있다.
  </li>
  <li>
    <strong>treeAggregate 함수</strong>는 aggregate 함수와 유사하지만 기본적으로 드라이버에서 최종 집계를 수행하기 전 <strong>익스큐터들끼리 트리</strong>를 형성해 집계 처리의 일부 하위 과정을 <strong>푸시 다운(push down) 방식</strong>으로 먼저 수행한다.
  </li>
    <ul>
      <li>
        이렇게 집계 처리를 <strong>여러 단계</strong>로 구성하는 것은 드라이버의 <strong>메모리를 모두 소비하는 현상을 방지</strong>한다. (작업의 안정성 또한 포함).
      </li>
      <li>
        <strong>대규모의 데이터</strong>에서는 <strong>treeAggregate</strong>를 사용하는 것이 좋지만 <strong>소규모 데이터</strong>를 다룰 때에는 <strong>aggregate 함수가 더 빠르다</strong>.
      </li>
    </ul>
</ul>

```python
# 1. aggregate의 예
nums.aggregate(0, maxFunc, addFunc)
```

```python
# 2. treeAggregate의 예
depth = 3
nums.treeAggregate(0, maxFunc, addFunc, depth)
```

<h3>2-3-2. aggregateByKey</h3>
<ul>
  <li>
    <strong>aggregateByKey 함수</strong>는 aggregate 함수와 동일하지만 파티션 대신 <strong>key를 기준으로 연산을 수행</strong>한다는 차이가 있다.
  </li>
</ul>

```python
# 1. aggregateByKey 함수를 통한 집계
KVcharacters.aggregateByKey(0, addFunc, maxFunc).collect()
```

<h3>2-3-3. combineByKey</h3>
<ul>
  <li>
    <strong>combineByKey 함수</strong>는 집계 함수 대신 <strong>컴바이너(combiner)</strong>를 사용한다.
  </li>
  <li>
    combiner는 <strong>key를 기준</strong>으로 연산을 수행하며 파라미터로 사용된 <strong>함수</strong>에 따라 <strong>값을 병합</strong>한다. 이후 여러 combiner의 결괏값을 <strong>다시 병합</strong>해 결과를 반환한다.
  </li>
    <ul>
      <li>
        사용자 지정 파티셔너를 사용해 출력 파티션 수를 지정할 수도 있다.
      </li>
    </ul>
</ul>

```python
# 1. combineByKey을 통해 병합.
# 값을 combiner로 변환
def valToCombiner(value):
    return [value]

# 두 값을 합하는 함수
def mergeValuesFunc(vals, valToAppend):
    vals.append(valToAppend)
    return vals

# 두 combiner를 합하는 함수
def mergeCombinerFunc(vals1, vals2):
    return vals1 + vals2

# 출력 파티션의 수
outputPartitions = 6

# 함수 실행
KVcharacters\
    .combineByKey(
        valToCombiner,
        mergeValuesFunc,
        mergeCombinerFunc,
        outputPartitions)\
    .collect()
```

<h3>2-3-4. foldByKey</h3>
<ul>
  <li>
    <strong>foldByKey 함수</strong>는 <strong>결합 함수</strong>와 <strong>항등원(neutral)</strong>인 제로값을 이용해 각 key의 값을 병합한다.
  </li>
    <ul>
      <li>
        <strong>제로값</strong>은 결과에 여러 번 사용될 수 있으나 결과를 변경할 수는 없다. <strong>(덧셈: 0, 곱셈: 1)</strong>.
      </li>
    </ul>
  <li>
    <strong>항등원</strong>을 사용하면 RDD가 <strong>비는 경우</strong>가 없어 Error가 발생할 가능성을 줄일 수 있다. 또한 <strong>초기값이 필요한 경우</strong>(리스트 합치기 등)에도 도움이 된다.
  </li>
</ul>

```python
# 1. foldByKey 함수를 통한 병합
KVcharacters.foldByKey(0, addFunc).collect()
```

<br><br>

<h1>3. cogroup</h1>
<ul>
  <li>
    <strong>cogroup 함수</strong>는 RDD에 대한 <strong>그룹 기반의 조인</strong>을 수행한다.
  </li>
    <ul>
      <li>
        Scala를 사용하는 경우 최대 3개, <strong>python</strong>을 사용하는 경우 <strong>최대 2개</strong>의 <strong>key-value형태의 RDD</strong>를 그룹화 할 수 있으며 <strong>key를 기준</strong>으로 각 값을 <strong>결합</strong>한다.
      </li>
      <li>
        출력 파티션 수나 클러스터에 <strong>데이터 분산 방식</strong>을 정확하게 제어하기 위해 <strong>사용자 정의 파티션 함수</strong>를 파라미터로 사용할 수 있다.
      </li>
    </ul>
  <li>
    <strong>그룹화된 key</strong>를 key로, <strong>키와 관련된 모든 값</strong>을 value로 하는 <strong>key-value 형태의 배열</strong>을 결과로 반환한다.
  </li>
</ul>

```python
# 1. cogroup 함수를 통해 RDD에 대한 그룹화 기반 조인 수행.
import random

# 중복 없이 소문자로 값을 변경하여 초기화
distinctChars = words.flatMap(lambda word: word.lower()).distinct()

# 첫 번째 랜덤 샘플링하여 초기화
charRDD = distinctChars.map(lambda c: (c, random.random()))

# 두 번째 램덤 샘플링하여 초기화
charRDD2 = distinctChars.map(lambda c: (c, random.random()))

# cogroup 기반 조인
# 같은 key(문자)를 기준으로 두 RDD의 value들을 그룹핑해서 
# (key, (iterable1, iterable2)) 형태로 반환
charRDD.cogroup(charRDD2).take(5)
```

<br><br>

<h1>4. 조인</h1>
<ul>
  <li>
    RDD는 구조적 API와 거의 동일한 조인 방식을 갖지만 사용자가 많은 부분에 관여해야 한다.
  </li>
</ul>

<br>

<h2>4-1. 내부 조인</h2>

```python
# 1. RDD 조인의 예. (하단의 다른 조인들 모두 동일하다).
#   - fullOuterJoin
#   - leftOuterJoin
#   - rightOuterJoin
#   - cartesian

# distinctChars에서 무작위 샘플링.
keyedChars = distinctChars.map(lambda c: (c, random.random()))

# 출력 파티션 수 설정
outputPartitions = 10

# 출력 파티션 설정 없이 조인
KVcharacters.join(keyedChars).count()

# 출력 파티션 수를 설정하여 조인
KVcharacters.join(keyedChars, outputPartitions).count()
```

<br>

<h2>4-2. zip</h2>
<ul>
  <li>
    zip 함수를 사용해 <strong>동일한 길이</strong>의 두 개의 RDD를 사용해 <strong>PairRDD</strong>를 생성한다. 두 개의 RDD는 <strong>동일한 수의 요소</strong>와 <strong>동일한 수의 파티션</strong>을 가져야한다.
  </li>
</ul>

```python
# 1. zip 함수를 통한 조인(결합)
numRange = sc.parallelize(range(10), 2)
wrods.zip(numRnage).collect()
```

<br><br>

<h1>5. 파티션 제어하기</h1>
<ul>
  <li>
    <strong>RDD</strong>를 사용하면 데이터가 <strong>클러스터 전체</strong>에 <strong>물리적으로 정확히 분산되는 방식</strong>을 정의할 수 있다.
  </li>
  <li>
    몇몇 기능들은 구조적 API와 기본적으로 동일하지만 <strong>구조적 API</strong>는 <strong>파티션 함수</strong>를 파라미터로 사용할 수 있다는 차이가 있다.
  </li>
  <li>
    파티션 함수는 보통 사용자 지정 Partitioner를 의미한다.
  </li>
</ul>

<br>

<h2>5-1. coalesce</h2>
<ul>
  <li>
    coalesce는 파티션을 재분배할 때 데이터 셔플을 방지하기 위해 동일한 워커에 존재하는 파티션을 합치는 메서드이다.
  </li>
</ul>

```python
# 1. 두 개의 파티션으로 구성된 words RDD를 coalesce 메서드를 통해 하나의 파티션으로 병합
words.coalesce(1).getNumPartitions
```

<br>

<h2>5-2. repartition</h2>
<ul>
  <li>
    <strong>repartition 메서드</strong>를 통해 <strong>파티션의 수</strong>를 늘리거나 줄일 수 있다. 그러나 <strong>셔플</strong>이 발생할 수 있다는 단점이 있다.
  </li>
  <li>
    파티션의 수를 늘리면 <strong>맵 타입</strong>이나 <strong>필터 타입</strong>의 연산을 수행할 때 <strong>병렬 처리 수준</strong>을 높일 수 있다.
  </li>
</ul>

```python
# 1. repartition을 통해 10 개의 파티션 생성
words.repartition(10)
```

<br>

<h2>5-3. repartitionAndSortWithinPartitions</h2>
<ul>
  <li>
    해당 메서드를 통해 <strong>파티션을 재분배</strong>할 수 있으며 재분배된 결과 파티션의 <strong>정렬 방식</strong>을 지정할 수 있다. (관련 문서 확인).
  </li>
  <li>
    <strong>파티셔닝</strong>과 <strong>키</strong> 모두 <strong>사용자가 지정</strong>할 수 있다.
  </li>
</ul>

<br>

<h2>5-4. 사용자 정의 파티셔닝</h2>
<ul>
  <li>
    <strong>사용자 정의 파티셔닝(custom partitioning)</strong>은 RDD를 사용하는 가장 큰 이유 중 하나이다.
  </li>
  <li>
    논리적인 대응책을 갖고 있지 않기 때문에 <strong>구조적 API</strong>에서는 <strong>사용자 정의 파티셔너를 파라미터로 사용할 수 없다</strong>.
  </li>
    <ul>
      <li>
        사용자 정의 파티셔너는 <strong>저수준 API의 세부적인 구현 방식</strong>이다. Job이 성공적으로 동작되는지 여부에 상당한 영향을 미친다.
      </li>
    </ul>
  <li>
    사용자 정의 파티셔닝의 예로는 <strong>페이지랭크(PageRank)</strong>가 있다. PageRank는 사용자 정의 파티셔닝을 이용해 <strong>클러스터의 데이터 배치 구조를 제어</strong>하고 <strong>셔플을 회피</strong>한다.
  </li>
  <li>
    사용자 정의 파티셔닝의 목표는 데이터의 <strong>skew(치우침)</strong>과 같은 문제를 회피하고자 <strong>클러스터 전체에 데이터를 균등하게 분배</strong>하는 것이다.
  </li>
  <li>
    사용자 정의 파티셔너를 사용하는 방법은 다음과 같다. 해당 방법은 필요시에만 사용자 정의 파티셔닝을 사용할 수 있어 <strong>구조적 API</strong>와 <strong>RDD의 장점</strong>을 모두 갖는다.
  </li>
    <ul>
      <li>
        <strong>구조적 API로 RDD</strong>를 얻는다.<br>→ <strong>사용자 정의 파티셔너</strong>를 적용한다.<br>→ <strong>다시 DataFrame이나 Dataset</strong>으로 변환한다.
      </li>
    </ul>
  <li>
    사용자 정의 파티셔닝을 사용하기 위해서는 <strong>Partitioner를 확장한 클래스</strong>를 구현해야 한다.
  </li>
  <li>
    <strong>단일 값이나 다수 값(다수 컬럼)</strong>을 파티셔닝해야 한다면 <strong>DataFrame API</strong>를 사용하는 것이 좋다.
  </li>
  <li>
    <strong>HashPartitioner</strong>와 <strong>RangePartitioner</strong>는 RDD API에서 사용할 수 있는 내장형 파티셔너이다.
  </li>
    <ul>
      <li>
        <strong>HashPartitioner는 이산형 값</strong>을, <strong>RangePartitioner는 연속형 값</strong>을 다룰 때 사용한다.
      </li>
      <li>
        두 파티셔너는 <strong>구조적 API</strong>와 <strong>RDD</strong> 모두 사용할 수 있다.
      </li>
      <li>
        유용하지만 기초적인 기능을 제공하기에 <strong>매우 큰 데이터</strong>나 <strong>심각하게 치우친 키</strong>를 다룰 때에는 <strong>고급 파티셔닝 기능</strong>을 사용해야 한다.
      </li>
    </ul>
  <li>
    <strong>키 치우침 현상</strong>은 <strong>어떤 키</strong>가 다른 키에 비해 <strong>아주 많은 데이터</strong>를 갖는 현상을 의미한다.
  </li>
    <ul>
      <li>
        키 치우침 현상을 방지하기 위해 <strong>병렬성을 개선</strong>하고 실행 과정에서 OutOfMemoryError를 방지할 수 있도록 <strong>키를 최대한 분할</strong>해야 한다.
      </li>
    </ul>
  <li>
    키가 <strong>특정 형태</strong>를 띄는 경우 키를 분할해야 한다.
  </li>
    <ul>
      <li>
        예를 들어 전체 고객 중에 데이터를 많이 발생시키는 두 명의 고객이 있담녀 해당 두 고객의 정보를 분리하여 처리한다.
      </li>
    </ul>
  <li>
    <strong>사용자 정의 키 분배 로직</strong>은 <strong>RDD 수준</strong>에서만 사용할 수 있다.
  </li>
    <ul>
      <li>
        사용자 정의 키 분배 로직은 <strong>임의의 로직</strong>을 사용해 <strong>물리적인 방식</strong>으로 <strong>클러스터에 데이터를 분배</strong>하는 강력한 방법이다.
      </li>
    </ul>
</ul>

```python
# 1. 데이터를 읽고 10개의 파티션으로 "축소(coalesce)"한다.
df = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("/opt/spark-data/data/retail-data/all/")
rdd = df.coalesce(10).rdd

df.printSchema()
```

```scala
// 2. HashPartitioner를 통한 파티셔닝
import org.apache.spark.HashPartitioner

rdd.map(r => r(6)).take(5).foreach(println)
val keyedRDD = rdd.keyBy(row => row(6).asInstanceOf[Int].toDouble)

keyedRDD.partitionBy(new HashPartitioner(10)).take(10)
```

```python
# 3. 키 분할 (특정 키는 0번 파티션, 나머지는 랜덤으로 1~2번 파티션에 배치)
def partitionFunc(key):
    import random

    if key == 17850 or key == 12583:
        return 0
    else:
        return random.randint(1, 2)
    
# 6번째 컬럼을 key로 사용
keyedRDD = rdd.keyBy(lambda row: row[6])

keyedRDD\
    # 커스텀 파티셔너로 3개 파티션으로 분할
    .partitionBy(3, partitionFunc)\
    # key만 추출
    .map(lambda x: x[0])\
    # 각 파티션의 데이터를 리스트로 묶음
    .glom()\
    # 파티션별 고유 key 개수 계산
    .map(lambda x: len(set(x)))\
    # 앞 5개 결과 확인
    .take(5)
```

<br><br>

<h1>6. 사용자 정의 직렬화</h1>
<ul>
  <li>
    <strong>Kryo 직렬화</strong>에 대해 배운다. 병렬화 대상인 모든 객체나 함수는 <strong>직렬화</strong>할 수 있어야 한다.
  </li>
  <li>
    Spark가 직렬화에 사용하는 Kryo는 Java 직렬화 보다 약 10배 이상 성능이 좋고 간결하다. 단, 모든 직렬화 유형을 지원하지는 않으며 최상의 성능을 위해서는 프로그램에 사용할 클래스를 사전 등록해야 한다.
  </li>
  <li>
    <strong>SparkConf</strong>를 사용해 Job을 초기화하는 시점에서 <strong>spark.serializer 속성값</strong>을 <strong>org.apache.spark.serializer.KryoSerializer</strong>로 설정해 Kyro를 사용할 수 있다.
  </li>
  <li>
    spark.serializer 설정으로 <strong>워커 노드 간 데이터 셔플링과 RDD를 직렬화</strong>해 <strong>디스크에 저장하는 용도</strong>로 사용할 시리얼라이저를 지정할 수 있다.
  </li>
  <li>
    Kryo가 기본값이 아닌 이유는 <strong>사용자가 직접 클래스를 등록</strong>해야하기 때문이다.
  </li>
  <li>
    <strong>Spark 2.0.0 버전</strong>부터는 단순 데이터 타입, 단순 데이터 타입의 배열, 문자열 데이터 타입의 RDD를 셔플링하면 <strong>내부적으로 Kryo 시리얼라이저</strong>를 사용한다.
  </li>
  <li>
    Spark는 트위터 칠(Twitter chill) 라이브러리의 AllScalaRegister에서 다루는 핵심 스칼라 클래스를 자동으로 Kryo 시리얼라이즈에 등록한다.
  </li>
  <li>
    Kryo에 사용자 정의 클래스를 <strong>등록</strong>하려면 <strong>registerKryoClasses 메서드</strong>를 사용한다.
  </li>
</ul>

```scala
// 1. 병렬화작업을 직렬화 변환
class SomeClass extends Serializable {
  var someValue = 0
  def setSomeValue(i:Int) = {
    someValue = I
    this
  }
}

sc.parallelize(1 to 10).map(num => SomeClass().setSomeValue(num))
```

```scala
// 2. Kryo 등록
val conf = new SparkConf().setMaster(...).setAppName(...)
// SparkConf 객체 생성 (마스터와 애플리케이션 이름 설정)

conf.registerKryoClasses(Array(classOf[MyClass1], classOf[MyClass2]))
// Kryo 직렬화를 사용할 때, 사용자 정의 클래스들을 미리 등록
//    → 성능 향상 및 직렬화 효율 개선

val sc = new SparkContext(conf)
// 등록된 설정을 기반으로 SparkContext 생성
```