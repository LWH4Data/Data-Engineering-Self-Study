<ul>
  <li>
    개인 PC에서 Airflow 실행하기
  </li>
  <li>
    첫 번째 워크플로 작성 및 실행하기
  </li>
  <li>
    Airflow 인터페이스에서 첫 번째 뷰 내용 검토하기
  </li>
  <li>
    Airflow에서 실패한 태스크 처리하기
  </li>
</ul>

<br>

<h1>1. 다양한 소스에서 데이터 수집</h1>
<ul>
  <li>
    John이 로켓에 대한 모든 뉴스를 한 곳에 수집하여 로켓 발사에 대해 간파할 수 있도록 하는 프로그램을 작성하는 실습.
  </li>
</ul>

<br>

<h2>1-1. 데이터 탐색</h2>
<ul>
  <li>
    Launch Library 2(https://thespacedevs.com/llapi)를 사용한다.
  </li>
    <ul>
      <li>
        예정되어 있는 10 개의 로켓 발사에 대한 데이터와 로켓 이미지에 대한 URL을 제공한다.
      </li>
    </ul>
  <li>
    JSON 형식으로 되어 있으면서 로켓의 ID, 이름, 이미지 URL과 같은 로켓 발사 정보를 제공한다.
  </li>
</ul>

<br><br>

<h1>2. 첫 번째 Airflow DAG 작성</h1>
<ul>
  <li>
    Airflow는 하나 이상의 단계로 구성된 대규모 작업을 <strong>개별 태스크</strong>로 분할하고 DAG로 형성할 수 있다.
  </li>
  <li>
    다중 task는 병렬적으로 실행이 가능하며 <strong>서로 다른 기술</strong>을 사용할 수 있다.
  </li>
    <ul>
      <li>
        예를 들면 현재 작업은 python 스크립트로 진행하지만 업스트림의 작업은 bash 스크립트로 진행이 가능하다.
      </li>
    </ul>
  <li>
    task의 단계를 구분하는 것에는 정답이 없으며 몇 가지 고려사항만 존재한다. 고려사항들은 책 전체에서 다룬다.
  </li>
</ul>

```python
# 1. 로켓 발사 데이터 다운로드 및 처리를 위한 DAG.
import json
import pathlib

import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

# 객체의 인스턴스 생성 - 모든 워크플로의 시작점.
#   - DAG 클래스를 구체화하여 dag 인스턴스 생성.
dag=DAG(
    # DAG 이름
    dag_id="download_rocket_launches",
    # DAG 처음 실행 시작 날짜
    start_date=airflow.utils.dates.days_ago(14),
    # DAG 실행 간격 (None: 자동으로 DAG가 실행되지 않음).
    schedule_interval=None,
)

# BashOperator를 이용해 curl로 URL 결괏값 다운로드
download_launches=BashOperator(
    # 태스크의 이름
    task_id="download_launches",
    # 실행할 배시 커맨드
    bash_command="curl -o /tmp/launches.json -L
        'https://ll.thespacedevs.com/2.0.0/launch/upcoming'", dag=dag,
)

# 함수: 결괏값을 파싱하고 모든 로켓 사진을 다운로드
def _get_pictures():
    # 경로가 존재하는지 확인.
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)

    # launches.json 파일에 있는 모든 그림 파일을 다운로드
    # 로켓 발사 JSON 파일 열기
    with open("/tmp/launches.json") as f:
        # 데이터를 섞을 수 있도록 dictionary로 열기
        launches=json.load(f)
        
        # 모든 발사에 대한 image의 URL 값 읽기
        image_urls=[launch["image"] for launch in launches["results"]]

        # 모든 이미지 URL을 얻기 위한 for loop
        for image_url in image_urls:
            try:
                # 이미지 가져오기.
                response=requests.get(image_url)
                
                # 마지막 파일 이름만 필터링
                image_filename=image_url.split("/")[-1]

                # 타깃 파일 저장 경로 구성
                target_file=f"/tmp/images/{image_filename}"

                # 타깃 파일 핸들 열기
                with open(target_file, "wb") as f:
                    # 파일 경로에 이미지 쓰기
                    f.write(response.content)
                
                # 결과 출력
                print(f"Downloaded {image_url} to {target_file}")
            
            # 잠재적인 error 관리
            except requests_exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL.")
            except requests_exceptions.ConnectionError:
                print(f"Could not connect to {image_url}.")

# python 함수를 호출하여 DAG 실행
get_pictures=PythonOperator(
    task_id="get_pictures",
    python_callable=_get_pictures,
    dag=dag,
)

notify=BashOperator(
    task_id="notify",
    bash_command='echo "There are now $(ls /tmp/images/ | wc -l) images."',
    dag=dag,
)

# 테스크 실행 순서 설정.
#   - >>(오른쪽 시프트 연산자): 의존성(dependency)을 나타낸다.
#   - python에서는 >> 비트연산자 이지만 Airflow에서는 의존성을 의미한다.
download_launches >> get_pictures >> notify
```

<br>

<h2>2-1. 태스크와 오퍼레이터 차이점</h2>
<ul>
  <li>
    <strong>오퍼레이터(operator)</strong>는 <strong>단일 작업 수행</strong> 역할을 한다.
  </li>
  <li>
    <strong>DAG</strong>는 오퍼레이터 집합에 대한 <strong>실행을 오케스트레이션(orchestration, 조정 혹은 조율)</strong>하는 역할을 한다.
  </li>
  <li>
    <strong>오퍼레이터</strong>는 사용자 관점에서 <strong>단일 작업을 수행할 수 있는 기능</strong>을 의미하고, <strong>태스크</strong>는 Airflow 관점에서 오퍼레이터의 래퍼(wrapper) 또는 매니저(manager)로 생각해 볼 수 있다. 즉, <strong>오퍼레이터의 상태를 관리하고 사용자에게 상태를 표시하는 내장 컴포넌트</strong>이다.
  </li>
</ul>

<br>

<h2>2-2. 임의 파이썬 코드 실행</h2>
<ul>
  <li>
    다른 스크립트를 사용하더라도 Airflow는 워크플로와 실행 로직을 <strong>동일한 스크립트</strong>에 작성하는 것이 편리하다.
  </li>
    <ul>
      <li>
        이전 코드에서 <strong>'BashOperator 실행 - python 함수 정의 - PythonOperator 실행'</strong>과 같이 하나의 스트립트에 워크플로와 실행 로직을 한 번에 작성한다.
      </li>
    </ul>
  <li>
    모든 오퍼레이터들은 <strong>task_id</strong>가 필요하며 task_id는 테스크 실행 시에 참조되어 Airflow UI에도 표시된다.
  </li>
  <li>
    <strong>PythonOperator</strong>는 두 가지 사항을 적용해야 한다.
  </li>
    <ul>
      <li>
        오퍼레이터에 <strong>자신(get_pictures)</strong>을 정의해야 한다.
      </li>
      <li>
        <strong>python_callable</strong>은 인수에 <strong>호출이 가능한 일반 함수(_get_pictures)</strong>를 가리킨다.
      </li>
    </ul>
  <li>
    자세한 내용은 이전의 코드에 <strong>주석</strong>으로 정리해 두었다.
  </li>
</ul>

```python
# 1. PythonOperator 예

# 작업 실행을 내포하는 함수 정의
def _get_pictures():
    # 작업 실행 코드 작성
    return

# PythonOperator 실행 정의
get_pictures = PythonOperator(
    task_id="get_pictures",
    # python_callable에 호출 가능한 일반 함수 지정.
    python_callable = _get_pictures,
    dag=dag
)
```

<br><br>

<h1>2-3. Airflow에서 DAG 실행하기</h1>
<ul>
  <li>
    Airflow는 <strong>스케줄러</strong>, <strong>웹 서버</strong> 그리고 <strong>데이터베이스</strong> 세 가지 핵심 컴포넌트로 구성된다.
  </li>
</ul>

<br>

<h2>3-1. 파이썬 환경에서 Airflow 실행</h2>
<ul>
  <li>
    PyPi를 통해 파이썬 패키지인 Airflow를 설치하고 실행한다. (2016년 아파치 재단에 가입하면서 apahce-airflow가 되었다).
  </li>
  <li>
    파이썬 프로젝트에서 각 프로젝트를 특정 파이썬 환경을 유지하고 재사용할 수 있도록 패키징하여 종속성 충돌을 예방한다.
  </li>
    <ul>
      <li>
        pyenv: https://github.com/pyenv/pyenv
      </li>
      <li>
        Conda: https://docs.conda.io
      </li>
      <li>
        virtualenv: https://virtualenv.pypa.io
      </li>
    </ul>
</ul>

```python
# 1. 패키지 설치.
pip install apache-airflow
```

```bash
# 2. Airflow 실행

# 메타스토어(Airflow 상태를 저장하는 데이터베이스) 초기화
airflow db init

# 사용자 생성.
airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email addmin@example.org

# 로켓 발사 DAG를 DAG 디렉터리에 복사
cp download_rocket_launches.py ~/airflow/dags/

# 웹 서버 실행
airflow webserver

# 스케줄러 실행
airflow scheduler

# localhost:8080으로 접속한 뒤 user와 password 모두 admin을 입력하고 접속.
```

<br>

<h2>3-2. 도커 컨테이너에서 Airflow 실행하기</h2>

```bash
# 1. Airflow-prac 폴더를 만들고 실행.
#   - dags 폴더를 내부에 만들고 DAG 관리.
docker run -it --name airflow -p 8080:8080 \
  -v /mnt/c/Users/SSAFY/Desktop/Airflow-prac:/opt/airflow/dags \
  --entrypoint /bin/bash \
  apache/airflow:2.0.0-python3.8 \
  -c 'airflow db init && \
      airflow users create \
        --username admin \
        --password admin \
        --firstname Anonymous \
        --lastname Admin \
        --role Admin \
        --email admin@example.org ; \
      airflow webserver -p 8080 & \
      airflow scheduler'
```

<br>

<h2>3-3. Airflow UI 둘러보기</h2>
<ul>
  <li>
    Airflow <strong>http://localhost:8080</strong> 으로 접속하여 UI를 확인할 수 있다.
  </li>
  <li>
    지정한 username(admin)과 password(admin)으로 로그인하면 바인드 마운트 경로의 <strong>DAG</strong>를 확인할 수 있다.
  </li>
  <li>
    DAG 이름을 클릭하면 <strong>그래프 뷰 화면</strong>을 확인할 수 있다.
  </li>
    <ul>
      <li>
        뷰에서는 DAG의 <strong>모든 구조</strong>와 <strong>모든 태스크</strong> 실행 순서와 실행 방법을 연결해 보여준다.
      </li>
    </ul>
  <li>
    <strong>상태 범례(state legend)</strong>는 실행 시에 볼 수 있는 모든 <strong>상태 색상</strong>을 표시한다.
  </li>
  <li>
    <strong>토글 버튼</strong>을 누르고 <strong>재생 버튼</strong>을 눌러 시행한다.
  </li>
  <li>
    Graph 뷰의 태스크를 클릭하면 해당 태스크의 결과를 확인할 수 있다.
  </li>
    <ul>
      <li>
        몇 가지 값을 선택할 수 있는데 Log를 선택하면 로그를 출력해 볼 수 있다.
      </li>
    </ul>
  <li>
    Docker로 실행할 경우 실행 결과는 Docker 내부에 적재된다.
  </li>
</ul>

<br><br>

<h1>4. 스케줄 간격으로 실행하기</h1>
<ul>
  <li>
    Airflow에서는 DAG를 일정 시간 간격으로 실행할 수 있도록 <strong>스케줄 설정</strong>이 가능하다.
  </li>
    <ul>
      <li>
        DAG의 <strong>schedule_interval</strong>의 인수를 설정하면 된다.
      </li>
    </ul>
  <li>
    <strong>트리 뷰</strong>는 그래프 뷰와 유사하지만 <strong>시간 경과</strong>에 따라 실행되는 그래프 구조를 표시한다. 단일 워크플로의 모든 실행 상태에 대한 개요를 볼 수 있다.
  </li>
  <li>
    <strong>start_date가 과거값</strong>으로 들어오면 해당 시점부터 주어진 <strong>간격(schedule_intervals)에 맞추어 DAG를 실행한다. 
  </li>
</ul>

```python
# 1. 하루에 한 번 DAG 실행.
dag=DAG(
    dag_id="download_rocket_launches",
    start_date=airflow.utils.dates.days_ago(14),
    # 하루에 한 번 자동 실행(Trigger가 필요 없다).
    schedule_interval="@daily"
)
```

<br><br>

<h1>5. 실패한 태스크에 대한 처리</h1>
<ul>
  <li>
    <strong>실패</strong>한 특정 태스크는 그래프 뷰와 트리 뷰에 모두 <strong>빨간색</strong>으로 표시된다.
  </li>
  <li>
    <strong>의존성</strong>으로 인해 수행되지 못하는 태스크는 <strong>주황색</strong>으로 표시된다.
  </li>
  <li>
    태스크의 <strong>로그</strong>를 열어 어떤 이유로 태스크가 실패했는지 확인할 수 있다.
  </li>
  <li>
    디버깅을 완료한 태스크는 해당 태스크를 선택하여 <strong>Clear 버튼</strong>을 클릭한 뒤 해당 태스크부터 태스크를 <strong>재실행</strong>할 수 있다.
  </li>
</ul>
