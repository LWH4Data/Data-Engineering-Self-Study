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