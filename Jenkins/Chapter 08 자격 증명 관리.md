<ul>
  <li>
    Jenkins에서 인증에 필요한 정보 <strong>자격 증명(credential)</strong>이라 한다.
  </li>
  <li>
    자격 증명의 예를 들면 사용자 이름과 비밀번호, 개인 키와 공개 키를 사용하는 SSH 인증, API 토큰 기반 등의 방식이 있다.
  </li>
  <li>
    이번 장에서는 젠킨스에서 다양한 종류의 자격 증명을 생성하는 방법을 배운다.
  </li>
</ul>

<br>

<h1>1. 젠킨스의 자격 증명 이해</h1>
<ul>
  <li>
    자격 증명은 <strong>젠킨스에 저장된 인증 정보</strong>로 구성되며 이를 통해 젠킨스는 다양한 종류의 <strong>외부 도구에 접속</strong>한다.
  </li>
  <li>
    젠킨스는 <strong>각기 다른 자격 증명 항목을 생성</strong>하여 인증 정보를 안전하게 보관한다.
  </li>
  <li>
    자격 증명 형태로 저장된 정보는 <strong>다른 젠킨스 작업들과도 공유</strong>할 수 있다.
  </li>
  <li>
    자격 증명 항목은 <strong>고유의 자격 증명 ID</strong>를 갖으며 젠킨스 또한 이 ID를 사용한다. (원본 데이터 X).
  </li>
</ul>

<br><br>

<h1>2. 자격 증명 항목 생성</h1>
<ul>
  <li>
    주로 사용되는 인증 기법은 다음이 있다.
  </li>
    <ul>
      <li>
        기본 인증
      </li>
      <li>
        SSH 인증
      </li>
      <li>
        API 토큰
      </li>
      <li>
        인증서(certificate)
      </li>
    </ul>
  <li>
    젠킨스는 <strong>자격 증명을 생성</strong>하고 필요한 <strong>인증 정보를 저장</strong>하는데 <strong>Credentials 플러그인</strong>을 사용한다.
  </li>
  <li>
    젠킨스 작업/파이프라인 작업을 할 때 자격 증명 ID를 통해 <strong>자격 증명을 참조</strong>한다. 이 때에는 <strong>Credentials Binding 플러그인</strong>을 사용한다.
  </li>
</ul>

<br>

<h2>2-1. 범위 및 도메인 이해</h2>
<h3>2-1-1. 범위 (scope)</h3>
<ul>
  <li>
    범위는 특정한 자격 증명 항목을 <strong>사용할 수 있는 위치</strong>를 정의한다.
  </li>
</ul>
<h4>a. 전역(global) 범위</h4>
<ul>
  <li>
    <strong>모든</strong> 젠킨스 작업과 <strong>모든</strong> 젠킨스 서버 시스템에서 사용할 수 있다.
  </li>
</ul>
<h4>b. 시스템 (system)</h4>
<ul>
  <li>
    <strong>해당하는 시스템 기능</strong>을 수행하는 데에만 사용할 수 있다.
  </li>
  <li>
    <strong>젠킨스 작업</strong>에서는 사용할 수 없다.
  </li>
    <ul>
      <li>
        젠킨스 작업: <strong>빌드 수명 주기를 자동화</strong>하기 위해 <strong>일련의 단계</strong>를 정의한 것.
      </li>
    </ul>
</ul>

<br>

<h3>2-1-2. 도메인 (domain)</h3>
<ul>
  <li>
    유사한 시스템에서 사용하는 자격 증명을 <strong>그룹화</strong>한다.
  </li>
  <li>
    간단하게 <strong>도메인을 생성</strong>하고 필요한 <strong>자격 증명 항목들을 추가</strong>하면 된다.
  </li>
</ul>

<br>

<h2>2-2. 젠킨스에서 자격 증명 항목 생성</h2>
<ul>
  <li>
    이후 과정은 모두 간단한 실습을하며 자격 증명을 생성하는 것이기에 필요할 때 참고하면 된다.
  </li>
</ul>