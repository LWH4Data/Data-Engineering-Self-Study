<ul>
  <li>
    접근 제어를 위한 RBAC 인터페이스 검사 및 구성
  </li>
  <li>
    LDAP 서비스에 연결하여 중앙 사용자 집합에 대한 엑세스 권한 부여
  </li>
  <li>
    데이터베이스에서 기밀을 암호화하도록 Fernet 키 구성.
  </li>
  <li>
    브라우저와 웹 서버 간의 트래픽 보호
  </li>
  <li>
    중앙 보안괸리 시스템에서 보안사항 가져오기
  </li>
</ul>

<br><br>

<h1>1. Airflow 웹 인터페이스에서 보안</h1>
<ul>
  <li>
    Airflow 2부터는 http://localhost:8080의 웹 UI가 <strong>RBAC 기반</strong>이다. 
  </li>
  <li>
    로그인을 진행한 뒤 Security 탭을 클릭하면 보안 관련 설정을 할 수 있다. Airflow RBAC에는 5가지 역할이 존재하며 p351에 장표로 정리되어 있다.
  </li>
  <li>
    즉, 역할을 할당하여 <strong>접근 권한</strong>으로 보안을 관리한다.
  </li>
</ul>

<br>

<h2>1-1. RBAC 인터페이스에서 사용자 추가</h2>

```bash
# 1. RBAC 인터페이스에 사용자 등록하기.
airflow users create \
    # Admin은 해당 사용자에게 모든 권한을 부여한다.
    --role Admin \
    --username bobsmith \
    # password 플래그는 암호를 확인한다.
    --password topsecret \
    --email bobsmith@company.com \
    --firstname Bob \
    --lastname Smith
```

<br>

<h2>1-2. RBAC 인터페이스 설정</h2>
<ul>
  <li>
    RBAC 인터페이스는 <strong>FAB(Flask-AppBuilder)</strong> 프레임워크를 기반으로 개발 되었다.
  </li>
  <li>
    RBAC 웹 서버를 처음 실행하면 <strong>$AIRFLOW_HOME</strong>에 <strong>web-server_config.py</strong>라는 파일이 있다.
  </li>
    <ul>
      <li>
        FAB는 config.py 파일로 구성이 가능하지만 명확성을 위해 webserver가 붙었다.
      </li>
      <li>
        해당 파일은 RBAC의 보안을 포함한 모든 구성을 갖고 있다.
      </li>
    </ul>
  <li>
    관련 내용은 FAB 문서를 참고.
  </li>
</ul>

<br><br>

<h1>2. 미사용 데이터 암호화</h1>
<ul>
  <li>
    Airflow와 같이 여러 구성 요소로 구성되는 앱은 <strong>접근 경로의 노출</strong>을 줄이는 것이 보안상 좋다.
  </li>
</ul>

<br>

<h2>2-1. Fernet Key 생성</h2>
<ul>
  <li>
    <strong>Fernet Key</strong>를 사용하여 데이터를 암호화 및 복호화 할 수 있다. 
  </li>
    <ul>
      <li>
        Fernet Key는 데이터를 <strong>DB에 저장하기 전</strong>에 <strong>암호화</strong>를 하고, <strong>읽기 전</strong>에 <strong>복호화</strong>를 진행한다.
      </li>
      <li>
        따라서 침입자가 Fernet Key에 액세스하지 못하면 암호를 사용할 수 없기에 보안이 유지된다.
      </li>
      <li>
        암호화 및 복호화에 필요한 키가 하나이기에 <strong>대칭암호화</strong>에 해당한다.
      </li>
    </ul>
  <li>
    Fernet Key를 환경 변수 저장하지 않으려면 <strong>Bash 명령</strong>에서 값을 읽도록 Airflow를 구성할 수 있다.
  </li>
    <ul>
      <li>
        AIRFLOW__CORE__FERNET_KEY_CMD=cat /path/to/secret에서 설정을 하며 key를 갖는 파일을 Airflow 사용자만 읽기 전용으로 만들 수 있다.
      </li>
    </ul>
</ul>

```python
# 1. Fernet Key 생성.
from cryptography.fernet import Fernet

fernet_key=Fernet.generate_key()
print(fernet_key.decode())
# <출력된 Fernet Key>
```

```bash
# 2. AIRFLOW__CORE__FERNET_KEY 구성 항목을 설정.
AIRFLOW__CORE__FERNET_KEY=<Fernet Key>
```

<br><br>

<h1>3. LDAP 서비스로 연결</h1>
<ul>
  <li>
    이미 회사에서 사용되고 있는 <strong>사용자 관리 디렉터리</strong> 서비스인 <strong>Azure AD</strong> 또는 <strong>OpenLDAP</strong>와 같은 LDAP를 Airflow에서 활용할 수 있다.
  </li>
</ul>

<br>

<h2>3-1. LDAP의 이해</h2>
<ul>
  <li>
    디렉터리 서비스는 데이터를 저장하고, <strong>LDAP</strong>는 디렉터리 서비스를 <strong>쿼리</strong>하는 데 사용된다.
  </li>
  <li>
    디렉터리 서비스는 <strong>대량의 읽기 작업</strong>을 위해 설계되었다. (즉, 자주 요청되지만 변경되지는 않는 데이터).
  </li>
  <li>
    디렉터리 서비스에서 <strong>엔티티</strong>는 <strong>디렉터리 정보 트리(directory information tree, DIT)</strong>라는 계층 구조에 저장된다.
  </li>
    <ul>
      <li>
        각 항목은 <strong>Entry</strong>라고 하며 정보는 속성 및 값이라는 <strong>key-value 쌍</strong>으로 저장된다.
      </li>
      <li>
        각 항목은 <strong>고유 이름(distinguished name, DN)</strong>으로 개별적으로 식별된다.
      </li>
        <ul>
          <li>
            <strong>dc (domain component)</strong>: 도메인 구성 요소이며 트리의 시작점이다.
          </li>
          <li>
            <strong>ou (organizational unit)</strong>: <strong>조직 단위</strong>의 약자이다.
          </li>
          <li>
            <strong>cn (common name)</strong>: <strong>일반 이름</strong>의 약자이다.
          </li>
        </ul>
    </ul>
  <li>
    LDAP 표준은 <strong>특정 키</strong>와 함께 특정 <strong>엔티티</strong>를 정의하는 <strong>다양한 ObjectClass를 정의</strong>한다.
  </li>
    <ul>
      <li>
        sn(surname) 등으로 사람의 성을 지정하고 해당 Object Class에서 사람의 이름을 찾도록할 수 있다.
      </li>
    </ul>
  <li>
    LDAP도 SQL 처럼 쿼리문을 제공하며 p357에서 확인할 수 있다.
  </li>
</ul>

```bash
# 1. LDAP 검색 예
ldapsearch -b "dc=apacheairflow,dc=com"
ldapsearch -b "dc=apacheairflow,dc=com" "(uid=bsmith)"
```

<br>

<h2>3-2. LDAP 서비스에서 사용자 가져오기</h2>
<ul>
  <li>
    LDAP 인증은 FAB을 통해 지원되며 <strong>web-server_config.py($AIRFLOW_HOME)</strong>에서 구성해야 한다.
  </li>
    <ul>
      <li>
        올바른 구성을 위해서는 로그인 시 FAB은 LDAP 서비스에 주어진 사용자 이름과 비밀번호를 <strong>검색</strong>한다.
      </li>
    </ul>
</ul>

```python
# 1. webserver_config.py에서 LDAP 동기화.
from flask_appbuilder.security.manager import AUTH_LDAP

AUTH_TYPE=AUTH_LDAP
AUTH_USER_REGISTRATION=True
# 로그인하는 모든 사용자에게 할당된 기본 역할.
AUTH_USER_REGISTRATION_ROLE = "User"

AUTH_LDAP_SERVER="ldap://openldap:389"
AUTH_LDAP_USE_TLS=False
# 사용자 검색을 위한 DIT 섹션
AUTH_LDAP_SEARCH = "dc=apacheairflow,dc=com"
# 연결하고 검색할 LDAP 서비스의 사용자
AUTH_LDAP_BIND_USER = "cn=admin,dc=apacheairflow,dc=com"
AUTH_LDAP_BIND_PASSWORD = "admin"
# 사용자 이름을 검색할 LDAP 서비스의 필드 이름.
AUTH_LDAP_UID_FIELD = "uid"
```

<br><br>

<h1>4. 웹 서버에 대한 트래픽 암호화</h1>
<ul>
  <li>
    <strong>MITM(man-in-the-middle attack)</strong>을 최대한 피하는 방법에 대해 다룬다.
  </li>
    <ul>
      <li>
        MITM 공격은 두 시스템 또는 사람이 <strong>서로 통신</strong>하는 동안 세 번째 사람이 통신을 <strong>가로채서</strong> 메시지를 읽고 전달하는 공격이다.
      </li>
    </ul>
</ul>

<br>

<h2>4-1. HTTPS 이해</h2>
<ul>
  <li>
    HTTPS에서 사용되는 암호화는 <strong>비대칭 암호화</strong>와 <strong>대칭 암호</strong>를 모두 사용하는 <strong>TLS(transport layer security, 전송 계층 보안)</strong>이다.
  </li>
    <li> HTTPS 세션이 시작될 때, 웹 서버는 먼저 공개적으로 공유할 수 있는 <strong>공개 키(public key)</strong>가 포함된 <strong>인증서</strong>를 <strong>사용자(브라우저)에게 반환</strong>한다. <br>→ 브라우저는 임의로 생성한 <strong>세션 키(session key)</strong>를 서버의 <strong>공개 키로 암호화</strong>하여 <strong>웹 서버에 전달</strong>한다. <br>→ 웹 서버는 자신만이 보유한 <strong>개인 키(private key)</strong>로 암호화된 세션 키를 <strong>복호화</strong>하여 세션 키를 획득한다. <br>→ 이후 통신은 브라우저와 웹 서버가 공유한 <strong>세션 키</strong>를 이용한 <strong>대칭키 암호화 방식</strong>으로 안전하게 진행된다. 
  </li>
</ul>

<br>

<h2>4-2. HTTPS용 인증서 구성</h2>
<ul>
  <li>
    Airflow는 기본적으로 HTTP를 제공하는데 <strong>HTTPS</strong>로 환경을 구성하여 보안을 관리할 수 있다.
  </li>
  <li>
    Airflow에서 대표적인 공개 엔드 포인트인 웹 서버를 보호하기 위해서는 두 가지 항목이 필요하다.
  </li>
    <ul>
      <li>
        개인 키(기밀 유지)
      </li>
      <li>
        인증서(공유하기에 안전)
      </li>
    </ul>
  <li>
    비공개 키와 인증서는 모두 <strong>인증 기관에서 제공하는 파일</strong>이거나 <strong>자체 서명된 인증서</strong>이다.
  </li>
  <li>
    <strong>유효성을 검사</strong>할 수 있는 <strong>신뢰할 수 있는 기관</strong>에서 인증서를 발급 받아야 다체 서면된 인증서를 신뢰하는 번거로움을 줄일 수 있다.
  </li>
</ul>

```bash
# 1. 자체 서명된 인증서.
openssl req \
-x509 \
-newkey rsa:4096
-sha256 \
-nodes \
# 1년 동안 유효한 키를 생성한다.
-days 365 \
# 개인 키의 파일 이름.
-keyout privatekey.pem \
# 인증서 파일 이름.
-out certificate.pem \
-extensions san \
# 대부분 브라우저에는 보안상 이유로 SAN 확장이 필요하다.
-config \
  <(echo "[req]";
    echo distinguished_name=req;
    echo "[san]";
    echo subjectAltName=DNS:localhost,IP:127.0.0.1 ) \
-subj "/CN=localhost"
```

<br><br>

<h1>5. 시크릿 관리 시스템에서 자격 증명 가져오기</h1>
<ul>
  <li>
    많은 회사들은 <strong>시크릿 저장 시스템</strong>을 사용하여 <strong>하나의 단일 시스템</strong>에 <strong>한 번만 저장</strong>을 해두고 필요할 때 기밀 내용을 요청할 수 있다.
  </li>
  <li>
    Airflow에는 기존 변수 및 연결 클래스를 계속 사용하면서 외부 시크릿 스토리지 시스템에서 시크릿을 가져오는 <strong>시크릿 백엔드</strong>라는 기능을 제공한다.
  </li>
  <li>
    DAG 코드에는 HashiCorp Vault에 대한 명시적인 참조가 없으며 이 경우 SimpleHttpOperator는 연결에 설정된 URI로 HTTP 요청을 한다.
  </li>
    <ul>
      <li>
        시크릿 백엔드가 구현되기 전에 해당 시크릿 백엔드 URL을 Airflow 연결에 저장한다.
        <br>→ 이후 HashiCorp Vault에 시크릿 값을 저장할 수 있다.
      </li>
    </ul>
  <li>
    작업을 위해서는 다음 몇 가지를 고려해야 한다.
  </li>
    <ul>
      <li>
        시크릿 백엔드는 <strong>AIRFLOW__SECRETS__BACKEND</strong> 및 <strong>AIRFLOW__SECRETS__BACKEND_KWARGS</strong>로 구성되어야 한다.
      </li>
      <li>
        모든 시크릿에는 <strong>공통 접두사</strong>가 있어야 한다.
      </li>
      <li>
        모든 연결은 <strong>"conn_uri"</strong>라는 키에 저장되어야 한다.
      </li>
      <li>
        모든 변수는 <strong>"value"</strong>라는 키에 저장되어야 한다.
      </li>
    </ul>
  <li>
    시크릿 이름은 <strong>경로</strong>로 저장되며 <strong>시크릿 및 연결</strong>은 <strong>조직에 사용되는 폴더</strong>로 볼 수 있고, <strong>secure_api</strong>는 실제 시크릿을 <strong>식별하는 이름</strong>이다.
  </li>
  <li>
    Vault 시크릿 엔진 내에서 <strong>connections/secure_api</strong> 이름의 시크릿을 생성한다.
  </li>
    <ul>
      <li>
        conenctions는 필요하지 않지만 Airflow는 <strong>접두사</strong>를 사용해 검색하기에 추후 시크릿 계층의 <strong>한 부분 내에서만 검색</strong>할 때 편리하다.
      </li>
    </ul>
  <li>
    시크릿 <strong>백엔드에 Airflow 연결을 저장</strong>하려면 Airflow가 요청하는 키인 <strong>conn_uri</strong>라는 키를 설정한다.
  </li>
    <ul>
      <li>
        연결은 <strong>URI 형식</strong>으로 제공되어야 한다.
      </li>
    </ul>
  <li>
    Airflow에서 자격 증명을 가져올 때에는 두 가지 구성 옵션을 설정한다.
  </li>
    <ul>
      <li>
        <strong>AIRFLOW__SECRETS__BACKEND</strong>는 <strong>시크릿을 읽는 클래스</strong>로 설정되어야 한다.
      </li>
      <li>
        선택한 시크릿 백엔드와 관련된 다양한 <strong>세부 정보</strong>를 <strong>AIRFLOW__SECRETS__BACKEND_KWARGS</strong>에서 구성한다.
      </li>
    </ul>
  <li>
    시크릿 백엔드는 <strong>환경 변수</strong> 및 <strong>Airflow 메타스토어</strong>에 저장된 시크릿을 대체하지 않는 대안적인 위치이다.
  </li>
  <li>
    Airflow는 <strong>시크릿 백엔드 → 환경 변수 → Airflow 메타스토어</strong> 순으로 시크릿을 가져온다.
  </li>
  <li>
    Airflow 릴리스에는 보안 수정 사항이 포함돼 있어 이전 버전의 버그를 닫을 수 있기에 <strong>Airflow 릴리스를 최신 상태</strong>로 유지해야 한다.
  </li>
</ul>

```python
# 1. 구성된 시크릿 백엔드에서 연결 세부 정보 가져오기.
import airflow.utils.dates
from airflow.models import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
dag=DAG(
    dag_id="secretsbackend_with_vault",
    start_date=airflow.utils.dates.days_ago(1),
    schedule_interval=None,
)

call_api=SimpleHttpOperator(
    task_id="call_api",
    # Vault의 시크릿 ID를 참조.
    http_conn_id="secure_api",
    method="GET",
    endpoint="",
    log_response=True,
    dag=dag,
)
```