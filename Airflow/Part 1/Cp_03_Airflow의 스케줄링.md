<ul>
  <li>
    일정한 간격으로 DGA를 실행하기
  </li>
  <li>
    증분 데이터를 처리하기 위한 동적 DAG 구성하기
  </li>
  <li>
    과거의 데이터 세트를 적재 및 재처리하기
  </li>
  <li>
    신뢰할 수 있는 태스크를 위한 모범 사례 적용하기
  </li>
</ul>

<br>

<h1>1. 예시: 사용자 이벤트 처리하기</h1>

```python
# 1. 웹사이트에서 사용자 동작을 추적하고 사용자가 웹사이트에서 액세스한 페이지를 분석할 수 
#    있는 서비스를 가정.

import datetime as dt from pathlib import Path

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

dag=DAG(
    dag_id="01_unscheduled",
    # DAG의 시작 날짜를 정의
    start_data=dt.datetime(2019, 1, 1),
    # 스케줄되지 않는 DAG로 지정
    schedul_interval=None 
)

fetch_events=BashOperator(
    task_id="fetch_events",
    # API에서 이벤트를 가져온 후 저장
    bash_command=(
        "mkdir -p /data && "
        "curl -o /data/events.json "
        "https://localhost:5000/events"
    ),
    dag=dag
)

# 이번트 데이터에 대해 필요한 통계를 계산하고 출력 디렉터리에 CSV 파일로 저장.
def _calculate_stats(input_path, output_path):
    """이벤트 통계 계산하기"""
    events=pd.read_json(input_path)
    stats=events.groupby(["date", "user"]).size().reset_index()
    # 출력 디렉터리에 저장.
    Path(output_path).parent.mkdir(exist_ok=True)
    stats.to_csv(output_path, index=False)

# PythonOperator를 통해 파이썬 스크립트로 상단의 함수 실행.
calculate_stats=PythonOperator(
    task_id="calculate_stats",
    # 정의한 함수 사용.
    python_callable=_calculate_stats,
    op_kwargs={
        "input_path": "/data/events.json",
        "output_path": "/data/stats.csv",
    },
    dag=dag
)

# 실생 순서 설정
fetch_events >> calculate_stats
```

<br><br>

<h1>2. 정기적으로 실행하기</h1>
<ul>
  <li>
    DAG를 초기화할 때 <strong>schedule_interval</strong> 인수를 설정하여 스케줄 간격을 정의할 수 있다.
  </li>
    <ul>
      <li>
        디폴트 값은 None이며 DAG가 예약 실행되지 않고, UI 또는 API르 통해 <strong>수동으로 트리거</strong>를 실행한다.
      </li>
    </ul>
</ul>

<br>

<h2>2-1. 스케줄 간격 정의하기</h2>
<ul>
  <li>
    Airflow는 <strong>@daily 매크로</strong>를 설정하여 매일 자정에 DAG를 실행하도록 예약할 수 있다.
  </li>
  <li>
    DAG 시작 날짜를 지정하여 Airflow가 <strong>언제부터 시작할지</strong>를 설정한다. Airflow는 시작 날짜를 기준으로 <strong>첫 번째 DAG의 실행 스케줄(시작 날짜 + 간격)</strong>을 정한 뒤 간격에 맞추어 정기적으로 수행한다.
  </li>
  <li>
    종료일이 없으면 DAG는 매일 스케줄된 대로 <strong>영원히 실행</strong>한다. 특정 날짜 이후 <strong>DAG 실행을 중지</strong>하도록 설정하려면 <strong>end_date 인수</strong>를 활용할 수 있다.
  </li>
</ul>

```python
# 1. @daily 매크로를 통해 매일 자정에 수행되도록 설정.

dag=DAG(
    dag_id="02_daily_schedule",
    # @daily 매크로를 통해 매일 자정에 실행되도록 설정
    schedule_interval="@daily",
    # DAG 실행 스케줄을 시작할 날짜/시간 지정
    start_date=dt.datetime(2019, 1, 1,) 
)

"""중략"""
```

```python
# 2. end_date 인수를 활용하여 DAG의 종료날짜 지정.

dag=DAG(
    dag_id="03_with_end_date",
    schedule_interval="@daily",
    start_date=dt.datetime(year=2019, month=1, day=1),
    # 2019-01-02 ~ 2019-01-05 (총 4 번)
    end_date=dt.datetime(year=2019, month=1, day=5),
)

"""중략"""
```

<br>

<h2>2-2. Cron 기반의 스케줄 간격 설정하기</h2>
<ul>
  <li>
    <strong>Cron</strong>에는 <strong>다섯 개의 구성 요소</strong>가 있으며 좀 더 복잡한 실행 주기를 설정할 수 있다.
  </li>
  <li>
    cron job은 시간/날짜가 <strong>해당 필드의 값</strong>과 <strong>시스템 시간</strong>이 일치할 때 실행된다.
  </li>
  <li>
    숫자 대신 <strong>에스터리스크(별표, *)</strong>로 <strong>제한되지 않은 필드</strong>를 정의할 수 있으며 이는 해당 시간은 신경쓰지 않음을 의미한다.
  </li>
  <li>
    <strong>* * * * *</strong>
  </li>
    <ul>
      <li>
        분 (0 ~ 59)
      </li>
      <li>
        시간 (0 ~ 23)
      </li>
      <li>
        일 (1 ~ 31)
      </li>
      <li>
        월 (1 ~ 12)
      </li>
      <li>
        요일 (0: 일요일 ~ 6: 토요일), 일부 시스템은 7이 일요일이다.
      </li>
    </ul>
  <li>
    cron 식을 사용할 때 <strong>콤마(쉼표, ",")</strong>를 사용하여 <strong>값의 리스트</strong>를 정의하거나 <strong>대시("-")</strong>를 사용하여 <strong>값의 범위를 정의</strong>하는 값의 집합을 지정할 수 있다.
  </li>
  <li>
    책에는 @daily를 포함하여 자주 사용하는 매크로를 정리한 장표가 있다(p46).
  </li>
  <li>
    cron 식은 기능이 좋은 만큼 복잡하기에 적용전 문서화를 하거나 cron 식을 검증 또는 설명하는 도구를 활용하는 것이 좋다.
  </li>
</ul>

```python
# 1. Cron 표현식 예

# 매시간(정시에 실행)
"0 * * * *"

# 매일(자정에 실행)
"0 0 * * *"

# 매주(일요일 자정에 실행)
"0 0 * * 0"

# 매월 1일 자정
"0 0 1 * *"

# 매주 토요일 23시 45분
"45 23 * * SAT"
```

```python
# 2. 쉼표와 하이픈을 이용한 cron 식 예

# 쉼표
# 매주 월, 화, 금요일 자정에 실행
"0 0 * * MON, WED, FRI"

# 매일 자정 및 호후 12시에 실행
"0 0,12 * * *"

# 매주 월요일부터 금요일 자정에 실행
"0 0 * * MON-FRI"
```

<br>

<h2>2-3. 빈도 기반의 스케줄 간격 설정하기</h2>
<ul>
  <li>
    cron 식은 <strong>패턴과 일치</strong>하는 현재 시간을 지속적으로 확인하기 위한 정의이기에 <strong>이전 작업이 실행된 시점</strong>을 기억하지 않는다. 따라서 빈도를 기반으로 스케줄링이 불가하다.
  </li>
  <li>
    <strong>빈도를 기반</strong>으로 스케줄을 사용할 때에는 <strong>timedelta</strong>(표준 라이브러리인 datetime 모듈에 포함) 인스턴스를 사용한다.
  </li>
</ul>

```python
# 1. timedelta를 활용한 빈도 기반 스케줄링.
dag=DAG(
    dag_id="04_time_delta",
    # timedelta를 3으로 설정하여 3일에 한 번 수행되도록 설정.
    schedule_interval=dt.timedelta(days=3),
    start_data=dt.datetime(year=2019, month=1, day=1),
    end_date=dt.datetime(year=2019, month=1, day=5),
)

"""중략"""
```

<br><br>

<h1>3. 데이터 증분 처리하기</h1>
<ul>
  <li>
    <strong>증분</strong>이란 모든 데이터를 받아오는 것이 아니라 <strong>새로 추가 혹은 변경된 데이터</strong>만 가져오는 것을 의미한다.
  </li>
</ul>

<br>

<h2>3-1. 이벤트 데이터 증분 가져오기</h2>
<ul>
  <li>
    증분 방식(incremental approach)은 스케줄된 하나의 작업에서 처리해야 할 데이터 양을 크게 줄일 수 있어 효율적이다.
  </li>
</ul>

```python
# 1. API의 날짜를 수정하여 증분 처리하도록 설정.
#   - 2019-01-01와 2019-01-02로 설정.
#   - 2019-01-01 00:00:00 ~ 2019-01-01 23:59:59의 데이터를 가져온다.

"""중략"""

fetch_events=BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /data && "
        "curl -o /data/events.json "
        "http://localhost:5000/events?"
        "start_date=2019-01-01&"
        "end_date=2019-01-02"
    ),
    dag=dag,
)

"""중략"""
```

<br>

<h2>3-2. 실행 날짜를 사용하여 동적 시간 참조하기</h2>
<ul>
  <li>
    <strong>시간 기반 프로세스(time-based process)</strong> 워크플로의 경우, 주어진 작업이 실행되는 <strong>시간 간격</strong>을 아는 것이 중요하다.
  </li>
  <li>
    Airflow는 태스크가 실행되는 특정 간격을 정의하는 추가 매개변수를 제공한다.
  </li>
    <ul>
      <li>
        <strong>execution_date</strong>
      </li>
        <ul>
          <li>
            DAG가 실행되는 <strong>날짜와 시간</strong>을 나타낸다.
          </li>
          <li>
            시작 시간의 특정 날짜가 아니라 <strong>스케줄 간격</strong>으로 실행되는 시작 시간을 나타내는 타임스탬프이다.
          </li>
        </ul>
      <li>
        <strong>next_execution_date</strong>
      </li>
        <ul>
          <li>
            스케줄 간격의 <strong>종료 시간</strong>을 정의한다.
          </li>
        </ul>
      <li>
        <strong>previous_execution_date</strong>
      </li>
        <ul>
          <li>
            <strong>과거</strong>의 스케줄 간격의 시작을 정의한다.
          </li>
          <li>
            현재 시간 간격의 데이터와 <strong>이전 간격의 데이터를 대조</strong>하여 분석을 수행할 때 유용하다.
          </li>
        </ul>
    </ul>
  <li>
    Airflow는 일반적인 날짜 형식에 댛 여러 축약 매개변수(shorthand parameters)를 제공한다.
  </li>
    <ul>
      <li>
        축약 매개변수는 익숙해지면 사용하기 편하지만 복잡한 날짜 형식의 경우(혹은 datetime) 유연하게 표현할 수 있는 <strong>strftime 메서드</strong>가 유요할 수 있다.
      </li>
    </ul>
</ul>

```python
# 1. 특정 날짜 지정을 위한 템플릿.
#   - execution_date와 next_execution_date 활용
#   - {}는 특정 맥변수를 참조하는 표현이다.

"""중략"""

fetch_events=BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /data && "
        "curl -o /data/events.json "
        "http://localhost:5000/events?"
        # strftime: 문자열 형식으로 반환 형식을 지정
        "start_date={{execution_date.strftime('%Y-%m-%d')}}
        "&end_date={{next_execution_date.strftime('%Y-%m-%d')}}
    ),
    dag=dag
)

"""중략"""
```

<br>

<h2>3-3. 데이터 파티셔닝</h2>
<ul>
  <li>
    데이터를 <strong>어떤 단위</strong>로 적재를 할 것인가를 결정하는 데에는 몇 가지 방법들을 고려할 수 있다.
  </li>
  <li>
    데이터 세트를 이처럼 관리하기 쉬운 조각으로 나누는 방벙은 <strong>파티셔닝(partitioning)</strong>이라고 하며 이렇게 나누어진 작은 부분은 <strong>파티션(partition)</strong>이라 한다.
  </li>
</ul>

```python
# 1. 날짜 별로 파일을 만들어 일일 배치처리.
fetch_events=BashOperator(
    task_id="fetch_events",
    bash_command=(
        "mkdir -p /data/events && "
        # 일단위로 반환된 값이 파일명이 된다.
        "curl -o /data/events/{{ds}}.json "
        "http://localhost:5000/events?"
        "start_date={{ds}}&"
        "end_date={{nect_ds}}",
    dag=dag
    )
)
```

```python
# 2. 파티셔닝된 데이터를 통해 파티션 별로 통계 계산
# 모든 컨텍스트 변수를 수신한다.
def _calculate_stats(**context):
    """Calculates event statistics."""

    # templates_dict 개체에서 템플릿 값을 검색한다.
    #     - 이후 PythonOperator에서 템플릿 값을 전달한다.
    input_path=context["templates_dict"]["input_path"]
    output_path=context["templates_dict"]["output_path"]
    Path(output_path).parent.mkdir(exist_ok=True)

    events=pd.read_json(input_path)
    stats=events.groupby(["data", "user"]).size().reset_index()
    stats.to_csv(output_path, index=False)
  
calculate_stats=PythonOperator(
    task_id="calculate_stats",
    python_callable=_calculate_stats,
    # 함수에 전달될 템플릿 값을 정의한다.
    templates_dict={
        "input_path": "/data/events/{{ ds }}.json",
        "output_path": "/data/stats/{{ ds }}.csv",
    },
    dag=dag
)

# 템플릿
#   - 보일러플레이트(boilerplate) 코드 작성
#       - 여러 곳에 필수적으로 사용되는 코드를 의미하며 수정하지 않거나 최소의 수정만 하도
#         록 설계한다.
#   - PythonOperator에서 템플릿을 구현하려면 오퍼레이터의 templates_dist 매개변수를 사
#     용하여 템플릿화 해야하는 모든 인수를 전달한다.
```

<br><br>

<h1>4. Airflow의 실행 날짜 이해</h1>
<h2>4-1. 고정된 스케줄 간격으로 태스크 실행</h2>
<ul>
  <li>
    <strong>간격 기반 스케줄링</strong>은 이전 실행을 기준으로 일정 간격 후 실행되므로, <strong>작업 실행 시간까지 포함</strong>하여 주기를 계산한다. 반면 <strong>시점 기반 스케줄링</strong>은 캘린더 시점을 기준으로 트리거되며, Airflow의 작업 처리 시간과 관계없이 <strong>지정한 시점</strong>에 실행되도록 설계된다.
  </li>
  <li>
    간격 기반 접근 방식은 작업이 <strong>실행되는 시간 간격(시작과 끝)</strong>을 정확히 알 수 있다.
  </li>
    <ul>
      <li>
        <strong>간격 기반 스케줄링</strong>은 이전 실행 시점을 기준으로 다음 주기를 계산하므로, 자연스럽게 <strong>증분 처리(Incremental Processing)</strong>에 적합하다.
      </li>
      <li>
        반면 <strong>cron 기반</strong> 스케줄링은 고정된 시점에 실행되므로, 증분 처리를 위해서는 execution_date(예: {{ ds }})를 활용해 <strong>처리 구간을 명시적으로 계산</strong>해야 한다.
      </li>
    </ul>
  <li>
    시점 기반 방식으로도 증분 처리가 되지만 정확한 증분을 위해서는 <strong>airflow 작업 끝 시간</strong>을 기준으로하는 것이 좋다는 의미이다.
  </li>
  <li>
    간격 기반 스케줄링에서는 <strong>시작 시점(start_date)</strong>을 잘 결정해야 한다. 
    Airflow의 실행은 지정한 시점 자체가 아니라, <strong>해당 시점을 지난 직후</strong>에 트리거된다.
  </li>
    <ul>
      <li>
        예를 들어 <strong>start_date=2019-01-03</strong>으로 설정하고 
        <strong>timedelta(days=1)</strong> 간격을 주면, 첫 DAG 실행은 2019-01-04 00:00에 발생한다.
      </li>
    </ul>
  <li>
    Airflow 실행 날짜를 <strong>해당 스케줄 간격의 시작</strong>으로 생각해 정의하면 특정 간격의 시작과 끝을 유추할 때 사용할 수 있다.
  </li>
    <ul>
      <li>
        현재 스케줄 간격 = |execution_date - next_execution|
      </li>
      <li>
        현재 스케줄 범위 = [execution_date, next_execution) 
      </li>
      <li>
        이전 스케줄 간격 = |previous_execution_date - execution_date|
      </li>
      <li>
        이전 스케줄 범위 = [previous_execution_date, execution_date)
      </li>
    </ul>
  <li>
    previous_execution_date 및 next_execution_date 매개변수는 <strong>DAG 실행</strong>을 통해서만 정의되기에 <strong>Airflow UI 또는 CLI</strong>를 통해 수동으로 실행할 경우 <strong>매개변수의 값이 정의되지 않는다</strong>.
  </li>
</ul>

<br><br>

<h1>5. 과거 데이터 간격을 메꾸기 위해 백필 사용하기</h1>
<ul>
  <li>
    Airflow는 임의의 날짜로부터 스케줄 간격을 정의할 수 있기에 <strong>백필(bacdfilling)</strong>을 활용하여 DAG를 과거 시점으로 지정하여 <strong>과거 데이터 세트</strong>를 다룰 수 있다.
  </li>
</ul>

<br>

<h2>5-1. 과거 시점의 작업 실행하기</h2>
<ul>
  <li>
    Airflow는 아직 실행되지 않은 과거 스케줄 간격을 예약하고 실행하기에 <strong>과거 시작 이후의 모든 스케줄 간격</strong>이 생성된다.
  </li>
  <li>
    해당 기능은 DAG의 <strong>catchup 매개변수</strong>에 의해 제어되며 catchup을 false로 설정하면 비활성화 할 수 있다.
  </li>
    <ul>
      <li>
        <strong>False</strong>: 과거 실행일들을 건너뛰고 DAG를 켜는 시점부터 <strong>앞으로의 실행</strong>만 수행.
      </li>
      <li>
        <strong>True</strong>: start_date부터 현재까지 모든 주기별 실행일(schedule interval)을 따라가며 <strong>과거 태스크도 전부 실행</strong>.
      </li>
    </ul>
</ul>

```python
# 1. 과거 시점의 태스크 실행을 피하기 위해 catchup 비활성화.
dag=DAG(
    dag_id="09_no_catchup",
    schedule_interval="@daily",
    start_date=dt.datetime(year=2019, month=1, day=1),
    end_date=dt.datetime(year=2019, month=1, day=5),\
    # 과거 태스크 실행 X. (백필 수행 안함).
    catchup=False
)
```

<br><br>

<h1>6. 태스크 디자인을 위한 모범 사례</h1>
<ul>
  <li>
    Airflow의 <strong>원자성(atomicity)</strong>과 <strong>멱등성(idempotency)</strong>을 살펴 본다.
  </li>
</ul>

<br>

<h2>6-1. 원자성</h2>
<ul>
  <li>
    <strong>원자성</strong>은 모든 <strong>발생하거나 발생하지 않는, 나눌 수 없고 돌이킬 수 없는</strong> 일련의 데이터베이스와 같은 작업으로 간주된다.
  </li>
  <li>
    즉, Airflow는 성공적으로 <strong>결과를 생성</strong>하거나 시스템에 영향을 미치지 않고 <strong>실패</strong>하도록 정의한다.
  </li>
  <li>
    완전한 원자성은 아니기에 일정 정도 수행이되는 경우도 있는 듯하다.
  </li>
  <li>
    <strong>의존성</strong>이 문제가 될 경우에는 오히려 단일 태스크 내에 여러 <strong>작업들을 담아 하나의 일관된 태스크 단위</strong>를 형성하는 것이 나을 수도 있다.
  </li>
  <li>
    대부분 Airflow 오퍼레이터는 이미 원자성을 유지하도록 설계되어 있다.
  </li>
</ul>

```python
# 1. 하나의 태스크 내의 두 작업 → 원자성 불충족
#   - CSV 작성 후 이메일을 보내면 단일 태스크 내에서 두 가지 작업을 하기에 원자성이 깨진다.
def _calculate_stats(**context):
    
    """이벤트 데이터 통계 계산하기"""
    input_path=context["templates_dict"]["input_path"]
    output_path=context["templates_dict"]["output_path"]

    events=pd.read_json(input_path)
    stats=events.groupby(["date", "user"]).size().reset_index()

    # CSV 작성
    stats.to_csv(output_path, index=False)

    # 이메일 전송
    email_stats(stats, email="user@example.com")

    calculate_stats >> email_stats
```

```python
# 2. 이메일 발송 기능을 별도의 태스크로 분리하여 원자성 보장.
#   - 보내기만 하는 함수를 생성하여 CSV작성과 이메일 작성을 분리.
def _send_stats(email, **context):
  stats=pd.read_csv(context["templates_dict"]["stats_path"])
  email_stats(stats, email=email)

send_stats=PythonOperator( python_callable=_send_stats,
    task_id="send_stats",
    op_kwargs={"email": "user@example.com"},
    templates_dict={"stats_path": "/data/stats/{{ ds }}.csv"},
    dag=dag,
)

calculate_stats >> send_stats
```

<br>

<h2>6-2. 멱등성</h2>
<ul>
  <li>
    <strong>멱등성</strong>이란 특정 연산을 <strong>여러 번 반복</strong>해서 실행해도 결과가 <strong>한 번</strong> 실행했을 때와 동일하게 유지되는 성질을 의미한다.
  </li>
  <li>
    데이터를 쓰는 태스크는 <strong>기존 결과를 확인</strong>하거나 이전 태스크 결과를 <strong>덮어쓸지 여부</strong>를 확인하여 멱등성을 유지할 수 있다.
  </li>
</ul>