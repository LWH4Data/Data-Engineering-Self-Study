<ul>
  <li>
    Airflow 스케줄러 분석
  </li>
  <li>
    서로 다른 익스큐터(executor)를 사용하여 수평적으로 확장할 수 있는 Airflow 구성.
  </li>
  <li>
    Airflow의 환경 및 성능을 시각적으로 모니터링
  </li>
  <li>
    작업 실패 시 알림 방송
  </li>
</ul>

<br>

<h1>1. Airflow 아키텍처</h1>
<ul>
  <li>
    Airflow는 최소 구성 요건으로 <strong>웹 서버</strong>, <strong>스케줄러</strong> 그리고 <strong>데이터베이스</strong> 세 가지 요소를 갖추고 있다.z
  </li>
    <ul>
      <li>
        웹 서버와 스케줄러는 Airflow의 프로세스이다. 반면 <strong>데이터베이스</strong>는 웹 서버 및 스케줄러의 메타 데이터를 저장하는 역할을 하기 위해 Airflow에 제공해야 하는 <strong>별도의 서비스</strong>이다.
      </li>
      <li>
        스케줄러는 <strong>DAG 정의가 있는 폴더</strong>에 액세스 할 수 있어야 한다.
      </li>
    </ul>
  <li>
    스케줄러는 다음과 같은 두 가지 역할을 한다.
  </li>
    <ul>
      <li>
        DAG 파일 구문 분석(DAG 파일 읽기, 비트 및 조각 추출, 메타 스토어에 저장 등).
      </li>
      <li>
        실행할 태스크를 결정하고 대기열에 배치.
      </li>
    </ul>
  <li>
    Airflow는 <strong>익스큐터 유형</strong>에 따라 다양한 설치 환경을 구성할 수 있다.
  </li>
    <ul>
      <li>
        익스큐터 유형은 <strong>AIRFLOW_CORE_EXECUTOR</strong>로 설정한다.
      </li>
      <li>
        p302에서는 장표로 각 익스큐터의 특징을 살펴볼 수 있으면 익스큐터는 <strong>환경</strong>에 맞게 설정해야 한다.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 어떤 익스큐터가 적합한가?</h2>
<ul>
  <li>
    <strong>SequentialExecutor</strong>
  </li>
    <ul>
      <li>
        별도의 설정이나 환경 구성 없이 바로 실행시킬 수 있는 방법이다.
      </li>
      <li>
        태스크를 <strong>순차적</strong>으로 수행하며 테스트 및 데모 목적으로 사용할때 선호한다.
      </li>
      <li>
        단, 속도가 조금 느리며 <strong>단일 호스트</strong> 환경에서만 작동한다.
      </li>
    </ul>
  <li>
    <strong>LocalExecutor</strong>
  </li>
    <ul>
      <li>
        여러 태스크를 <strong>병렬</strong>로 실행할 수 있다.
      </li>
      <li>
        익스큐터 내부적으로 워커 프로세스가 <strong>FIFO 적용 방식</strong>을 통해 대기열에 실행할 태스크를 등록한다. (최대 32 개의 병렬 프로세스를 실행할 수 있다).
      </li>
    </ul>
  <li>
    <strong>CeleryExecutor</strong>
  </li>
    <ul>
      <li>
        워커로드를 <strong>여러 머신에 분산</strong>하려는 경우 사용할 수 있다.
      </li>
      <li>
        내부적으로 <strong>Celery</strong>를 이용하여 실행할 태스크들에 대해 대기열을 등록한다.
      </li>
      <li>
        LocalExecutor와 유사하지만 모든 구성 요소가 <strong>서로 다른 호스트</strong>에서 실행된다는 차이가 있다.
      </li>
      <li>
        책을 집필하는 시점에서는 대기열 메커니즘을 위해 RabbitMQ, Redis 또는 AWS SQS를 지원하며 모니터링을 위해 Flower라는 모니터링 도구를 함께 제공한다.
      </li>
      <li>
        Celery는 파이썬 라이브러리 형태로 제공되기에 Airflow 환경에 적용하기 편리하다.
      </li>
    </ul>
  <li>
    <strong>KubernetesExecutor</strong>
  </li>
    <ul>
      <li>
        워커로드를 <strong>여러 머신에 분산</strong>하려는 경우 사용할 수 있다.
      </li>
      <li>
        <strong>쿠버네티스</strong>에서 워크로드를 실행할 때 사용한다.
      </li>
      <li>
        쿠버네티스 설정 및 구성이 필요하며 익스큐터는 Airflow 태스크를 배포하기 위해 <strong>쿠버네티스 API</strong>와 통합된다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. Airflow를 위한 메타스토어 설정</h2>
<ul>
  <li>
    Airflow에서 일어나는 모든 일은 <strong>DB에 등록</strong>되며 DB를 <strong>메타스토어(metastore)</strong>라 한다.
  </li>
  <li>
    <strong>워크플로 스크립트</strong>는 스케줄러를 통해 작업 내역을 분석 및 관리하는 역할을 수행하고 메타스토어에 내용을 저장하는 등 <strong>여러 컴포넌트</strong>로 구성되어 있다.
  </li>
  <li>
    Airflow는 Python ORM(Object Relational Mapper) 프레임워크인 <strong>SQLAlchemy</strong>를 사용하여 모든 DB 태스크를 수행한다.
  </li>
    <ul>
      <li>
        SQL 쿼리를 수동으로 작성하는 대신, <strong>직접 DB</strong>에 작성할 수 있다.
      </li>
      <li>
        SQLAlchemy를 사용하면 SQLAlchemy를 지원하는 DB만 사용할 수 있다. Airflow에서는 <strong>PostgreSQL</strong> 또는 <strong>MySQL</strong> 사용을 권장한다.
      </li>
    </ul>
  <li>
    별도 환경 구성없이 airflow db init을 실행하면 $AIRFLOW_HOME/airflow.db에 SQLite 데이터베이스가 생성된다.
  </li>
    <ul>
      <li>
        따라서 <strong>별도의 DB(postgres 혹은 MySQL 등)</strong>를 사용하는 경우 먼저 <strong>DB를 별도로 생성</strong>한 뒤 <strong>AIRFLOW__CORE__SQL__ALCHEMY_CONN</strong>을 설정하여 Airflow가 DB를 인지하는 절차를 수행해야 한다.
      </li>
        <ul>
          <li>
            <strong>MySQL</strong>: mysql://username:password@localhost:3306/airflow 
          </li>
          <li>
            <strong>PostgreSQL</strong>: postgres://username:password@localhost:5432/airflow
          </li>
        </ul>
    </ul>
  <li>
    Airflow CLI는 DB 구성을 위한 세 가지 명령을 제공한다.
  </li>
    <ul>
      <li>
        <strong>airflow db init</strong>
      </li>
        <ul>
          <li>
            빈 DB에 <strong>Airflow DB 스키마를 생성</strong>한다.
          </li>
        </ul>
      <li>
        <strong>airflow db reset</strong>
      </li>
        <ul>
          <li>
            기존 DB를 지우고 <strong>비어있는 새 DB를 생성</strong>한다. DB의 <strong>모든 정보가 삭제</strong>된다.
          </li>
        </ul>
    </ul>
  <li>
    <strong>airflow db upgrade</strong>
  </li>
    <ul>
      <li>
        <strong>변경된 DB 스키마 정보</strong>를 DB에 적용한다.
      </li>
      <li>
        이미 업그레이드 되었다면 아무 작업도 수행하지 않기에 <strong>여러 번 실행해도 안전</strong>하다.
      </li>
      <li>
        DB가 아직 초기화되지 않은 경우 <strong>db init</strong>과 효과가 동일하지만 <strong>기본 연결</strong>을 생성하지는 않는다.
      </li>
    </ul>
  <li>
    기본 예제 DAG가 표시되는 것을 원하지 않는 경우 <strong>AIRFLOW__CORE__LOAD_EXAMPLES=False</strong>를 설정하여 DAG를 표시하지 않게 할 수 있다.
  </li>
  <li>
    스케줄러와 웹 서버를 다시 시작하면 다시 예제 DAG가 보이는 경우가 있는데 이때에는 AIRFLOW__CORE__LOAD_DEFAULT_CONNECTION=False로 설정하면 된다.
  </li>
  <li>
    최종 단계는 다음과 같이 정리할 수 있다.
  </li>
    <ul>
      <li>
        Airflow 설치
        <br>→ AIRFLOW__CORE__LOAD_EXAMPLE=False 설정
        <br>→ AIRFLOW__CORE__LOAD_DEFAULT_CONNECTION=False 설정
        <br>→ airflow db init 실행
      </li>
    </ul>
</ul>

<br>

<h2>1-3. 스케줄러 자세히 살펴보기</h2>
<ul>
  <li>
    스케줄러의 대표적인 역할은 다음 세 가지와 같다.
  </li>
    <ul>
      <li>
        DAG 파일을 구문 분석하고 추출된 정보를 <strong>DB에 저장</strong>한다.
      </li>
      <li>
        실행할 준비가 된 태스크를 결정하고 이를 <strong>대기 상태</strong>로 전환환다.
      </li>
      <li>
        대기 상태에서 태스크를 가져오고 <strong>실행</strong>한다.
      </li>
    </ul>
  <li>
    Airflow는 <strong>Job</strong> 내에서 <strong>DAG의 모든 태스크</strong>를 실행한다. 모든 Job은 <strong>Airflow UI</strong>에서 확인할 수 있다.
  </li>
</ul>

<br>

<h2>1-4. SchedulerJob의 세 가지 핵심 역할</h2>
<h3>1-4-1. DAG 프로세서</h3>
<ul>
  <li>
    <strong>Airflow 스케줄러</strong>는 DAG 디렉터리의 파이썬 파일을 <strong>주기적으로 업데이트</strong>한다.
  </li>
    <ul>
      <li>
        DAG 코드는 그대로 유지하면서 <strong>외부 소스</strong>에서 작업 구조가 변경되는 경우 Airflow DAG에서 <strong>동적으로 DAG가 생성되기 때문</strong>이다.
      </li>
    </ul>
  <li>
    DAG를 처리하기 위해서는 처리 능력, 즉 <strong>CPU</strong>가 필요하며 네 가지 구성을 고려하여 설정한다. (p308).
  </li>
  <li>
    모든 DAG의 처리는 <strong>while True</strong> 루프 내에서 발생하며 Airflow는 DAG파일을 계속 처리하기 위해 <strong>일련의 단계를 반복</strong>한다.
  </li>
</ul>

<h3>1-4-2. 태스크 스케줄러</h3>
<ul>
  <li>
    스케줄러는 <strong>실행할 태스크 인스턴스</strong>를 결정하는 역할을 한다.
  </li>
  <li>
    모든 태스크 인스턴스에 대해 실행중인 경우 정상적으로 <strong>끝까지 실행되었는지를 판단</strong>하고, 모든 조건을 충족 했을 때 <strong>다음 일정에 대한 예약을 수행</strong>한다.
  </li>
  <li>
    태스크가 예약된 상태에서 <strong>대기 상태로 전환</strong>되는 조건을 결정한다.
  </li>
    <ul>
      <li>
        예약에서 대기로 조건이 바뀌기 위해서는 해당 태스크에 쓸 수 있는 <strong>슬롯에 여유</strong>가 있어야 한다.
      </li>
    </ul>
  <li>
    태스크가 <strong>대기열(queue)</strong>에 들어가면 상태가 <strong>‘대기중’</strong>으로 바뀌고, <strong>익스큐터</strong>가 워커를 통해 해당 태스크를 실행한다.
  </li>
</ul>

<br>

<h2>1-4-3. 태스크 익스큐터</h2>
<ul>
  <li>
    스케줄러가 태스크를 대기열에 배치하면 익스큐터는 <strong>태스크 인스턴스</strong>를 가져와 <strong>실행</strong>한다.
  </li>
    <ul>
      <li>
        Airflow는 메타스토어에 각 상태 변경 상황을 항상 등록한다.
      </li>
      <li>
        Queue에 배치된 메시지에는 태스크 인스턴스의 여러 세부 사항이 포함된다.
      </li>
      <li>
        <strong>태스크를 실행</strong>한다는 것은 <strong>태스크가 실패</strong>하더라도 Airflow가 중단되지 않도록 태스크를 실행할 <strong>새 프로세스</strong>를 만드는 것을 의미한다.
      </li>
      <li>
        새 프로세스에서는 CLI 명령 <strong>airflow tasks run</strong>을 실행하여 <strong>단일 태스크 인스턴스</strong>를 실행하도록 한다.
      </li>
    </ul>
  <li>
    명령을 실행하기 직전에 Airflow는 태스크 인스턴스의 상태를 메타스토어에 <strong>running</strong>으로 등록한다.
  </li>
  <li>
    running으로 등록한 후에는 태스크를 실행하고 메타스토어로 <strong>하트비트(heartbeat)</strong>를 전송하여 주기적으로 확인한다.
  </li>
    <ul>
      <li>
        태스크가 완료 되었는지
      </li>
      <li>
        태스크가 종료되었고 <strong>종료 코드가 0</strong>인 경우는 <strong>작업 성공</strong>을, <strong>종료 코드가 0이 아닌 경우</strong>는 <strong>작업 실패</strong>를 의미한다.
      </li>
      <li>
        태스크가 종료되지 않았다면 하트비트를 등록하고 <strong>AIRFLOW__SCHEDULER__JOB_HEARTBEAT_SEC</strong>만큼 <strong>대기하는 것을 반복</strong>한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 익스큐터 설치</h1>
<ul>
  <li>
    익스큐터는 Airflow 스케줄러의 일부이다.
  </li>
  <li>
    AIRFLOW__CORE__EXECUTOR를 사용하여 설정할 수 있으며 네 가지가 존재한다.
  </li>
    <ul>
      <li>
        SequentialExecutor(기본)
      </li>
      <li>
        LocalExecutor
      </li>
      <li>
        CeleryExecutor
      </li>
      <li>
        KubernetesExecutor
      </li>
    </ul>
</ul>

<br>

<h2>2-1. SequentialExecutor 설정</h2>
<ul>
  <li>
    <strong>단일 하위 프로세스</strong>에서 실행된다.
  </li>
  <li>
    작업은 <strong>순차적으로 하나씩</strong> 실행되며 익스큐터 종류 중 <strong>가장 느리다</strong>. 그러나 구성 절차가 필요하지 않아 <strong>가장 간단하다</strong>.
  </li>
  <li>
    <strong>SQLite DB</strong>와 함께 작동한다.
  </li>
    <ul>
      <li>
        별도 설정 내용 없이 <strong>airflow db init</strong>을 실행하면 $AIRFLOW_HOME 디렉터리에서 <strong>airflow.db</strong>라는 단일 파일인 SQLite DB가 초기화 된다.
      </li>
      <li>
        <strong>airflow scheduler</strong>와 <strong>airflow webserver</strong> 두 가지 프로세스를 시작하면 Airflow가 동작한다.
      </li>
    </ul>
</ul>

<br>

<h2>2-2. LocalExecutor</h2>
<ul>
  <li>
    SequentialExecutor와 유사하지만 여러 하위 프로세스가 있어 <strong>병렬</strong>로 태스크를 실행할 수 있으며 이로인해 비교적 더 빠르다.
  </li>
  <li>
    SequentialExecutor을 제외한 모든 익스큐터는 <strong>MySQL</strong> 및 <strong>PostgreSQL</strong>과 같은 보다 정교한 DB와 함께 작동하여 성능 향상을 도모할 수 있다.
  </li>
  <li>
    <strong>AIRFLOW__CORE__EXECUTOR</strong>를 <strong>LocalExecutor</strong>로 설정하고 <strong>AIRFLOW__CORE__PARALLELISM</strong>에 의해 구성된 <strong>최대 하위 프로세스 수</strong>까지 생성할 수 있다.
  </li>
    <ul>
      <li>
        최대 하위 프로세스 수를 설정하는 것 외에도 병렬 태스크 수를 제한하는 다른 방법으로는 <strong>AIRFLOW__CORE__DAG_CONCURRENCY</strong> 또는 <strong>AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG</strong>의 값을 감소하는 방법을 활용할 수 있다.
      </li>
    </ul>
  <li>
    DB 측면에서는 추가 종속성과 함께 Airflow를 설치하는 태스크가 필요하다.
  </li>
    <ul>
      <li>
        <strong>MySQL</strong>: pip install apache-airflow[mysql]
      </li>
      <li>
        <strong>PostgreSQL</strong>: pip install apache-airflow[postgres]
      </li>
    </ul>
  <li>
    설정이 쉽고 적절한 성능을 얻을 수 있다는 장점이 있다.
  </li>
  <li>
    환경은 스케줄러 시스템의 리소스에 의해 제한되며 더이상 프로세스를 늘릴 수 없는 상황이 발생하면 CeleryExecutor 혹은 KubernetesExecutor를 통한 환경 구성을 고려할 수 있다.
  </li>
</ul>

<br>

<h2>2-3. CeleryExecutor</h2>
<ul>
  <li>
    Celery 프로젝트를 기반으로 구축되었다.  
  </li>
  <li>
    스케줄러와 Celery는 모두 <strong>DAG</strong>와 <strong>DB</strong>에 접근할 수 있어야 한다.
  </li>
  <li>
    <strong>CeleryExecutor</strong>를 구성할 때 고려해야할 부분은 다음과 같다.
  </li>
    <ul>
      <li>
        <strong>공유 파일 시스템</strong>을 통해 <strong>모든 컴퓨터</strong>에서 DAG를 사용할 수 있도록 하거나 DAG가 Airflow와 함께 <strong>docker image에 빌드</strong>되는 컨테이너화된 설정을 통해 구축한다.
      </li>
    </ul>
  <li>
    Celery를 시작하려면 먼저 <strong>Celery 추가 종속성</strong>과 함께 <strong>Airflow를 설치</strong>하고 <strong>익스큐터를 구성</strong>한다.
  </li>
    <ul>
      <li>
        pip install apache-airflow[celery]
      </li>
      <li>
        AIRFLOW__CORE__EXECUTOR=CeleryExecutor
      </li>
    </ul>
  <li>
    Celery에서 대기열은 <strong>브로커(broker)</strong>라 하며 Redis, RabbitMQ 혹은 AWS SQS 등 <strong>Celery가 지원하는 모든 것</strong>이 될 수 있다.
  </li>
  <li>
    브로커를 설치한 후에는 AIRFLOW__CELERY__BROKER_URL을 설정하여 브로커에 대한 Airflow를 구성해야 한다.
  </li>
    <ul>
      <li>
        <strong>Redis</strong>: AIRFLOW__CELERY__BROKER_URL=redis://localhost:6379/0
      </li>
      <li>
        <strong>RabbitMQ</strong>: AIRFLOW__CELERY__BROKER_URL=amqp://user:pass@localhost:5672/
      </li>
    </ul>
  <li>
    Airflow 메타스토어와 통신하려면 AIRFLOW__CELERY__RESULT_BACKEND도 같이 구성해야 한다.
  </li>
    <ul>
      <li>
        <strong>MySQL</strong>: AIRFLOW__CELERY_RESULT_BACKEND=db+mysql://user:pass@localhost/airflow
      </li>
      <li>
        <strong>PostgreSQL</strong>: AIRFLOW__CELERY__RESULT_BACKEND=db+postgresql://user:pass@localhost.airflow
      </li>
    </ul>
  <li>
    <strong>AIRFLOW__CORE__DAGS_FOLDER</strong>에서 구성한 것과 동일한 경로에 있는 워커 호스트에서도 <strong>DAG 폴더에 접근</strong>할 수 있는지 확인한다. 이후 다음과 같은 순서로 실행한다.
  </li>
    <ul>
      <li>
        Airflow webserver 실행
        <br>→ Airflow scheduler 실행
        <br>→ Airflow Celery worker 실행
      </li>
    </ul>
  <li>
    시스템 상태를 모니터링하기 위해 익스큐터, 태스크 및 전체 Celery 시스템을 상태 검사할 수 있는 Celery용 웹 기반 모니터링 도구 <strong>Flower</strong>를 설정할 수 있다.
  </li>
    <ul>
      <li>
        Flower는 기본적으로 <strong>5555 포트</strong>를 사용한다.
      </li>
      <li>
        웹의 첫 화면에는 등록된 Celery 워커 수, 상태 및 각 워커가 처리한 태스크 수에 대한 몇 가지 고급 정보를 확인할 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>2-4. KubernetesExecutor 설정</h2>
<ul>
  <li>
    <strong>AIRFLOW__CORE__EXECUTOR=KubernetesExecutor</strong>를 설정해야 한다.
  </li>
  <li>
    <strong>KubernetesExecutor</strong>를 사용하면 모든 태스크가 쿠버네티스 <strong>파드(pod)에서 실행</strong>된다.
  </li>
  <li>
    쿠버네티스에서 웹 서버, 스케줄러 및 DB를 실행할 필요는 없지만 KubernetesExecutor를 사용할 때 쿠버네티스에서 <strong>다른 서비스들이 함께 실행</strong>되는 것이 관리가 수월하다.
  </li>
  <li>
    <strong>Pod</strong>는 쿠버네티스에서 <strong>가장 작은 작업 단위</strong>이며 <strong>하나 이상의 컨테이너를 실행</strong>할 수 있다. Airflow 관점에서는 <strong>하나의 태스크</strong>는 <strong>하나의 파드</strong>에서 실행된다.
  </li>
    <ul>
      <li>
        태스크가 실행될 때 파드가 생성되는 구조이다.
      </li>
    </ul>
  <li>
    다른 익스큐터들은 작업중인 <strong>워커의 정확한 위치</strong>를 알 수 있지만 쿠버네티스의 파드는 <strong>여러 호스트에 분산</strong>될 수도 있어 사용자 관점에서 실행하는 프로세스가 <strong>어떤 호스트</strong>에서 실행되는지 명확하게 알 수는 없다.
  </li>
  <li>
    쿠버네티스에서 소프트웨어를 배포할 때 가장 많이 사용되는 방법은 쿠버네티스용 패키지 관리자인 <strong>Helm</strong>을 사용하는 것이며 Airflow도 가능하다.
  </li>
  <li>
    Airflow 프로세스 간에 DAG 파일을 배포하는 방법을 결정하는 세 가지 방법.
  </li>
    <ul>
      <li>
        <strong>PersistentVolume</strong>을 사용하여 <strong>pod 간에 DAG 공유</strong>
      </li>
      <li>
        <strong>Git-sync init container</strong>를 사용해 리포지토리의 <strong>최신 DAG</strong> 가져오기
      </li>
      <li>
        <strong>Docker 이미지</strong>에 DAG 빌드
      </li>
    </ul>
  <li>
    모든 Airflow 프로세스를 시작하고 DAG 코드가 있는 시스템의 디렉터리를 지정하는 것은 쉽지만 <strong>다른 컴퓨터</strong>에서 Airflow 프로세스를 실행하는 경우가 복잡하다.
  </li>
    <ul>
      <li>
        공유 파일 시스템과 같이 두 컴퓨터에서 DAG 코드에 액세스할 수 있도록 해야한다.
      </li>
      <li>
        NFS는 인터넷을 통해 직접 파일을 주고받을 수 없기 때문에, 인터넷으로 전송할 땐 <strong>FTP 같은 별도의 전송 방식</strong>을 이용해야 한다.
      </li>
      <li>
        <strong>DAG puller DAG</strong>를 사용하여 Airflow 시스템에서 코드를 가져올 수도 있다. (마스터 브랜치의 코드와 Airflow의 코드 배포 사이에 지연이 존재할 수 있다).
      </li>
    </ul>
</ul>

```bash
# 1. Helm 차트를 사용해 쿠버네티스에 Airflow 설치.
# Helm 차트가 포함된 Airflow 소스 코드 다운.
curl -OL https://github.com/apache/airflow/archive/master.zip
unzip master.zip
# 쿠버네티스에서 Airflow 네임 스페이스를 생성.
kubectl create namespace airflow
# 지정된 버전의 종속적인 Helm 차트를 다운.
helm dep update ./airflow-master/chart
# Airflow Helm 차트를 설치.
helm install airflow ./airflow-master/chart --namespace airflow
```

```python
# 1. DAG puller DAG로 최신 코드 가져오기.
import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator

dag=DAG(
    dag_id="dag_puller",
    # 모든 종속성을 무시한 상태에서 태스크를 실행.
    default_args={"depends_on_past": False},
    start_date=datetime.datetime(2020, 1, 1),
    # 5분 마다 최신 코드를 가져온다.
    scheduler_interval=datetime.timedelta(minites=5),
    # 모든 종속성을 무시한 상태에서 태스크를 실행.
    catchup=False
)

fetch_code=BashOperator(
    task_id="fetch_code",
    bash_command=(
        "cd /airflow/dags &&"
        # Git을 설치하고 구성해야 한다.
        "git reset --hard origin/master"
    ),
    dag=dag,
)
```

<h3>2-4-1. PersistentVolume을 사용하여 포드 간에 DAG 공유</h3>
<ul>
  <li>
    <strong>PersistentVolume</strong>은 스토리이제 대한 <strong>쿠버네티스의 추상화</strong>이며 NFS, Azure File Storage 혹은 AWS EBS 같은 기본 스토리지 기술을 몰라도 <strong>공유 볼륨</strong>을 컨테이너에 마운트할 수 있다.
  </li>
  <li>
    단, 공유 볼륨으로 직접 푸시하기 위한 기본 기능은 제공하지 않기에 <strong>ARIFLOW__KUBERNETES__DAGS_VOLUME_CLAIM</strong>을 <strong>Airflow 파드의 볼륨 이름</strong>으로 설정해야 한다.
  </li>
</ul>

<h3>2-4-2. Git-sync init container를 사용하여 리포지토리에서 최신 DAG 코드 가져오기</h3>
<ul>
  <li>
    Airflow 태스크를 실행하기 전에 <strong>사이드카 컨테이너</strong>에서 Git 저장소를 가져오기 위해 몇 가지 구성을 해야한다. (p321 목록 참고).
  </li>
    <ul>
      <li>
        <strong>사이드카 컨테이너</strong>: Pod 안의 <strong>메인 컨테이너 기능을 확장</strong>하고 <strong>개선</strong>시키는 역할을 하는 컨테이너.
      </li>
    </ul>
</ul>

<h3>2-4-3. 도커 이미지에 DAG 빌드</h3>
<ul>
  <li>
    DAG 코드와 Airflow 이미지를 빌드할 때의 장점
  </li>
    <ul>
      <li>
        현재 배포된 <strong>코드 버전</strong>이 명확하다.
      </li>
      <li>
        프로덕션에서와 <strong>동일한 Airflow 환경</strong>을 로컬에서 실행할 수 있다.
      </li>
      <li>
        새로운 <strong>종속성 간의 충돌(conflict)</strong>은 런타임이 아닌 <strong>빌드 타임</strong>에 발견된다.
      </li>
    </ul>
  <li>
    코드 빌드 단계에 조금 더 체계적인 단계를 도입하고자 한다면 다음을 고려할 수 있다.
  </li>
    <ul>
      <li>
        설치 종속성
      </li>
      <li>
        DAG 코드만 추가 
      </li>
    </ul>
</ul>

```Dockerfile
# 1. 종속성을 관리하는 Dockerfile 예

# 공식 Airflow 이미지 기반
FROM apache/airflow:2.0.0-python3.8

# 기본 사용자는 root 사용자가 아닌 Airflow 사용자이기에 설치를 위해서는 root 사용자로 전환
# 해야 한다.
USER root

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# 설치 후에는 다시 Airflow 사용자로 전환한다.
USER airflow

# requirements에 나열된 추가 종속 항목을 설치한다.
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --user -r /opt/airflow/requirements.txt && \
    rm /opt/airflow/requirements.txt
```

```Dockerfile
# 2. DAG 코드를 관리하는 Dockerfile 예
FROM myrepo/airflow-base:1.2.3

COPY dags/ /opt/airflow/dags/

# 종속성과 DAG를 별도 관리하기에 배포 과정이 간단하다.
```

```bash
# 3. Helm으로 배포된 Airflow 이미지 업데이트
helm upgrade airflow ./airflow-master/chart --namespace airflow\
    --set images.airflow.repository=yourcompany/airflow\
    --set images.airflow.tag=1234abc
```

<br><br>

<h1>3. 모든 Airflow 프로세스의 로그 확인</h1>
<ul>
  <li>
    Airflow에는 세 가지 유형의 로그가 있다.
  </li>
    <ul>
      <li>
        <strong>웹 서버 로그</strong>: <strong>웹 서버</strong>로 전송되는 요청에 대한 정보를 보관한다.
      </li>
      <li>
        <strong>스케줄러 로그</strong>: DAG 구문 분석, 예약 작업 등 <strong>모든 스케줄러 활동</strong>에 대한 정보를 보관한다.
      </li>
      <li>
        <strong>태스크 로그</strong>: 각 로그 파일에는 <strong>단일 태스크 인스턴스의 로그</strong>가 보관된다.
      </li>
    </ul>
  <li>
    기본적으로 로그는 로컬 파일 시스템의 <strong>$AIRFLOW_HOME/logs</strong>에 기록된다.
  </li>
</ul>

<br>

<h2>3-1. 웹 서버 로그 저장</h2>
<ul>
  <li>
    웹 서버 내에는 두 가지 유형의 로그가 존재한다.
  </li>
    <ul>
      <li>
        액세스 로그와 오류
      </li>
      <li>
        시스템 정보도 보관하는 오류 로그.
      </li>
    </ul>
</ul>

```bash
# 1. airflow 웹 서버를 시작할 때 플래그를 적용하여 두 유형의 로그를 파일에 기록한다.
airflow webserver --access_logfile [filename]
airflow webserver --error_logfile [filename]
```

<br>

<h2>3-2. 스케줄러 로그 저장</h2>
<ul>
  <li>
    스케줄러는 웹 서버와 다르게 기본적으로 <strong>파일</strong>에 로그를 작성한다.
  </li>
  <li>
    스케줄러가 DAG 파일을 처리할 때마다 각 DAG에서 발생하는 로그를 별도로 기록하며 스케줄러가 작동하는 방법을 이해하는데 중요한 역할을 한다.
  </li>
  <li>
    로그는 <strong>scheduler 디럭터리</strong> 내의 파일에서 확인할 수 있다.
  </li>
  <li>
    scheduler 디럭터리 외에 <strong>dag_processor_manager.log</strong> 이름의 단일 파일을 확인하면 스케줄러가 처리한 파일이 <strong>집계된 내용</strong>을 확인할 수 있다.
  </li>
</ul>

```bash
# 1. 스케줄러 DGA 파일 로그 예.

... Started process (PID=46) to work on /opt/airflow/dags/hello_world.py
# 해당하는 파일의 처리를 시작
... Processing file /opt/airflow/dags/hello_world.py for tasks to queue
... Filling up the DagBag from /opt/airflow/dags/hello_world.py
# DAG hello_world가 파일에서 검색되었음.
☞ ... DAG(s) dict_keys(['hello_world']) retrieved from \
        /opt/airflow/dags/hello_world.py

# DAG가 실행되고 일정에 따라 해당 태스크 인스턴스를 만들 수 있는지, 
# SLA가 누락되었는지 확인.
... Processing hello_world
# 간격의 끝에 도달했기 때문에 DagRun을 생성.
... Created <DagRun hello_world @ 2020-04-11 00:00:00 ...>
# 기존 태스크 인스턴스가 실행 중으로 설정되어야하는지 확인.
... Examining DAG run <DagRun hello_world @ 2020-04-11 00:00:00 ...>
# 누락된 SLA 알림을 보내야하는지 확인.
☞ ... Skipping SLA check for <DAG: hello_world> because \
        no tasks in DAG have SLAs

# 생성할 채스크를 확인하고 예약된 상태로 설정.
☞ ... Creating / updating <TaskInstance: hello_world.hello 2020-04-11 ...> \
        in ORM

# 생성할 채스크를 확인하고 예약된 상태로 설정.
☞ ... Creating / updating <TaskInstance: hello_world.world 2020-04-11 ...> \
        in ORM

# 파일 처리 완료.
☞ ... Processing /opt/airflow/dags/hello_world.py took 0.327 seconds        
```

<br>

<h2>3-3. 태스크 로그 저장</h2>
<ul>
  <li>
    각 파일은 <strong>하나의 태스크</strong>에 대한 <strong>한 번의 시도</strong>를 나타낸다.
  </li>
  <li>
    파일의 내용은 <strong>웹 서버 UI</strong>에서 <strong>태스크</strong>를 열 때 표시되는 내용을 반영한다.
  </li>
</ul>

<br>

<h2>3-4. 원격 저장소로 로그 보내기</h2>
<ul>
  <li>
    Airflow는 로그를 원격 시스템에 전송할 수 있는 <strong>원격 로깅</strong>이라는 기능을 제공한다.
  </li>
  <li>
    원격 로깅을 구성하려면 다음 두 가지 설정이 필요하다.
  </li>
    <ul>
      <li>
        AIRFLOW__CORE__REMOTE_LOGGING=True
      </li>
      <li>
        AIRFLOW__CORE__REMOTE_LOG_CONN_ID=<자격 증명을 보유한 연결 ID>
      </li>
    </ul>
</ul>

<br><br>

<h1>4. Airflow 메트릭 시각화 및 모니터링</h1>
<ul>
  <li>
    <strong>메트릭(metric)</strong>이라고 하는 시스템 상태에 대한 숫자 데이터에 중점을 둔다.
  </li>
  <li>
    모니터링 관점에서 시스템에 대한 파악과 이해는 <strong>로그</strong>, <strong>메트릭</strong> 그리고 <strong>추적</strong> 세 가지 항목을 조합하여 구성된다.
  </li>
</ul>

<br>

<h2>4-1. Airflow로부터 메트릭 수집하기</h2>
<ul>
  <li>
    Airflow는 StatsD로 측정된다.
  </li>
  <li>
    Airflow의 관점에서 측정이란 이번트에 대한 정보를 수집, 집계, 시각화 또는 보고하기 위해 어딘가에 전송하는 것을 의미한다.
  </li>
</ul>

<h3>4-1-1. Pushing vs Pulling</h3>
<ul>
  <li>
    <strong>Push 모델</strong>은 애플리케이션이 메트릭 데이터를 메트릭 수집 시스템으로 직접 <strong>전송(push)</strong>하는 방식이다.
  </li>
    <ul>
      <li>
        여러 애플리케이션이 동시에 데이터를 전송할 경우, 수집 시스템이 <strong>과부하(오버플로)</strong>될 수 있다.
      </li>
    </ul>
  <li>
    <strong>Pull 모델</strong>은 메트릭 수집 시스템이 지정된 <strong>엔드포인트에서 주기적으로 데이터를 가져오는(pull)</strong> 방식이다. 애플리케이션은 모니터링 대상 데이터를 엔드포인트를 통해 노출한다.
  </li>
  <li>
    <strong>StatsD</strong>는 <strong>Push 모델</strong>로 동작하며, 메트릭을 전송받을 수 있도록 수집 시스템을 미리 설정해야 한다.
  </li>
</ul>

<h3>4-1-2. 어떤 메트릭 수집 시스템을 써야 하는가?</h3>
<ul>
  <li>
    StatsD 외에 대표적인 시스템에는 Prometheus와 Graphite가 대표적이다.
  </li>
  <li>
    StatsD는 Airflow에 포함된 형태로 구성되지만 <strong>메트릭을 수집하는 서버</strong>는 사용자가 직접 설정해야 한다.
  </li>
    <ul>
      <li>
        많은 메트릭 수집 시스템은 서로의 형식을 읽어 <strong>구성 요소를 교환</strong>할 수 있다.
      </li>
    </ul>
  <li>
    일반적으로 StatsD보다는 <strong>Prometheus</strong>가 메트릭을 수집하고 <strong>Grafana</strong>가 대시보드에서 메트릭을 시각화하는 방법을 더 많이 사용한다.
  </li>
</ul>

<br>

<h2>4-2. 측정 항목을 전송하도록 Airflow 구성</h2>

```bash
# 1. Airflow가 StatsD 항목을 push 하도록 statsd 추가 종속성과 함께 Airflow를 설치한다.
pip install apache-airflow[statsd]

# Airflow가 측정 항목을 push할 위치를 구성한다.
#   - AIRFLOW__METRICS__STATSD_ON=True
#   - AIRFLOW__METRICS__STATSD_HOST=localhost (=default value)
#   - AIRFLOW__METRICS__STATSD_PORT=9125
#   - AIRFLOW__METRICS__STATSD_PREFIX=airflow (=default value)
```

<br>

<h2>4-3. 메트릭을 수집하도록 Prometheus 구성</h2>
<ul>
  <li>
    Prometheus는 시스템 모니터링을 위한 소프트웨어이다.
  </li>
  <li>
    핵심은 <strong>PromQL</strong>이라는 언어로 쿼리할 수 있는 <strong>시계열 DB</strong>의 역할을 수행한다는 것이며 <strong>메트릭을 DB로</strong> 가져오는 방식으로 작동한다.
  </li>
    <ul>
      <li>
        X초 마다 사용자가 구성한 대상에서 최신 메트릭을 가져온다.
      </li>
    </ul>
  <li>
    Prometheus가 너무 많은 일을 수행하게 되면 대상을 scraping할 때 자동으로 <strong>속도를 느리게 조정</strong>한다.
  </li>
  <li>

  </li>
</ul>


```bash
# 1. 도커로 StatsD 내보내기 실행.
#     - 9102: Prometheus HTTP 포트
#     - 9125: StatsD UDP 수집 포트
docker run -d -p 9102:9102 -p 9125:9125/udp prom/statsd-exporter
```

```bash
# 2. StatsD 내보내기를 사용하여 노출된 샘플 Prometheus 메트릭

# HELP airflow_collect_dags Metric autogenerated by statsd_exporter.
# TYPE airflow_collect_dags gauge
airflow_collect_dags 1.019871
# HELP airflow_dag_processing_processes Metric autogenerated by statsd_
#     exporter.
# TYPE airflow_dag_processing_processes counter airflow_dag_processing_
#     processes 35001
# HELP airflow_dag_processing_total_parse_time Metric autogenerated by 
#     statsd_exporter.
# TYPE airflow_dag_processing_total_parse_time gauge airflow_dag_processing_
#     total_parse_time 1.019871 
☞ # HELP airflow_dagbag_import_errors Metric autogenerated by statsd_exporter.
# TYPE airflow_dagbag_import_errors gauge
airflow_dagbag_import_errors 0
# HELP airflow_dagbag_size Metric autogenerated by statsd_exporter.
# TYPE airflow_dagbag_size gauge
airflow_dagbag_size 4
```

```yaml
# 3. 최소 Prometheus 구성.
scrape_configs:
    # Prometheus 메트릭 스크레이핑 태스크를 정의
    - job_name: 'airflow'
      static_configs:
      # 스크레이핑 작업의 URL
      - targets: ['localhost:9102']
```

```bash
# 4. 도커와 함께 Prometheus를 실행하여 메트릭 수집.
docker run -d -p 9090:9090 \
    -v /tmp/prometheus.yaml:/etc/prometheus/ prometheus.yaml \
    prom/prometheus

# http://localhost:9090의 Prometheus에서 airflow 대상이 작동 중인지 확인.
```

<h3>4-3-1. 메트릭 데이터 모델</h3>
<ul>
  <li>
    Prometheus의 데이터 모델은 <strong>이름</strong>과 <strong>key-value 세트</strong>로 고유한 측정 항목을 식별한다.
  </li>
  <li>
    StatsD를 포함한 다른 메트릭 시스템은 계층 기반으로 구성되어 있으며 메트릭을 지칭하는 이름은 <strong>점(dot)</strong>으로 구분되어 저장된다.
  </li>
  <li>
    StatsD 내보내기는 특정 점으로 구분된 메트릭을 <strong>Prometheus 메트릭으로 변환</strong>되게 구성할 수 있다.
  </li>
</ul>

<br>

<h2>4-4. Grafana를 이용한 대시보드 생성</h2>
<ul>
  <li>
    Grafana는 메트릭 시각화를 위한 대표적인 도구이다.
  </li>
  <li>
    <strong>http://localhost:3000</strong>으로 접속한 뒤 Prometheus는 첫 번째 데이터 소스로 추가한다.
  </li>
  <li>
    Prometheus는 주기적으로 정보를 수집하여 전달하기에 완전 실시간 대시보드는 아니다. (몇 분 수준의 <strong>지연</strong>).
  </li>
  <li>
    Prometheus는 모니터링 및 경고에 적합하기에 보고 형태로 시스템을 구현하고 싶다면 개별 이벤트에 대해 InfluxDB와 같은 <strong>시계열 DB</strong>를 고려해 볼 수 있다.
  </li>
</ul>

```bash
# 1. 도커로 Grafana 실행
docker run -d -p 3000:3000 grafana/grafana
```

<br>

<h2>4-5. 무엇을 모니터링해야 하는가?</h2>
<h3>4-5-1. Latancy</h3>
<ul>
  <li>
    서비스 요청에 <strong>얼마나 걸리는지</strong>, 웹 서버가 <strong>응답하는 데 걸리는 시간</strong> 또는 스케줄러가 태크스를 <strong>대기 상태에서 실행 상태로 이동하는 데 걸리는 시간</strong>을 등.
  </li>
  <li>
    일반적으로 특정 항목은 <strong>기간</strong>으로 표현된다.
  </li>
</ul>

<h3>4-5-2. Traffic</h3>
<ul>
  <li>
    시스템에 얼마나 많은 수요가 몰리고 있는지, Airflow 시스템이 처리해야 하는 태스크 수 또는 Airflow가 사용할 수 있는 <strong>풀 슬롯(open pool slot)의 수</strong>를 고려한다.
  </li>
  <li>
    일반적으로 <strong>기간당 평균</strong>으로 표현한다.
  </li>
</ul>

<h3>4-5-3. Errors</h3>
<ul>
  <li>
    어떤 오류가 발생했는지를 의미한다.
  </li>
</ul>

<h3>4-5-4. Saturation</h3>
<ul>
  <li>
    시스템 <strong>자원의 어느 부분</strong>을 활용하고 있는지를 의미한다. 시스템이 얼마나 충분하지 확인하기 위해서는 <strong>시스템의 상한선</strong>을 알아여 한다.
  </li>
  <li>
    Prometheus의 주요 내보내기 항목들
  </li>
    <ul>
      <li>
        Airlfow가 실행 중인 머신(CPU, 메모리, 디스크 I/O, 네트워크 트레픽 등)을 위한 노드.
      </li>
      <li>
        DB 모니터링을 위한 PostgreSQL / MySQL 서버.
      </li>
      <li>
        CeleryExecutor를 사용할 때 Celery 모니터링을 위한 Celery export 중 하나.
      </li>
      <li>
        Blackbox 내보내기. 엔드 포인트를 풀링하고 미리 정의된 HTTP 코드가 반환되는지 확인.
      </li>
      <li>
        쿠버네티스 환경의 경우 쿠버네티스 문서를 참조.
      </li>
    </ul>
  <li>
    사용 가능한 모든 측정 항목의 개요는 Airflow 문서에 나열되어 있다.
  </li>
    <ul>
      <li>
        <strong>DAG</strong>
      </li>
        <ul>
          <li>
            <strong>dag_processing.import_errors</strong>: DAG를 처리하는 동안 발생한 <strong>오류의 수</strong>.
          </li>
          <li>
            <strong>dag_processing.total_parse_time</strong>: <strong>DAG 추가 / 변경 후</strong> 변동이 큰 것은 좋지 않다.
          </li>
          <li>
            <strong>ti_failure</strong>: <strong>실패한 태스크</strong> 인스턴스의 수.
          </li>
        </ul>
      <li>
        <strong>Airflow의 성능상태</strong>를 이해하기 위한 항목
      </li>
        <ul>
          <li>
            <strong>dag_processing.last_duration.[filename]</strong>: DAG 파일을 처리하는 데 걸린 시간. (값이 높으면 문제이다).
          </li>
          <li>
            <strong>dag_processing.last_run.seconds_ago.[filename]</strong>: 스케줄러가 DAG를 포함하는 파일을 마지막으로 확인할 이후의 시간. 값이 크다는 것은 스케줄러가 바쁘다는 것을 의미한다.
          </li>
          <li>
            <strong>dagrun.schedule_delay.[dag_id]</strong>: 예약된 실행 날짜와 DAG 실행의 실제 실행 날짜 사이의 지연.
          </li>
          <li>
            <strong>executor.open_slots</strong>: 사용가능한 익스큐터 슬롯의 수
          </li>
          <li>
            <strong>executor.queued_tasks</strong>: 대기 상태의 태스크 수
          </li>
          <li>
            <strong>executor.running_tasks</strong>: 실행 상태의 태스크 수
          </li>
        </ul>
    </ul>
</ul>

<br><br>

<h1>5. 실패한 태스크에 대한 알림을 받는 방법</h1>
<h2>5-1. DAG 및 오퍼레이터에서 경고</h2>
<ul>
  <li>

  </li>
</ul>

```python
# 1. DAG 실패시 실행할 실패 콜백 함수 정의.
def send_error():
    # DAG 또는 태스크가 실패할 때 실행되는 사용자 정의 함수
    # 실제 운영에서는 Slack 알림, 이메일 전송, 로깅 등을 여기에 구현할 수 있음
    print("ERROR!")

dag=DAG(
    dag_id="chapter12_task_failure_callback",
    # default_args 내에 on_failure_callback을 지정하면
    # DAG 내 모든 태스크에 동일한 실패 콜백이 적용됨
    default_args={"on_failure_callback": send_error},
    # DAG 자체가 실패했을 때 실행할 콜백도 별도로 지정 가능
    on_failure_callback=send_error,
    """ 중략 """
)

failing_task=BashOperator(
    task_id="failing_task",
    # 항상 실패(exit code 1 반환)
    bash_command="exit 1",
    dag=dag,
)
```

```plaintext
# 3. 자동화된 이메일을 보내기 위한 샘플 SMTP 구성.
AIRFLOW__SMTP__SMTP_HOST=smtp.gmail.com 
AIRFLOW__SMTP__SMTP_MAIL_FROM=myname@gamil.com
AIRFLOW__SMTP__SMTP_PASSWORD=abcdefghijklmnop
AIRFLOW__SMTP__SMTP_PORT=587
AIRFLOW__SMTP__SMTP_SSL=False
AIRFLOW__SMTP__SMTP_STARTTLS=True
AIRFLOW__SMTP__SMTP_USER=myname@gmail.com
```

```python
#  경고를 보낼 이메일 주소 구성.
dag=DAG(
    dag_id="task_failure_email",
    # default_args에 이메일 주소를 지정하면,
    # 태스크가 실패할 때 Airflow가 자동으로 이메일 알림을 전송함
    default_args={"email": "bob@work.com"},
    """ 중략 """
)
```

<br>

<h2>5-2. 서비스 수준 계약 정의</h2>
<ul>
  <li>
    Airflow의 <strong>서비스 수준 계약(SLA, Service Level Agreement)</strong>의 일반적인 정의는 서비스 또는 제품에 대해 충족하는 <strong>특정 표준</strong>이다.
  </li>
    <ul>
      <li>
        특정 표준, 예를 들어 1시간이 기준일 때 <strong>태스크가 1시간 이내에 완료되지 않으면</strong> Airflow는 <strong>SLA Miss 이벤트</strong>를 발생시켜 알림을 전송한다.
      </li>
    </ul>
  <li>
    Airflow의 기본 SLA 이메일 알림은 누락된 SLA 정보만 전달하므로, <strong>이메일 이외의 방식</strong>으로 알림을 보내고 싶다면 <strong>sla_miss_callback</strong> 인수를 사용해 사용자 정의 함수를 통해 처리할 수 있다.
  </li>
    <ul>
      <li>
        sla_miss_callback은 <strong>DAG 클래스</strong>에 대한 인수이다.
      </li>
    </ul>
  <li>
    <strong>태스크 최대 런타임</strong>을 찾는 경우 연산자에 <strong>execution_timeout</strong> 인수를 구성을 고려해 볼 수 있다.
  </li>
    <ul>
      <li>
        execution_timeout을 초과하면 태스크 자체가 실패한다.
      </li>
    </ul>
</ul>

```python
# 1. SLA 구성.
dag=DAG(
    dag_id="chapter12_task_sla",
    # 태스크 실패 또는 SLA 미달 시 이메일 알림을 받을 주소
    default_args={"email": "bob@work.com"},
    # DAG는 30분 마다 트리거
    schedule_interval=datetime.timedelta(minutes=30),
    # DAG 실행 시작 시각
    start_date=datetime.datetime(2020, 1, 1, 12),
    # DAG 실행 종료 시각 (이 이후로는 더 이상 스케줄되지 않음)
    end_date=datetime.datetime(2020, 1, 1, 15),
)

# BashOperator 태스크 정의
sleeptask=BashOperator(
    task_id="sleeptask",
    # 해당 태스크는 60초 동안 대기.
    bash_command="sleep 60",
    # SLA 설정:
    #   - DAG의 예약된 시작 시각과 태스크 완료 시각 사이의 최대 허용 시간(2분)
    #   - 즉, 태스크가 시작 후 2분 이내에 완료되지 않으면 SLA Miss 발생
    sla=datetime.timedelta(minutes=2),
    # 이 태스크가 속한 DAG 객체
    dag=dag
)
```

<br><br>

<h1>6. 확장성 및 성능</h1>
<ul>
  <li>
    <strong>성능</strong>이란 <strong>지연 없이</strong> 가능한 한 기다리지 않고 <strong>이벤트에 신속하게 대응</strong>할 수 있는 능력을 의미한다.
  </li>
  <li>
    <strong>확장성</strong>이란 <strong>서비스에 영향을 주지 않고</strong> 대규모 부하를 처리할 수 있는 능력을 의미한다.
  </li>
</ul>

<br>

<h2>6-1. 실행중인 태스크의 최대 수 제어</h2>
<ul>
  <li>
    실행 중인 태스크 수와 관련된 Airflow 구성.
  </li>
    <ul>
      <li>
        <strong>AIRFLOW__CORE__DAG_CONCURRENCY</strong>: DAG당 <strong>대기 중 또는 실행 중</strong> 상태에 있는 <strong>최대 태스크 수</strong>.
      </li>
      <li>
        <strong>AIRFLOW__CORE__MAX_ACTIVE_RUNS_PER_DAG</strong>: DAG당 <strong>최대 병렬 DAG</strong> 실행 수.
      </li>
      <li>
        <strong>AIRFLOW__CORE__PARALLEISM</strong>: <strong>전역적</strong>으로 <strong>병렬</strong>로 실행할 <strong>최대 태스크 인스턴스 수</strong>
      </li>
      <li>
        <strong>AIRFLOW___CELERY__WORKER_CONCURRENCY</strong>: (Celery만 해당). Celery 워커당 최대 태스크의 수.
      </li>
    </ul>
  <li>
    병렬 처리에 관해서는 <strong>전역 설정(AIRFLOW__CORE__PARALLELISM)</strong>이 우선된다.
  </li>
  <li>
    dag_concurrency 및 parallelism이 default_pool 제한에 도달하기 전에 설정 값을 변경해야 한다.
  </li>
    <ul>
      <li>
        병목 현상이 생긴다면 default_pool(128) 이전에 dag_concurrency 혹은 parallelism 설정이 낮은지 먼저 확인해야 한다.
      </li>
    </ul>
  <li>
    특히 <strong>CeleryExecutor</strong>의 경우 AIRFLOW__CELERY_WORKER_CONCURRENCY 설정은 <strong>Celery</strong>가 <strong>처리할 워커당 프로세스 수</strong>를 제어한다.
  </li>
    <ul>
      <li>
        동시 태스크 수행 숫자만큼 워커를 실행하고 실행하기 위한 기준으로 프로세스 당 200MB의 RAM을 고려한다.
      </li>
      <li>
        Celery 워커가 처리할 수 있는 <strong>병렬 태스크 수</strong>를 추정하기 위해 <strong>리소스를 가장 많이 사용하는 태스크</strong>가 <strong>병렬</strong>로 실행되는 최악의 시나리오를 고려해야 한다.
      </li>
      <li>
        특정 DAG의 경우 기본값 max_active_runs_per_dag는 DAG 클래스의 동시 실행 인수로 재정의할 수 있다.
      </li>
    </ul>
  <li>
    개별 태스크 수준에서 <strong>풀의 특정 태스크</strong>를 실행하도록 pool 인수를 설정할 수 있다. pool은 실행할 수 있는 <strong>태스크 수</strong>에 제한이 있다.
  </li>
  <li>
    태스크 수준에서 task_concurrency 인수를 설정하여 태스크 실행에 대한 특정 <strong>태스크의 추가 제한</strong>을 설정할 수 있다.
  </li>
    <ul>
      <li>
        많은 인스턴스를 병렬로 실행할 때 컴퓨터의 <strong>모든 리소스를 사용</strong>하는 경우 유용하다.
      </li>
    </ul>
</ul>

<br>

<h2>6-2. 시스템 성능 구성</h2>
<ul>
  <li>
    새로운 Airflow 버전에는 일반적으로 몇 가지 성능 개선 사항이 포함되어 있으므로 정기적으로 업데이트하는 것이 좋다.
  </li>
  <li>
    <strong>AIRFLOW__SCHEDULER__SCHEDULER_HEARTBEAT_SEC(기본값 5)</strong>의 값을 높이면 Airflow 태스크에서 수행하는 <strong>체크인(check-in) 수를 줄여 쿼리</strong>를 줄일 수 있다.
  </li>
    <ul>
      <li>
        AIRFLOW__SCHEDULER__SCHEDULER_HEALTH_CHECK_THRESHER를 수정하여 HEALTH CHECK에 대한 오류를 완화할 수 있다.
      </li>
    </ul>
  <li>
    AIRFLOW__SCHEDULER__PARSING_PROCESSES 값은 DAG의 상태를 처리하기 위해 <strong>스케줄러의 태스크 예약 부분이 동시에 동작</strong>하는 프로세스 수를 제어할 때 적용된다.
  </li>
    <ul>
      <li>
        각 프로세스는 새 DAG 실행을 생성해야 하는지, 새 태스크 인스턴스를 예약하거나 대기열에 넣어야 하는지 등을 확인한다.
      </li>
      <li>
        값이 클수록 더 많은 DAG를 동시에 확인할 수 있으나 CPU 사용량이 늘어난다.
      </li>
    </ul>
  <li>
    AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL 설정을 통해 스케줄러가 DAG 디렉터리에서 이전에 보지 못한 <strong>새 파일을 검색하는 빈도</strong>를 결정한다.
  </li>
    <ul>
      <li>
        새 DAG 파일을 자주 추가하는 경우 Airflow UI에 표시될 때까지 기다리는 경우가 많은데 이를 해결할 수 있다. 단, CPU 사용량이 발생한다.
      </li>
    </ul>
</ul>

<br>

<h2>6-3. 여러 스케줄러 실행</h2>
<ul>
  <li>
    Airflow의 경우 분산 시스템을 위한 리더를 선출은 <strong>DB 수준</strong>에서 <strong>행 수준 잠금(SELECT ... FOR UPDATE)</strong>으로 구현된다.
  </li>
    <ul>
      <li>
        DB는 특정 <strong>잠금 개념</strong>을 지원한다. 잠금(lock)이란 하나의 자원(데이터나 행, 파일 등)을 여러 프로세스가 <strong>동시에 건드리지 못하도록 막는 장치</strong>를 의미한다.
      </li>
    </ul>
  <li>
    스케줄러를 추가할 때에는 다른 스케줄러 프로세스를 <strong>추가로 시작</strong>하면 된다.
  </li>
    <ul>
      <li>
        각 스케줄러 인스턴스는 <strong>선입(first-come) 원칙</strong>에 따라 사용할 수 있는 <strong>태스크(DB에 행으로 표시)</strong>를 파악하며 추가 구성이 필요하지는 않다.
      </li>
      <li>
        여러 인스턴스를 실행한 후 머신 하나가 죽더라도 <strong>다른 스케줄러 인스턴스가 실행</strong>되기에 Airflow는 중단되지 않는다.
      </li>
      <li>
        죽은 태스크에 관해서는 <strong>복구가 수행</strong>된다.
      </li>
    </ul>
</ul>