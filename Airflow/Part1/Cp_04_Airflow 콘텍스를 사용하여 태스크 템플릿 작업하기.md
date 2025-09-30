<ul>
  <li>
    템플릿을 사용하여 런타임 시에 변수 할당하기
  </li>
  <li>
    PythonOperator 및 다른 오퍼레이터를 사용해 변수 템플릿 작업하기
  </li>
  <li>
    디버깅을 위해 템플릿 변수 할당하기
  </li>
  <li>
    외부 시스템에서 태스크 수행하기
  </li>
</ul>

<br>

<h1>1. Airflow로 처리할 데이터 검사하기</h1>
<h2>1-1. 증분 데이터를 적재하는 방법 결정하기</h2>
<ul>
  <li>
    모든 데이터는 크기에 상관없이 구조가 복잡할 수 있으며 파이프라인을 구축하기 전에 <strong>접근 방식에 대한 기술적 계획</strong>을 세우는 것이 중요하다.
  </li>
</ul>

<br><br>

<h1>2. 태스크 콘텍스트와 Jinja 템플릿 작업</h1>
<ul>
  <li>
    모든 것을 모아 위키피티아 페이지 뷰 수를 가져오는 DAG의 첫 번째 버전 구축.
  </li>
  <li>
    첫 번째 단계는 주기적으로 압축 파일을 다운로드 하는 것이다. 
  </li>
  <li>
    여러 가지 방식이 있지만 <strong>BashOperator</strong>와 <strong>PythonOperator</strong>를 중심으로 설명한다.
  </li>
    <ul>
      <li>
        오퍼레이터에 런타임 시 <strong>변수를 삽입</strong>하는 방법은 <strong>다른 모든 유형의 오퍼레이터도 동일</strong>하다.
      </li>
    </ul>
</ul>

```bash
# URL은 다양한 날짜 및 시간 구성 요소로 구성된다.
https://dumps.wikimedia.org/other/pageviews/{year}/{year}-{month}/pageviews-{year}{month}-{day}{hour}0000.gz
```

<br>

<h2>2-1. 오퍼레이터의 인수 템플릿 작업</h2>
<ul>
  <li>
    <strong>{{ }} 이중괄호</strong>는 <strong>Jinja 템플릿 문자열</strong>을 의미한다.
  </li>
  <li>
    <strong>Jinja</strong>는 런타임 시에 템플릿 문자열의 <strong>변수와 and 및 or 표현식을 대체</strong>하는 템플릿 엔진다.
  </li>
  <li>
    <strong>{{ }} 이중 괄호</strong>는 런타임 시 <strong>삽입될 변수</strong>를 의미한다.
  </li>
  <li>
    템플릿 작성은 프로그래머로서 코드 작성 시점에는 값을 알기 어렵지만 <strong>런타임 시에 값을 할당</strong>하기 위해 사용한다.
  </li>
  <li>
    Airflow에는 태스크 콘텍스트에서 실행 시에 사용할 수 있는 여러 변수가 있다.
  </li>
  <li>
    <strong>execution_date</strong> 변수가 그 중 하나이다.
  </li>
    <ul>
      <li>
        Airflow는 날짜 시간에 <strong>Pendulumn</strong> 라이브러리를 사용하며 <strong>execution_date</strong>는 Pendulum의 <strong>datetime 객체</strong>이다.
      </li>
      <li>
        네이티브 파이썬의 datetime의 <strong>호환(drop-in replacement) 객체</strong>이기에 파이썬에서 사용할 수 있는 모든 메서드는 Pendulum에도 사용할 수 있다.
      </li>
      <li>
        즉, datetime.new().year와 pendulum.now().year는 동일하다.
      </li>
    </ul>
</ul>

```python
# 1. BashOperator를 통해 위키피디아 페이지 뷰 다운.
#   - BashOperator는 실행 시 bash 명령을 제공하는 인수인 bash_command 사용.

import airflow.utils.dates
from airflow import DAG
from airflow.operator.bash import BashOperator

dag=DAG(
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@hourly",
)

get_data=BashOperator(
    task_id="get_data",
    bash_command=(
        "curl -o /tmp/wikipageviews.gz "
        "https://dumps.wikimedia.org/other/pageviews/"

        # {{ }}: 이중 괄호는 럼타임 시 삽입될 변수를 의미한다.
        "{{ execution_date.year }}/"
        "{{ execution_date.year }}-"
        "{{ '{:02}'.format(execution_date.month) }}/"
        "pageviews-{{ execution_date.year }}"
        "{{ '{:02}'.format(execution_date.month) }}"
        "{{ '{:02}'.format(execution_date.day) }}-"
        "{{ '{:02}'.format(execution_date.hour) }}0000.gz"
    ),
    dag=dag
)
```

<h3>2-1-1. 어떤 인수가 템플릿으로 지정됩니까?</h3>
<ul>
  <li>
    모든 오퍼레이터는 템플릿으로 만들 수 있는 <strong>속성의 허용 리스트</strong>를 유지하며 리스트에 포함되지 않으면 템플릿은 <strong>문자열로 해석</strong>된다.
  </li>
  <li>
    이 리스트는 모든 오퍼레이터의 <strong>template_fields 속성</strong>에 의해 설정된다.
  </li>
  <li>
    template_fields의 요소는 클래스 속성의 이름이다. __init__에 제공된 인수 이름은 클래스 속성 이름과 일치하기에 일반적으로  template_fields에 나열된 항목은 <strong>__init__ 인수에 1 :1 로 매핑</strong>된다.
  </li>
</ul>

<br>

<h2>2-2. 템플릿에 무엇이 사용 가능할까요?</h2>
<ul>
  <li>
    p68에는 모든 콘텍스트 변수를 확인할 수 있다.
  </li>
</ul>

```python
# 1. PythonOperator를 사용하여 전체 태스크 콘텍스트 출력하여 검사.
import airflow.utils.dates
from airflow import DAG
from airflow.operators.python import PythonOperator

dag=DAG(
    # DAG의 고유 ID
    dag_id="chapter4_print_context",
    # DAG 시작일 (3일 전부터 시작)
    start_date=airflow.utils.dates.days_ago(3),
    # 매일 실행
    schedule_interval="@daily",
)

def _print_context(**kwargs):
    # kwargs 딕셔너리에는 execution_date, ds, run_id 등 다양한 값이 들어있음
    print(kwargs)

# PythonOperator를 사용하여 태스크 생성
print_context=PythonOperator(
    # 태스크 고유 ID
    task_id="print_context",
    # 위에서 정의한 함수 실행
    python_callable=_print_context,
    # 이 태스크가 속할 DAG
    dag=dag,
)
```

<br>

<h2>2-3. PythonOperator 템플릿</h2>
<ul>
  <li>
    <strong>BashOperator</strong>는 bash_command 안에 {{ ds }} 같은 템플릿을 <strong>문자열</strong>로 직접 치환한다. 따라서 <strong>문자열 치환</strong> 방식으로 런타임 정보를 쓴다.
  </li>
    <ul>
      <li>
        bash_command="echo {{ ds }}"
      </li>
    </ul>
  <li>
    <strong>PythonOperator</strong>는 템플릿 치환 없이 kwargs로 context(dict)를 함수에 넘겨준다. 따라서 <strong>함수 인자 전달 방식</strong>으로 런타임 정보를 쓴다.
  </li>
    <ul>
      <li>
        def f(**context): print(context["ds"])
      </li>
    </ul>
  <li>
    <strong>python_callable</strong>는 <strong>실행할 함수를 지정</strong>하는 인자다.
  </li>
  <li>
    함수 안의 코드는 자동으로 템플릿 치환되지 않지만 대신 Airflow가 실행 시 <strong>컨텍스트 변수(ds, execution_date 등)를 kwargs로 전달</strong>해 준다.
  </li>
  <li>
    <strong>함수 인자</strong>는 Airflow가 제공하는 <strong>컨텍스트 변수</strong> 이름과 일치해야 값이 채워진다.
  </li>
  <li>
    <strong>Airflow 1</strong>에서는 <strong>provide_context=True</strong>를 설정해야 컨텍스트 변수를 받을 수 있었다.
  </li>
  <li>
    <strong>Airflow 2</strong>에서는 함수 인자 이름을 <strong>자동으로 매칭</strong>하기 때문에 provide_context=True가 필요 없다.
  </li>
  <li>
    작은 태스크의 경우 <strong>소수의 변수</strong>만 명시하는 것이 가독성이 좋다. 반면 <strong>**context</strong>를 사용하면 <strong>모든 변수</strong>에 접근이 가능하며 <strong>context["key"]</strong>를 통해 접근할 수 있다는 장점이 있다.
  </li>
</ul>

```python
# 1. PythonOperator로 위키피디아 페이지 뷰 다운로드
from urllib import request

import airflow from airflow
import DAG from airflow.operators.python import PythonOperator

# DAG 정의
dag=DAG(
    dag_id="stocksense",
    # DAG 실행 시작일 (하루 전부터 시작)
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval="@hourly",
)

def _get_data(execution_date):
    # execution_date에서 연, 월, 일, 시(hour) 추출
    year, month, day, hour, *_=execution_date.timetuple()
    # Wikimedia 페이지뷰 덤프 URL 구성
    url=(
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month:0>2}/"
        f"pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    # 파일 저장 경로
    output_path="/tmp/wikipageviews.gz"
    # 지정한 URL에서 데이터를 다운로드하여 /tmp에 저장.
    request.urlretrieve(url, output_path)

# PythonOperator 정의
get_data=PythonOperator(
    task_id="get_data",
    # 실행 함수 지정
    python_callable=_get_data,
    # 어떤 DAG에 속하는지 지정.
    dag=dag,
)
```

```python
# 2. 키워드 인수느 두 개의 애스터리스크(**)로 표시하면 캡쳐된다.
#   - Airflow가 실행 시 넘겨주는 모든 컨텍스트 변수를 kwargs(dict)로 캡쳐한다.
#   - kwargs라는 이름은 관례일 뿐, 다른 이름을 써도 됨.
def _print_context(**kwargs):
    print(kwargs)
```

```python
# 3. 인수에 context라는 이름을 지정하면 Airflow 태스크 콘텍스트라는 것을 의미.
#   - kwargs 대신 context라는 이름을 썼을 뿐, 동작은 동일하다.
#   - Airflow가 넘겨주는 task context dict 전체를 받는다.
def _print_context(**context):
    # kwargs와 똑같이 전체 컨텍스트 출력
    print(context)

print_context=PythonOperator(
    task_id="print_context",
    # 위 함수를 태스크로 등록
    python_callable=_print_context,
    dag=dag
)
```

```python
# 4. 스케줄 주기의 시작 및 종료 날짜 출력.

# 4-1) context 만을 활용하기.
#   - execution_date: 현재 태스크 실행 시점의 시작 시간
#   - next_execution_date: 다음 실행 시점
#   - 따라서 DAG 스케줄 주기의 시작/끝 범위를 확인할 수 있다.
def _print_context(**context):
    # context로 부터 execution_date 추출.
    start=context["execution_date"]
    end=context["next_execution_date"]
    print(f"Start: {start}, end: {end}")

print_context=PythonOperator(
    task_id="print_context", python_callable=_print_context, dag=dag
)

# 4-2) execution_date 변수만 명시하기
def _get_data(execution_date, **context):
    year, month, day, hour, *_=execution_date.timetuple()
    # 중략...

# 4-3) context를 사용하지 않고 모든 변수 명시하기.
def _get_data(conf=..., dag=..., dag_run=..., execution_date=..., ...):
    # 중략...
```

<br>

<h2>2-4. PythonOperator에 변수 제공</h2>
<ul>
  <li>
    PythonOperator는 콜러블 함수에 <strong>추가 인수</strong>를 제공하는 방법 또한 지원한다.
  </li>
  <li>
    추가 인수를 제공하는 방법은 <strong>op_args 인수</strong>를 사용하는 것이다.
  </li>
    <ul>
      <li>
        op_args에 <strong>리스트</strong>로 값을 주면 각 리스트의 값들은 콜러블 함수에게 <strong>순차적으로 전달</strong>된다.
      </li>
    </ul>
</ul>

```python
# 1. output_path를 함수 인수로 구성.
def _get_data(output_path, **context):
    year, month, day, hour, *_ = context["execution_date"].timetuple()
    url = (
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month:0>2}/pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    # 함수 내부에서 output_path를 그대로 변수로 사용한다.
    #   - request.urlretrieve는 urllib.request의 함수이다.
    #   - request.urlretrieve(저장할 URL, URL을 저장할 로컬 파일 경로)
    request.urlretrieve(url, output_path)
```

```python
# 2. op_args를 통해 콜러블 함수에 인수 전달

# op_args 인수를 사용한 전달
get_data=PythonOperator(
    task_id="get_date",
    # 앞서 지정한 함수 전달
    python_callable=_get_data,
    # 전달된 _get_data 함수에 인수 전달 (위치 인자)
    #   - /tmp/wikipageviews.gz가 output_path로 전달된다.
    op_args=["/tmp/wikipageviews.gz"],
    dag=dag
)

# op_kwargs를 통해 키워드 인수로 전달.
get_data=PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    # 키워드로 전달
    #   - _get_data(output_path="/tmp/wikipageviews.gz")와 같다.
    op_kwargs={"output_path": "/tmp/wikipageviews.gz"},
    dag=dag
)
```

```python
# 3. 콜러블 함수에 대한 입력으로 템플릿 문자열 제공.
def _get_data(year, month, day, hour, output_path, **_):
    # 함수 인자로 전달된 year, month, day, hour로 URL 생성
    url=(
        "https://dumps.wikimedia.org/other/pageviews/"
        f"{year}/{year}-{month:0>2}/"
        f"pageviews-{year}{month:0>2}{day:0>2}-{hour:0>2}0000.gz"
    )
    # 해당 URL 데이터를 지정한 output_path 경로에 저장
    request.urlretrieve(url, output_path)

get_dat=PythonOperator(
    task_id="get_data",
    python_callable=_get_data,
    # PythonOperator가 템플릿을 지원하지 않기에 kwargs를 통해 전달한다.
    #   - 인자들을 op_kwargs로 전달 (키워드 인자 방식)
    op_kwargs={
        # Jinja 템플릿 → 실행 시 실제 값으로 치환
        "year": "{{ execution_date.year }}",
        "month": "{{ execution_date.month }}",
        "day": "{{ execution_date.day }}",
        "hour": "{{ execution_date.hour }}",
        # Jinja 템플릿이 아닌 고정 문자열도 포함
        "output_path": "/tmp/wikipageviews.gz",
    },
    dag=dag,
)
```

<br>

<h2>2-5. 템플릿의 인수 검사하기</h2>
<ul>
  <li>
    <strong>Airflow UI</strong>에서 작업을 실행한 후 <strong>graph</strong> 또는 <strong>tree</strong> 보기를 선택하고 <strong>Rendered Template</strong> 버튼을 클릭하면 <strong>템플릿 인수 값을 검사</strong>할 수 있다.
  </li>
  <li>
    <strong>Airflow UI</strong>를 통한 보기는 작업을 <strong>스케줄링</strong> 해야한다는 단점이 있다. 반면 <strong>Airflow CLI</strong>를 활용하면 <strong>스케줄링 없이 템플릿 확인</strong>이 가능하다.
  </li>
    <ul>
      <li>
        Airflow CLI 환경은 메타 스토어에 아무것도 등록되지 않기에 간편하게 확인할 수 있다.
      </li>
    </ul>
</ul>

```bash
# 1. Airflow CLI로 템플릿을 렌더링
airflow tasks render [dag id] [task id] [desired execution date]
```

<br><br>

<h1>3. 다른 시스템과 연결하기</h1>
<ul>
  <li>
    Airflow가 태스크 간 데이터를 전달하는 방법에는 두 가지가 있다.
  </li>
    <ul>
      <li>
        <strong>XCom</strong>이라 하며 <strong>Airflow 메타스토어</strong>를 사용하여 태스크 간 결과를 쓰고 읽는다.
      </li>
      <li>
        <strong>영구적인 위치(e.g. 디스크 또는 DB)</strong>에 태스크 결과를 기록한다.
      </li>
    </ul>
  <li>
    Airflow 태스크는 설정에 따라 <strong>물리적으로 서로 다른 컴퓨터</strong>에서 독립적으로 실행되기에 <strong>메모리 공유가 불가</strong>하다.
  </li>
  <li>
    Airflow는 <strong>XCom</strong>이라는 기본 메커니즘을 제공하여 Airflow 메타스토어에서 <strong>선택 가능한(picklable) 개체</strong>를 저장하고 나중에 읽을 수 있다.
  </li>
    <ul>
      <li>
        <strong>피클(pickle)</strong>이란 파이썬의 직렬화 프로토콜로 메모리의 개체를 나중에 다시 읽을 수 있도록 <strong>디스크에 저장할 수 있는 형식으로 변환</strong>하는 것을 의미한다.
      </li>
      <li>
        기본적으로 파이썬 타입(e.g. string, int, dict, list)에서 빌드된 모든 객체는 피클링이 가능하다.
      </li>
    </ul>
  <li>
    피클링이 불가능한 개체로는 <strong>데이터베이스 연결</strong>과 <strong>파일 핸들러</strong>가 있다.
  </li>
  <li>
    <strong>크기가 작은</strong> 오브젝트는 <strong>XCom</strong>을 이용한 <strong>피클링</strong>이 적합하다.
  </li>
    <ul>
      <li>
        Airflow의 메타스토어(일반적으로 MySQL 혹은 Postres)는 <strong>크기가 한정</strong>되어 있다.
      </li>
      <li>
        피클링된 객체는 메타스토어의 <strong>블롭(blob)</strong>에 저장된다. Blob이란 큰 크기의 파일을 저장할 때 사용하는 <strong>이진 데이터</strong>를 의미한다.
      </li>
    </ul>
  <li>
    <strong>크기가 큰 데이터</strong>를 태스크 간 전송할 때에는 디스크 등 <strong>Airflow 외부</strong>에 데이터를 유지하는 것이 좋다.
  </li>
  <li>
    Jinja는 기본적으로 DAG 파일의 경로만 검색하기에 <strong>다른 경로</strong>를 검색하기 위해서는 <strong>template_searchpath 인수</strong>를 사용해 검색할 경로를 추가해야 한다.
  </li>
  <li>
    다양한 외부 시스템과 연계하기 위해서는 <strong>여러 의존성 패키지</strong>를 설치해야하며 이는 대부분 오케스트레이션 시스템의 특성 중 하나이다.
  </li>
  <li>
    PostgresOperator는 Postgres와 통신하기 위해 <strong>훅(hook)</strong>이라고 불리는 것을 인스턴스화 한다.
  </li>
    <ul>
      <li>
        훅은 <strong>연결 생성, postgres 쿼리 전송</strong> 그리고 <strong>연결에 대한 종료</strong> 작업을 처리한다.
      </li>
      <li>
        오퍼레이터는 사용자의 요청을 <strong>훅으로 전달</strong>하는 작업만 담당한다.
      </li>
      <li>
        훅은 오퍼레이터 내부에서만 동작하기에 신경쓸 필요는 없다.
      </li>
    </ul>
</ul>

```python
# 1. 지정된 페이지 이름에 대한 페이지 뷰 읽기

# ---- BashOperator ----
extract_gz=BashOperator(
    task_id="extract_gz",
    # gzip으로 압축된 파일(/tmp/wikipageviews.gz)을 강제로 풀어서 원본 파일 생성
    bash_command="gunzip --force /tmp/wikipageviews.gz",
    dag=dag
)

# ---- Python 함수 ----
def _fetch_pageviews(pagenames):
    # pagenames에 있는 페이지 이름을 키로 하고, 기본값을 0으로 하는 dict 초기화
    result=dict.fromkeys(pagenames, 0)

    # 압축 해제된 위키미디어 pageviews 파일 열기
    with open(f"/tmp/wikipageviews", "r") as f:
        for line in f:
            # 한 줄은 "domain_code page_title view_counts something" 형태
            domain_code, page_title, view_counts, _=line.split(" ")
            if domain_code == "en" and page_title in pagenames:
                # 해당 페이지의 뷰 카운트를 업데이트
                result[page_title]=view_counts

    print(result)
    # Prints e.g. "{'Facebook': '778', 'Apple': '20', 'Google': '451', 
    #               'Amazon': '9', 'Microsoft': '119'}

# ---- PythonOperator ----
fetch_pageviews=PythonOperator(
    task_id="fetch_pageviews",
    python_callable=_fetch_pageviews,
    # 함수에 전달할 인자 (키워드 인자)
    #   - _fetch_pageviews(pagenames={...}) 형태로 호출됨
    op_kwargs={
        "pagenames": {
            "Google",
            "Amazon",
            "Apple",
            "Microsoft",
            "Facebook",
        }
    },
    dag=dag
)
```

```sql
-- 2. DAG 출력 결과를 저장하기 위한 postgreSQL 테이블 생성.
CREATE TABLE pageview_counts (
    -- 위키피디아의 페이지 이름 저장
    pagename VARCHAR(50) NOT NULL,
    -- 주어진 시간 동안 페이지 뷰 수 저장
    pageviewcount INT NOT NULL,
    datetime TIMESTAMP NOT NULL
);
```

```sql
-- 3. DB에 값 쓰기
--     - PythonOperator는 결과를 출력하지만 직접 값을 쓰지는 않기 때문에 INSERT INTO가 
--       필요하다.
INSERT INTO pageview_counts VALUES ('Google', 333, '2019-07-17T00:00:00');
```

```bash
# 1. postgres에 데이터를 저장하기 위해 postgres 설치
#   - Airflow 2 이후 대부분의 오퍼레이터들은 pip 패키지를 통해 설치한다.
#   - pip 패키지를 이용하면 필요한 Airflow 패키지만 설치가 가능하다.
pip install apache-airflow-providers-postgres
```

```python
# 2. PostgresOperator에 공급할 INSERT 구문 작성
#   - Airflow의 PostgresOperator는 SQL을 실행할 수 있지만,
#     파이썬 함수가 직접 Postgres에 데이터를 쓰는 기능은 없다.
#   - 따라서 페이지뷰 데이터를 읽어 SQL INSERT 구문으로 변환하고,
#     이를 .sql 파일에 저장한 뒤 PostgresOperator에서 실행하도록 준비한다.
def _fetch_pageviews(pagename, execution_date, **_):
    # pagenames에 있는 페이지 이름을 키로 하고, 기본값 0으로 초기화
    result=dict.fromkeys(pagenames, 0)

    # 압축 해제된 페이지뷰 파일 읽기
    with open("/tmp/wikipageviews", "r") as f:
        for line in f:
            # 한 줄 구조: "도메인코드 페이지제목 조회수 기타"
            domain_code, page_title, view_counts, _=line.split(" ")
            # 영어 위키(en)이고 관심있는 페이지인 경우에만 카운트 기록
            if domain_code == "en" and page_title in pagenames:
                result[page_title]=view_counts
    
    # PostgresOperator에 공급할 SQL INSERT 문을 생성해 .sql 파일에 저장
    with open("/tmp/postgres_query.sql", "w") as f:
        for pagename, pageviewcount in result.items():
            f.write(
                "INSERT INTO pageview_counts VALUES ("
                f"'{pagename}', {pageviewcount}, '{execution_date}'"
                ");\n"
            )

# PythonOperator: 위 함수 실행 → .sql 파일 생성
fetch_pageviews=PythonOperator(
    task_id="fetch_pageviews",
    python_callable=_fetch_pageviews,
    op_kwargs={"pagenames": {"Google", "Amazon", "Apple", "Microsoft", "Facebook"}},
    dag=dag
)
```

```python
# 3. PostgresOperator를 호출.
from airflow.providers.postgres.operators.postgres import PostgresOperator

# DAG 정의 시 template_searchpath를 "/tmp"로 지정
#   - Airflow는 sql 인자가 파일명일 경우, template_searchpath에서 해당 파일을 찾아 실
#     행한다.
#   - 즉, 앞서 PythonOperator가 생성한 /tmp/postgres_query.sql 파일을 찾아 실행할 수 
#     있다.
dag=DAG(..., template_searchpath="/tmp")

# PostgresOperator 정의
write_to_postgres=PostgresOperator(
    task_id="write_to_postgres",
    # Airflow Connections에 등록된 Postgres 연결 ID
    postgres_conn_id="my_postgres",
    # 실행할 SQL 파일 이름 (template_searchpath 기준 탐색)
    sql="postgres_query.sql",
    dag=dag
)

"""CLI 방식
airflow connections add \
    --conn-type postgres \
    --conn-host localhost \
    --conn-login postgres \
    --conn-password mysecretpassword \
    my_postgres # 연결 식별자
"""
```

```sql
-- 페이지당 가장 인기 있는 시간을 확인하는 SQL 쿼리.
SELECT x.pagename, x.hr AS "hour", x.average AS "average pageviews"
FROM (
    SELECT 
        pagename,
        date_part('hour', datetime) AS hr,
        AVG(pageviewcount) AS average,
        ROW_NUMBER() OVER (PARTITION BY pagename ORDER BY AVG(pageviewcount) DESC)
    FROM pageview_counts
    GROUP BY pagename, hr
) AS x
WHERE row_number=1;
```