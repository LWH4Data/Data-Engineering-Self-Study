<ul>
  <li>
    Airflow와 같은 워크플로 관리 솔루션을 이용해 <strong>태스크</strong> 및 <strong>태스크 의존적인 그래프</strong>로 데이터 파이프라이닝을 표현하는 방법을 소개한다.
  </li>
  <li>
    Airflow에 대한 <strong>추상화된 개념</strong>과 이것이 워크플로 관리 전체 에코시스템(ecosystem)에 어떻게 적용되는지 확인한다.
  </li>
  <li>
    Airflow의 몇 가지 <strong>장단점</strong>을 확인하고 특정 사례에서 Airflow가 <strong>적합한 솔루션</strong>인지 확인한다.
  </li>
</ul>

<br>

<h1>1. 데이터 파이프라인 소개</h1>
<ul>
  <li>
    일반적인 데이터 파이프라인은 원하는 결과를 얻기 위해 실행되는 <strong>여러 태스크 혹은 동작으로 구성</strong>한다.
  </li>
    <ul>
      <li>
        다른 시스템의 날씨 API → 서비스 목적에 맞게 데이터 정제 혹은 변환 → 변환된 데이터를 대시보드등 서비스로 전송.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 데이터 파이프라인 그래프</h2>
<ul>
  <li>
    Task 간의 <strong>의존성</strong>을 명확히 하는 방법 중 하나는 데이터 파이프라인을 <strong>그래프</strong>로 표현하는 것이다.
  </li> 
    <ul>
      <li>
        그래프에서 <strong>Task는 노드</strong>로 표시된다.
      </li>
      <li>
        Task 간의 <strong>의존성은 화살표</strong>로 표시된다.
      </li>
      <li>
        따라서 이러한 형태의 그래프는 <strong>방향성 그래프(directed graph)</strong>라 한다.
      </li>
    </ul>
  <li>
    정확히는 <strong>방향성 비순환 그래프(Directed Acyclic Graph, DAG)</strong>이다.
  </li>
    <ul>
      <li>
        DAG는 방향성의 끝점(directed edge)를 포함하지만 반복이나 순환을 허용하지 않기에 <strong>순환 실행을 방지</strong>한다.
      </li>
        <ul>
          <li>
            <strong>순환</strong>이 존재할 경우 서로의 완료 상태를 대기하는 <strong>교착 상태(deadlock)</strong>가 발생할 수 있다.
          </li>
        </ul>
    </ul>
</ul>

<br>

<h2>1-2. 파이프라인 그래프 실행</h2>
<ul>
  <li>
    DAG 알고리즘의 진행 단계는 다음과 같다.
  </li>
    <ul>
      <li>
        그래프 안의 태스크는 각각 <strong>개방된(open) 상태이며(=미완료)</strong> 다음과 같은 단계를 수행한다.
      </li>
        <ul>
          <li>
            각각의 화살표 <strong>끝점은 태스크</strong>를 향하며 다음 태스크로 향하기 전에 <strong>이전 태스크가 완료되었는지 확인</strong>한다.
          </li>
          <li>
            태스크가 완료되면 다음에 실행해야 할 태스크를 <strong>대기열에 추가</strong>한다.
          </li>
        </ul>
      <li>
        실행 대기열에 있는 <strong>태스크를 실행</strong>하고 태스트 수행이 완료되면 <strong>완료 표시</strong>를 한다.
      </li>
      <li>
        그래프의 <strong>모든 태스크</strong>가 완료될 때까지 <strong>1단계</strong>로 돌아간다.
      </li>
    </ul>
  <li>
    각 <strong>작업 상태</strong>를 확인하기 위해 내부적으로는 <strong>루프</strong>처럼 <strong>반복적으로 상태를 체크</strong>한다.
  </li>
</ul>

<br>

<h2>1-3. 그래프 파이프라인과 절차적 스크립트 파이프라인 비교</h2>
<ul>
  <li>
    그래프 대신 간단한 스크립트를 이용해서 각 단계를 선형 체인(linear chain) 형태로 실행할 수도 있다. 단, <strong>그래프 방식이 더 유리</strong>하다.
  </li>
  <li>
    그래프 방식을 사용하면 별도의 데이터 소스로 부터 시작하는 여러 task를 <strong>병렬적으로 실행</strong>할 수 있다. 따라서 순차적 시행보다 <strong>시간이 절약</strong>된다.
  </li>
    <ul>
      <li>
        즉, 전체 작업을 하나의 모놀리식(monolithic) 스크립트 또는 프로세스로 구성되는 것이 아니라 <strong>task 단위로 명확하게 분리</strong>할 수 있다.
      </li>
    </ul>
  <li>
    task 단위로 전체 파이프라인을 분리하면 실패 시에 처음부터 시행하는 것이 아니라 <strong>실패한 task부터 수행</strong>이 가능하기에 효율적이다.
  </li>
</ul>

<br>

<h2>1-4. 워크플로 매니저를 이용한 파이프라인 실행.</h2>
<ul>
  <li>
    여러 워크플로 매니저에 대해 장표로 정리하고 설명해준다. 참고만.
  </li>
</ul>

<br><br>

<h1>2. Airflow 소개</h1>
<h2>2-1. 파이썬 코드로 유연한 파이프라인 정의</h2>
<ul>
  <li>
    Airflow는 <strong>파이썬 스크립트</strong>로 DAG의 구조를 설명하고 구성한다.
  </li>
    <ul>
      <li>
        각 DAG 파일은 주어진 DAG에 대한 <strong>태스크 집합</strong>과 <strong>태스크 간의 의존성</strong>을 기술한다.
      </li>
      <li>
        Airflow는 DAG 구조를 식별하기 위해 코드를 <strong>파싱(parsing)</strong>한다.
      </li>
      <li>
        DAG 파일에는 Airflow의 실행 방법과 시간 등을 정의한 몇 가지 추가 <strong>메타데이터</strong>를 포함할 수 있다.
      </li>
    </ul>
  <li>
    파이썬 코드로 정의하는 프로그래밍 방식은 DGA 구성하는데 많은 유연성을 제공한다. 즉, 여러 앱과 호환이 된다.
  </li>
</ul>

<br>

<h2>2-2. 파이프라인 스케줄링 및 실행</h2>
<ul>
  <li>
    DAG로 파이프라인 구조를 정의하면 Airflow가 언제 파이프를 실행할 것인지 각 <strong>DAG의 실행 주기</strong>를 정의할 수 있다.
  </li>
  <li>
    <strong>Airflow의 구성 요소</strong>
  </li>
    <ul>
      <li>
        <strong>Airflow 스케줄러</strong>: DAG를 분석하고 <strong>현재 시점에서 DAG의 스케줄이 지난 경우</strong> Airflow 워커에 <strong>DAG의 태스크를 예약</strong>한다.
      </li>
      <li>
        <strong>Airflow 워커</strong>: 예약된 태스크를 <strong>선택</strong>하고 <strong>실행</strong>한다.
      </li>
      <li>
        <strong>Airflow 웹 서버</strong>: 스케줄러에서 분석한 <strong>DAG를 시각화</strong>하고 <strong>DAG 실행과 결과</strong>를 확인할 수 있는 주요 인터페이스를 제공한다.
      </li>
    </ul>
  <li>
    <strong>Airflow의 스케줄러</strong>는 개념적으로 다음과 같은 단계를 통해 작업을 진행한다.
  </li>
    <ul>
      <li>
        사용자 DAG workflow 작성 → 스케줄러 DAG 파일 분석 → 각 DGA 태스크, 의존성 및 예약 주기 확인.
      </li>
      <li>
        스케줄러가 마지막 DAG까지 내용을 확인 → DAG의 <strong>예약 주기가 경과</strong>했는지 확인 → 예약 주기가 현재 시간 이전이라면 실행되도록 예약.
      </li>
      <li>
        예약된 각 태스크에 대해 스케줄러는 해당 태스크의 <strong>의존성(=업스트림 태스크)</strong>을 확인 → 태스크가 완료되지 않았다면 <strong>실행 대기열에 추가</strong>.
      </li>
      <li>
        스케줄러는 1단계로 다시 돌아가 <strong>새로운 루프를 잠시 동안 대기</strong>.
      </li>
    </ul>
  <li>
    Airflow에서 태스크가 실행 대기열에 추가되면, 워커가 <strong>pool의 제한</strong>에 따라 태스크를 선택하여 실행한다.
  </li>
  <li>
    과정의 모든 결과는 <strong>Airflow의 메타스토어</strong>로 전달되며 사용자는 Airflow의 웹 인터페이스를 통해 태스크 <strong>진행 상황을 추적하고 로그를 확인</strong>할 수 있다.
  </li>
</ul>

<br>

<h2>2-3. 모니터링과 실패 처리</h2>
<ul>
  <li>
    Airflow의 <strong>웹 인터페이스</strong>에 대해서 소개한다. 
  </li>
  <li>
    Airflow는 task 실패 시에 <strong>재시도</strong>할 수 있기에 오류 발생 시 task를 복구할 수 있다.
  </li>
  <li>
    <strong>재시도가 실패</strong>하면 Airflow는 <strong>task 실패를 기록</strong>하고 알림을 설정한 겨우 사용자에게 실패를 <strong>통보<./strong>한다.
  </li>
  <li>
    <strong>트리 뷰나 그래프</strong> 등을 통해 실패한 태스크를 확인하고 로그를 확인할 수 있기에 디버깅을 쉽게 할 수 있으며 트리 뷰에서 개별 <strong>task 결과를 삭제</strong>하고 <strong>종속된 task를 모두 재실행</strong>할 수 있다.
  </li>
</ul>

<br>

<h2>2-4. 점진적 로딩 및 백필</h2>
<ul>
  <li>
    최종 시점과 예상되는 다음 <strong>스케줄 주기</strong>를 상세하게 알려주는 것이 가능하다. 이를 통해 <strong>각각의 주기(매일, 매주 등)</strong>로 나누고 각 <strong>주기별로 DAG를 실행</strong>할 수 있다.
  </li>
  <li>
    주기별로 수행하는 특성은 파이프라인을 <strong>점진적으로 실행</strong> 가능하도록 하기에 매번 전체 데이터 세트를 처리할 필요없이 <strong>해당 시간 슬롯(delta 데이터)</strong>에 대한 데이터만 처리한다.
  </li>
  <li>
    스케줄 주기를 <strong>백필 개념</strong>과 결합하여 새로 생성한 DAG를 <strong>과거 시점 및 기간</strong>에 대해 실행이 가능하다.
  </li>
    <ul>
      <strong>Backfill</strong>: “과거의 누락된 데이터” 또는 “이전 기간에 대해 처리하지 못한 작업”을 다시 실행해서 채우는 작업을 말합니다.
    </ul>
    <li>
      과거 실행 결과를 삭제 후 태스크 코드를 변경하여 삭제된 과거 태스크를 쉽게 재실행할 수 있다.
    </li>
</ul>

<br><br>

<h1>3. 언제 Airflow를 사용해야 할까</h1>
<h2>3-1. Airflow를 선택하는 이유</h2>
<ul>
  <li>
    Airflow가 <strong>배치 지향(batch oriented)</strong> 데이터 파이프라인을 구현하는 데 적합한 이유를 아래에 나열한다.
  </li>
  <li>
    <strong>파이썬 언어</strong>를 사용하기에 파이썬을 활용한 <strong>복잡한 커스텀 파이프라인</strong>을 만들 수 있다.
  </li>
  <li>
    파이썬 기반의 Airflow는 <strong>쉽게 확장 가능</strong>하고 다양한 시스템과 <strong>통합이 가능</strong>하다.
  </li>
  <li>
    수많은 스케줄링 기법을 통해 파이프라인을 정기적으로 실행하고 점진적(증분, incremental) 처리를 통해, 전체 파이프라인을 <strong>재실행할 필요 없는</strong> 효율적인 파이프라인 구축이 가능하다.
  </li>
  <li>
    <strong>백필 기능</strong>을 활용하여 과거 데이터를 <strong>손쉽게 재처리</strong>할 수 있기에 코드를 변경한 후 재생성이 필요한 데이터에 재처리가 가능하다. 필터링 쿼리 없이 직관적으로 가능하다는 의미.
  </li>
  <li>
    <strong>웹 인터페이스</strong>를 통해 파이프라인 실행 결과를 <strong>모니터링</strong>할 수 있고 <strong>디버깅</strong>을 위한 편리한 뷰를 제공한다.
  </li>
  <li>
    오픈 소스이며 몇몇 회사에서는 Airflow 설치 관리 및 실행에 대한 유연성을 제공하는 괸라형(managed) Airflow 솔루션 또한 제공한다.
  </li>
</ul>

<br>

<h2>3-2. Airflow가 적합하지 않은 경우</h2>
<ul>
  <li>
    <strong>스트리밍(실시간데이터 처리)</strong> 워크플로 및 해당 파이프라인 처리에 적합하지 않다.
  </li>
  <li>
    추가 및 삭제가 빈번한 <strong>동적 프라이프라인</strong>의 경우 DAG는 가장 최근 실행 버전에 대한 정의만 표현하기에 동적으로 변화하는 파이프를 표현하기에 적합하지 않다.
  </li>
  <li>
    python 사용 경험이 전무한 경우 구현에 어려움을 겪을 수 있다.
  </li>
  <li>
    python으로 DAG를 작성할 경우 확장되며 어려워 질 수 있기에 처음부터 엄격하게 관리해야 한다.
  </li>
  <li>
    데이터 계보(lineage)와 데이터 버전 관리를 위해서는 특정 도구를 Airflow와 직접 통합해야 한다.
  </li>
</ul>