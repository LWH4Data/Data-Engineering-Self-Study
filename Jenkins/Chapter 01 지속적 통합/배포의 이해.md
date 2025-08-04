<ul>
  <li>
    실무에서 지속적 <strong>통합/배포(CI/CD)</strong>가 사용되는 방식과 소프트웨어 개발 방식에 끼치는 영향에 대해 설명한다.
  </li>
    <ul>
      <li>
        코드를 한 번에 병합하는 경우 회귀 결함(이전에 문제 없던 기능이 문제가 발생함) 혹은 코드 충돌 등이 생길 수 있다. CI/CD는 변경 사항이 많지 않을 때 <strong>자동적으로 통합/배포</strong>를 하여 문제를 줄일 수 있다.
      </li>
    </ul>
  <li>
    <strong>스프린트(sprint)</strong>: 애자일 개발 모델에서 분류된 일정량의 작업을 분석하고 구현하는 데 할당된 작업 기간을 의미한다.
  </li>
  <li>
    짧은 기간 안에 첫 번째 구현을 진행하며 브랜치에 푸쉬한다. 메인 브랜치는 빌드를 생성할 때 생성되며 Github에서는 main branch, Gitlab에서는 master branch라 한다.
  </li>
</ul>

<br>

<h1>1. 개발 워크플로</h1>
<h2>1-1. 로컬에서 단위 테스트 실행</h2>
<ul>
  <li>
    <strong>중앙 리포지토리(repository)</strong> → <strong>로컬로 clone</strong> → <strong>요구사항 구현</strong>
  </li>
  <li>
    요구 사항 구현 단계에서는 <strong>테스트 주도 개발(TDD, Test-Driven Development)</strong>를 주로 사용한다.
  </li>
  <li>
    <strong>테스트 주도 개발이란?</strong>
  </li>
    <ul>
      <li>
        코드를 구현하기 전 <strong>테스트 케이스</strong>를 먼저 작성.
      </li>
      <li>
        처음에는 테스트 케이스만 있기에 테스트 실행 시 모두 실패로 나온다. 그러나 <strong>구현부 코드를 채워나가면</strong> 점점 성공률이 올라간다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 중앙 리포지터리로 코드 푸시 및 병합</h2>
<ul>
  <li>
    개발자 기능 구현 → 중앙 리포지터리로 push → 메인 브랜치 merge
  </li>
</ul>

<br>

<h2>1-3. 병합 후 코드 컴파일</h2>
<li>
  메인 브랜치에 merge된 코드를 <strong>컴파일</strong>. 컴파일 과정에서 새로운 오류 발생 가능.
</li>

<br>

<h2>1-4.컴파일된 코드에서 테스트 실행</h2>
<ul>
  <li>
    <strong>단위 테스트</strong>와 <strong>통합 테스트</strong>를 실행하여 <strong>회귀 결함</strong> 여부 확인.
  </li>
  <li>
    필요 시 정적 분석 수행. 정적 분석이란 코딩 표준 준수 및 불필요한 코드 존재 여부 확인 등을 의미한다.
  </li>
</ul>

<br>

<h2>1-5. 아티팩트 배포</h2>
<ul>
  <li>
    병합된 코드의 단위별 품질 점검이 끝나면 모든 코드를 <strong>패키징</strong>하고, 서버에 <strong>배포</strong>한다.
  </li>
  <li>
    아티팩트(artifact)는 보통 .war 혹은 .jar 형식의 파일이다.
  </li>
</ul>

<br><br>

<h1>2. 지속적 제공/지속적 배포</h1>
<ul>
  <li>
    <strong>지속적 통합</strong>에서는 코드가 <strong>변경</strong>될 때마다 <strong>개발 환경에서 테스트가 수행</strong>되고 빌드 결과가 공개된다.
  </li>
  <li>
    개발 환경에서는 잘 동작하지만 <strong>프로덕션 환경</strong>에서 문제를 일으키는 경우도 있다.
  </li>
    <ul>
      <li>
        <strong>프로덕션 환경</strong>: 실제 사용자가 사용하는 <strong>운영 환경</strong>을 의미한다. 일반적으로 '개발 환경 → 스테이징 환경 → <strong>프로덕션 환경</strong>'으로 구성된다.
      </li>
    </ul>
  <li>
    애플리케이션이 자주 배포되지 않는 환경이라면 디버깅과 트러블슈팅이 어려울 수 있다.
  </li>
</ul>

<br>

<h1>3. CI/CD 워크플로 예제</h1>
<h2>3-1. 최신 코드 가져오기</h2>
<ul>
  <li>
    중앙 코드 리포지터리에서 로컬로 코드를 가져와 계산기 덧셈 기능 개발.
  </li>
</ul>

<br>

<h2>3-2. 단위 테스트 구현과 실행</h2>

```java
// 1. 하단의 코드 단위 테스트 코드이다.
// 아직 구현부 코드(Addition() 함수)를 작성하지 않아 단위 테스트는 실패한다.
{
  Result = Addition(10, 20);
Assert.assertEquals(Result, 30, "Addition functionality dose not work fine with positive numbers ");  
}
```

```java
// 2. 테스트 코드를 워해 단위 구현 함수(Addition())를 구현한다.
Addition(a, b)
{
  Result = a + b;
  return Result;
}

// 3. 2번 까지의 단위 구현이 완료되면 중앙 리포지터리에 푸쉬하여 Addition 함수를 병합한다.

//4. 중앙 리포지터리에서 테스트 실행을 하여 병합된 Addition() 함수와 기존의 기능들간 
// 문제가 발생하는지 확인한다.

// 5. 테스트에 문제가 없다면 프로덕션 환경에 배포한다.

// 6. E-E test (End to end test): UI 자동화 도구를 통해 애플케이션의 전체 워크플로가 
// 정상 동작하는지 확인한다.
```