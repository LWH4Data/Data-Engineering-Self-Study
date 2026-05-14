<h1>1. 사전 지식 : CI/CD</h1>
<ul>
  <li>
    1-1. CI/CD란?
  </li>
    <ul>
      <li>
        CI/CD를 도입하면 빌드부터 배포까지의 과정을 자동화할 수 있고 모니터링 또한 할 수 있다.
      </li>
        <ul>
          <li>
            CI는 지속적 통합을, CD는 지속적 제공의 의미가 있다.
          </li>
        </ul>
    </ul>
</ul>

<h3>1-1-1. 지속적 통합, CI</h3>
<ul>
  <li>
    CI는 Continuous Integration으로 개발자를 위한 <strong>빌드와 테스트를 자동화</strong>하는 과정이다.
  </li>
    <ul>
      <li>
        일반적으로 코드 변경 사항이 코드 저장소에 업로드되면 CI를 시작하고 문제가 생기면 코드의 오류를 반환한다.
      </li>
    </ul>
</ul>

<h3>1-1-2. 지속적 제공과 지속적 배포, CD</h3>
<ul>
  <li>
    CD(continuous delivery or continuous deployment)는 CI 작업이 완료된 뒤 수행되며 배포 준비가 된 코드를 <strong>자동으로 서버에 배포</strong>하는 작업을 자동화한다.
  </li>
</ul>

<h4>1-1-2-1. 지속적 제공에서의 CD 의미</h4>
<ul>
  <li>
    애플리케이션에 적용한 코드의 빌드와 테스트를 성공적으로 진행했을 때 <strong>코드 저장소에 자동으로 업로드</strong>한다.
  </li>
</ul>

<h4>1-1-2-2. 지속적 배포에서의 CD 의미</h4>
<ul>
  <li>
    성공적으로 병합한 코드를 배포 환경으로 내보낸다. (실무에서는 릴리스라 한다).
  </li>
</ul>

<br>

<h2>1-2. 깃과 깃허브</h2>
<ul>
  <li>
    깃은 <strong>코드를 저장하고 관리</strong>할 수 있는 시스템이고, 깃허브(github)는 <strong>깃과 연동해 작업한 코드를 저장</strong>할 수 있는 서비스이다.
  </li>
  <li>
    이후 내용은 이미 git과 github을 사용하고 있기에 skip.
  </li>
</ul>

<br><br>

<h1>2. 깃허브 액션 사용하기</h1>
<ul>
  <li>
    깃허브 액션(github actions)은 깃허브에서 제공하는 서비스이다.
  </li>
  <li>
    리포지터리(코드 원격 저장소)에 특정 이벤트가 발생하면 <strong>특정 작업</strong>을 하거나, <strong>주기적으로 특정 작업을 반복</strong>할 수 있게 한다.
  </li>
</ul>

<br>

<h2>2-1. 깃허브 리포지터리 생성하고 코드 푸시하기</h2>
<ul>
  <li>
    새로운 리포지터리를 생성(실습 폴더명과 동일하게)하고 SSH로 접근할 수 있는 리포지터리 주소를 복사한다.
  </li>
  <li>
    작업한 폴더를 열고 "git init"을 수행하여 깃 저장소로 만든다.
  </li>
  <li>
    만들어진 리포지터리와 로컬에 생성한 깃 저장소를 remote로 연결한다.
  </li>
</ul>

<br>

<h2>2-2. 깃허브 액션 스크립트 작성하기, CI</h2>
<ul>
  <li>
    기존 프로젝트 최상단에 ".github/workflows/ci.yml" 스크립트를 작성하여 CI 설정을한다.
  </li>
</ul>

<br>

<h2>2-3. 깃허브 액션 스크립트 작성하기, CD</h2>
<ul>
  <li>
    현재 프로젝트를 빌드하면 일반 jar 파일과 plain 접미사가 붙은 jar파일이 생성된다. 이중 <strong>jar 파일</strong>을 사용해야 한다.
  </li>
    <ul>
      <li>
        plain이 붙은 jar 파일은 plain archive라 하며 <strong>의존성을 포함하지 않기 때문</strong>이다.
      </li>
      <li>
        build.gradle을 수정해서 plain 파일이 나오지 않도록할 수 있다.
      </li>
    </ul>
  <li>
    ".github/workflows/ci.yml"파일을 ".github/workflows/cicd.yml"로 변경하고 cd를 위한 코드를 추가한다.
  </li>
    <ul>
      <li>
        나의 경우 배포를 해두지는 않았기에 새로운 파일로 생성하고 주석처리한다.
      </li>
    </ul>
  <li>
    IAM은 AWS 리소스를 사용하도록 권한을 부여하는 서비스이다. [사용자] → [사용자 생성] → github-action으로 이름 지정.
  </li>
  <li>
    [다음]으로 넘어가 [직접 정책 연결]을 한 뒤 AdmisistratorAccessAWSElasticBeanstalk를 해제한다. 
  </li>
    <ul>
      <li>
        모든 관리 권한을 사용자에게 주는 옵션이며 모든 권한을 주는 것은 너무 광범위해 제한하는 것이다.
      </li>
    </ul>
  <li>
    사용자 생성을 마치면 사용자르 선택하여 액세스 키를 생성한다.
  </li>
    <ul>
      <li>
        액세스 키는 생성 시에 딱 한번 확인 가능하기 때문에 꼭 기록해 두고 유출되지 않도록 한다.
      </li>
    </ul>
  <li>
    키를 복사하였다면 [Settings → Secrets and variables → Actions]에서 새로운 비밀 키를 각각 등록한다.
  </li>
</ul>

<br>

<h2>2-4. AWS 리소스 정리하기</h2>
<ul>
  <li>
    엘라스틱 빈스토크르 제거하면 대부분 제거가 되기에 이는 간편한듯하다.
  </li>
    <ul>
      <li>
        S3는 비어있어야 삭제가 가능하다.
      </li>
    </ul>
</ul>