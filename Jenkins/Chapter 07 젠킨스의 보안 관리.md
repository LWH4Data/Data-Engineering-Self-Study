<ul>
  <li>
    jenkins 인증과 권한 부여 기능을 구성하는 데 필요한 다양한 보안 관련 설정을 배운다.
  </li>
</ul>

<br>

<h1>1. 젠킨스 전역 보안 구성</h1>
<ul>
  <li>
    Jenkins의 보안 설정 전반에 대한 내용이므로 필요할 때 p77을 참고하여 설정하면 된다.
  </li>
  <li>
    http://localhost:8081/manage/configureSecurity/
  </li>
  <li>
    초기 접속 시에만 admin 유저를 생성하라고 나온다. 이후에는 가입이 불가하며 추가 사용자는 직접 Manage Users에서 추가해야 한다.
  </li>
  <li>
    Agent의 포트 번호는 Fixed로 사용한다. 이유는 매번 포트가 재설정되면 인바운드 규칙 등 보안 설정이 어렵기 때문이다.
  </li>
    <ul>
      <li>
        분산 빌드를 사용하지 않는 경우에는 Disable(비활성화)를 선택한다.
      </li>
    </ul>
</ul>

<br>

<h1>2. LDAP (Lightweight Directory Access Protocol)</h1>
<ul>
  <li>
    LDAP는 경량 디렉터리 액세스 프로토콜로 네트워크에서 조직, 개인, 리소스 등을 찾을 수 있게 해주는 소프트웨어 프로토콜이다.
  </li>
  <li>
    LDAP는 <strong>디렉터리 형태</strong>로 구성되며 데이터를 디렉터리에서 <strong>검색하고 인증</strong>한다.
  </li>
  <li>
    LDAP를 프로토콜이라 하는 이유는 디렉터리 형태로 구성되고 검색하는 것 자체가 <strong>LDAP의 통신규약</strong>이기 때문이다.
  </li>
  <li>
    LDAP의 일반적인 용도는 <strong>사용자 이름과 비밀번호를 저장</strong>하고 <strong>인증 기능을 제공</strong>하는 것이다. 젠킨스에서도 사요할 수 있다.
  </li>
  <li>
    해당 서버에 직접 계정을 생성하거나 수동 매핑할 필요 없이 LDAP가 자동으로 수행해 준다.
  </li>
</ul>

<br>

<h2>2-1. 젠킨스 LDAP 필요성</h2>
<ul>
  <li>
    다음의 두 유저가 있다.
  </li>
    <ul>
      <li>
        Pranodayd: 빌드 서버 권한 O, Jenkins 서버 X
      </li>
      <li>
        adminuser: 빌드 서버 권한 X, Jenkins 서버 O
      </li>
    </ul>
  <li>
    LDAP를 사용하는 경우 다음과 같다.
  </li>
    <ul>
      <li>
        Pranodayd → LDAP 프로토콜 → Jenkins 접속 → 빌드 서버에서 Jenkins 가동.
      </li>
    </ul>
  <li>
    즉, 서로의 서버에 계정을 등록하지 않고도 LDAP만으로 연결이 가능하다.
  </li>
</ul> 

<br>

<h2>2-2. 젠킨스 LDAP 구성</h2>
<ul>
  <li>
    현재 젠킨스 컨테이너에는 자동으로 LDAP가 설치되어 있다.
  </li>
  <li>
    LDAP 설정에 대한 부분은 이후 LDAP를 사용하는 부서의 규정을 따른다.
  </li>
</ul>