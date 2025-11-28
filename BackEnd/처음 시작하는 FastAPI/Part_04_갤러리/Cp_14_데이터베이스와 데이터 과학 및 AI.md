<h1>1. 데이터 저장소</h1>
<ul>
  <li>
    대개 웹사이트의 백엔드는 DB이다.
  </li>
  <li>
    DB는 일반적으로 다음 중 하나이다.
  </li>
    <ul>
      <li>
        <strong>SQL 쿼리</strong> 언어를 사용하는 <strong>관계형 DB</strong>
      </li>
      <li>
        <strong>다양한 쿼리</strong> 언어를 지원하는 <strong>비관계형 DB</strong>
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 관계형 DB와 SQL (p252)</h1>
<ul>
  <li>
    대표적인 관계형 DB와 해당 DB의 파이썬 드라이버 패키지를 소개한 장표가 있다.
  </li>
</ul>

<br>

<h2>2-1. SQLAlchemy</h2>
<ul>
  <li>
    SQLAlchemy에 기반이 되는 모듈을 <strong>코어(core)</strong>라 하며 다음으로 구성된다.
  </li>
    <ul>
      <li>
        DB-API 표준을 구현하는 Engine 객체
      </li>
      <li>
        SQL 서버 유형과 드라이버, 그리고 해당 서버의 특정 DB 집합을 표현하는 URL
      </li>
      <li>
        클라이언트-서버 연결 풀
      </li>
      <li>
        트랜잭션(COMMIT과 ROLLBACK)
      </li>
      <li>
        DB 유형마다 다른 SQL 방언 지원
      </li>
      <li>
        SQL 쿼리를 직접 처리
      </li>
      <li>
        SQLAlchemy 표현식 언어로 된 쿼리
      </li>
    </ul>
</ul>

```python
# 1. get_one() 함수에서 간단한 SQL을 직접 사용 (data/explorer.py)
def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())
```

```python
# 2. get_one() 함수를 SQLAlchemy 표현식 언어로 수정.
from sqlalchemy import MetaData, Table, Column, Text
from sqlalchemy import create_engine, select, Row

engine = create_engine("sqlite:///db/cryptid.db")
conn = engine.connect()
meta = MetaData()
explorer_table = Table(
    "explorer",
    meta,
    Column("name", Text, primary_key=True),
    Column("country", Text),
    Column("description", Text),
)

def get_one(name: str) -> Row | None:
    stmt = select(explorer_table).where(explorer_table.c.name==name)
    result = conn.execute(stmt)
    return result.fetchone()
```

<h3>ORM</h3>
<ul>
  <li>
    ORM은 도메인 데이터 모델의 관점에서 쿼리를 표현한다.
  </li>
  <li>
    ORM은 SQL 표현식보다 언어가 훨씬 복잡하며 완전한 객체 지향 패턴을 선호하는 개발자는 대부분 ORM을 선호한다.
  </li>
  <li>
    간단한 방법은 SQL을 사용하다가 SQL이 복잡해지는 시점에 표현식 언어나 ORM으로 이동하는 방법이다.
  </li>
</ul>

<br>

<h2>2-2. SQLModel</h2>
<ul>
  <li>
    SQLAlchemy ORM을 Pydantic 데이터 정의 및 유효성 검사와 결합한다.
  </li>
</ul>

<br>

<h2>2-3. SQLite</h2>
<ul>
  <li>
    모든 브라우저와 스마트폰에 지원이 되지만, 관계형 DB 선택지로는 잘 고려되지 않는다.
  </li>
</ul>

<br>

<h2>PostgreSQL</h2>
<ul>
  <li>
    과거 오픈 소스인 Ingres가 Oracle에 밀렸는데 후에 PostgreSQL로 마이그레이션 되었다.
  </li>
</ul>

<br>

<h2>EdgeDB</h2>
<ul>
  <li>
    EdgeDB는 SQL의 까다로운 특징을 완화한 새로운 쿼리 언어로 실제로는 PostgreSQL에서 실행할 수 있는 SQL로 변환한다.
  </li>
</ul>

<br><br>

<h1>3. 비관계형 데이터베이스(p257)</h1>
<ul>
  <li>
    NoSQL과 NewSQL의 DB가 장표로 정리되어 있다.
  </li>
  <li>
    NoSQL은 규칙을 완화해 데이터 행에서 다양한 열/필드 유형을 허용하기도 한다. JSON이나 파이썬으로 표현된 불규칙한 구조를 가질 수 있다.
  </li>
</ul>

<br>

<h2>3-1. 레디스</h2>
<ul>
  <li>
    Redis는 <strong>메모리에서 실행되는 데이터 구조</strong>를 갖는 서버이다.
  </li>
</ul>

<br>

<h2>3-2. 몽고DB</h2>
<ul>
  <li>
    몽고 DB는 NoSQL 계의 PostgreSQL과 같다.
  </li>
  <li>
    <strong>collection</strong>은 <strong>SQL 테이블</strong>에 대응되고, <strong>document</strong>는 <strong>SQL 테이블의 행</strong>에 해당한다.
  </li>
    <ul>
      <li>
        Document가 어떻게 생겼는지 정의할 필요 없으며 어떤 문자열도 키가 될 수 있는 <strong>파이썬 딕셔너리</strong>와 같다.
      </li>
    </ul>
</ul>

<br>

<h2>3-3. 카산드라</h2>
<ul>
  <li>
    Cassandra는 수백 개의 노드에 분산해 실행할 수 있는 대규모 데이터베이스미여 Java로 작성됐다.
  </li>
</ul>

<br>

<h2>3-4. 엘라스틱서치</h2>
<ul>
  <li>
    텍스트 검색에 자주 사용된다. DB보다는 <strong>DB 인덱스</strong>에 가깝다.
  </li>
</ul>

<br><br>

<h1>4. SQL 데이터베이스의 NoSQL 기능</h1>
<ul>
  <li>
    관계형 DB는 정규형이라 부르는 다양한 수준의 규칙을 따른다.
  </li>
  <li>
    NoSQL DB는 <strong>JSON</strong>을 직접 지원하며, DB 구조가 고르지 않거나 불규칙한 경우 대게 유일한 선택지였다.
  </li>
  <li>
    최근에는 관계형 DB에서도 JSON을 지원한다.
  </li>
</ul>

<br><br>

<h1>5. 데이터베이스 부하 테스트</h1>
<ul>
  <li>
    페이커(faker) 패키지를 사용해 쉽게 데이터를 만들어 부하 테스트를 진행한다.
  </li>
</ul>

```python
# 1. faker를 통해 이름과 국가를 만들고 load() 함수로 SQLite에 적재.
from faker import Faker
from time import perf_counter

def load():
    from error import Duplicate
    from data.explorer import create
    from model.explorer import Explorer

    f = Faker()
    NUM = 100_000
    t1 = perf_counter()
    for row in range(NUM):
        try:
            create(Explorer(name=f.name(),
                country=f.country(),
                description=f.text()))
        except Duplicate:
            pass
    t2 = perf_counter()
    print(NUM, "rows")
    print("write time:", t2-t1)

def read_db():
    from data.explorer import get_all
    t1 = perf.counter()
    _ = get_all()
    t2 = perf_counter()
    print("db read time:", t2-t1)

def read_api():
    from fastapi.testclient import TestClient
    from main import app
    t1 = perf_counter()
    client = TestClient(app)
    _ = client.get("/explorer/")
    t2 = perf_counter()
    print("api read time:", t2-t1)

load()
read_db()
read_db()
read_api()
```

<br><br>

<h1>6. 데이터 과학과 AI</h1>
<ul>
  <li>
    AI와 관련된 다양한 패키지와 워크 프레임 등을 소개한다.
  </li>
</ul>

```python
# 1. 최상위 수준의 LLM 테스트: ai.py
from fastapi import FastAPI

app = FastAPI()

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = GenerationConfig(max_new_tokens=200)

@app.get("/ai")
def prompt(line: str) -> str:
    tokens = tokenizer(line, return_tensors="pt")
    outputs = model.generate(**tokens, max_new_tokens=config.max_new_tokens)
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return result[0]
```