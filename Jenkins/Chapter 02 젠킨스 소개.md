<ul>
  <li>
    CI/CD 프로세스를 자동화하고 생산성을 높이는 자동화 서버 Jenkins 소개.
  </li>
  <li>
    애자일 방법론은 변경된 코드가 반영됨과 동시에 실행 가능한 제품을 출시할 수 있다. 마찬가지로 젠킨스는 코드 변화가 바로 CI/CD가 이루어지기에 철학적 가치가 유사하다.
  </li>
  <li>
    젠킨스는 다양한 플랫폼에 애플리케이션 빌드가 가능하다. 또한 산춘물 발행과 pull-request 통합 절차도 자동화할 수 있다.
  </li>
  <li>
    젠킨스는 단위 테스트, 통합 테스트, 컨테이너 테스트를 조합하여 고품질의 빌드를 생성하는 역할을 한다. 이는 개별적으로 다루는 것보다 긍정적이다.
  </li>
</ul>

<br>

<h1>1. 젠킨스란?</h1>
<ul>
  <li>
    개발 프로세스의 <strong>다양한 단계를 자동화</strong>한다.
  </li>
    <ul>
      <li>
        최신 코드 가져오기, 소스 코드 컴파일, 단위 테스트 실행 → 패키징, 산출물 → 배포
      </li>
    </ul>
  <li>
    <strong>자바</strong> 기반이며 <strong>서블릿 컨테이너(servlet container)</strong> 내부에서 실행된다.
  </li>
    <ul>
      <li>
        <strong>서블릿 컨테이너</strong>: 자바 코드(Servlet)를 실행하고 응답을 만들어 주는 역할을 하는 서버 시스템.
      </li>
    </ul>
</ul>

<br>

<h2>1-1. 젠킨스의 역사</h2>
<ul>
  <li>
    코드 오류로 인한 빌드 실패 문제 개선 수요 <br> → 소스 리포지터리 커밋 전 코드 작동 여부 확인 수요<br>→ Hudson이라는 자동화 서버 개발<br>→ 오라클과의 분쟁으로 Jenkins와 Hudson으로 이원화 됨 <br>→ Jenkins가 살아남음.
  </li>
</ul>

<br>

<h2>1-2. 젠킨스를 이용한 CI/CD 구현</h2>
<ul>
  <li>
    CI/CD 프로세스: 애플리케이션 <strong>코드에 변경</strong>이 발생하면 배포가 될 때까지 <strong>E-E 빌드 수명주기 단계에서 검증</strong>을 하는 프로세스.
  </li>
  <li>
    젠킨스 자동화 서버는 <strong>도메인 특화 언어(DSL, Domain Specific Language)</strong>로 빌드 수명 주기 단계를 구축한다.
  </li>
    <ul>
      <li>
        도메인 특화 언어(DSL): 특정 분야에 특화되어 설계된 언어.
      </li>
    </ul>
  <li>
    젠킨스에는 <strong>파이프라인</strong>이라 불리는 <strong>스크립트</strong>가 있다. 스크립트를 활용하여 각 빌드 단계마다 젠킨스가 <strong>수행할 태스크</strong> 및 <strong>하위 태스크의 순서</strong>를 정의한다.
  </li>
</ul>

<br>

<h2>1-3. 젠킨스 아키텍처</h2>
<ul>
  <li>
    젠킨스의 CI/CD 프로세스
  </li>
    <ul>
      <li>
        각 개발자가 작업 후 중앙 리포지터리에 <strong>push</strong><br>→ 브랜치 변경 사항을 젠킨스에 <strong>통보</strong><br>→ 젠킨스 <strong>작업(job) 시작</strong>.
      </li>
    </ul>
  <li>
    젠킨스의 작업(job)
  </li>
    <ul>
      <li>
        리포지터리에서 변경된 파일을 <strong>가져온다</strong>.<br>→ 변경된 파일들을 <strong>컴파일</strong> 한다.<br>→ 컴파일된 코드의 <strong>단위/통합 테스트를 실행</strong>한다.<br>→ <strong>정적 분석</strong>(코딩 표준 준수 여부, 데드 코드 확인).<br>→ 완료된 파일들을 .jar 혹은 .war과 같은 <strong>라이브러리 형태로 번들링</strong>.<br>→ 빌드된 라이브러리 파일을 <strong>테스트/프로덕션 환경으로 배포</strong>.<br>→ E-E 테스트 자동화 도구를 통해 배포된 <strong>애플리케이션을 대상으로 테스트</strong>.<br>→ 새로 생성된 애플리케이션 및 E-E 테스트 결과 이메일로 <strong>팀원에게 공유</strong>.
      </li>
    </ul>
</ul>