<ul>
  <li>
    드디어 여러 종류의 작업을 구성하고 다양한 방식으로 시작한다.
  </li>
  <li>
    여러 종류의 애플리케이션들은 각자 빌드와 배포 절차를 갖는다. 따라서 젠킨스에서 애플리케이션의 빌드 수명 주기를 구현하려면 먼저 각 애플리케이션의 <strong>빌드 수명 주기 단계</strong>와 <strong>사용되는 도구</strong>에 대해 이해해야 한다.
  </li>
  <li>
    교재에서는 TestNG와 메이븐 등의 도구들을 통해 자바 API 프로젝트와 프로젝트가 거치는 빌드 수명 주기 단계를 구현한다.
  </li>
  <li>
    12장 부터는 11장에서 빌드한 것을 기반으로 API 프로젝트를 자동 배포 할 수 있도록 다양한 종류의 젠킨스 빌드 방법을 다룬다.
  </li>
</ul>

<br>

<h1>1. 메이븐 빌드 도구의 이해</h1>
<ul>
  <li>
    메이븐의 핵심 목표는 개발자가 단시간 내에 <strong>전체 개발 상태를 이해</strong>하도록 돕는 것이다.
  </li>
</ul>

<h2>1-1. 자바 API 프로젝트 개발 과정</h2>
<h3>1-1-1. 서드파티 라이브러리 다운로드</h3>
<ul>
  <li>
    <strong>서드파티 라이브러리</strong>란 기본 라이브러리 외에 <strong>다른 API 개발자가 구현한 라이브러리</strong>를 의미한다.
  </li>
  <li>
    개발에 있어서는 기본 라이브러리 뿐만 아니라 서드파티 라이브러리도 필요하다.
  </li>
</ul>

<h3>1-1-2. 프로젝트에 라이브러리 추가</h3>
<ul>
  <li>
    다운로드한 라이브러리를 프로젝트 <strong>개발자가 작업 중인 레퍼런스 라이브러리에 추가</strong>한다. (자바 API 프로젝트의 경우 CLASSPATH에 추가).
  </li>
</ul>

<h3>1-1-3. 단위 테스트 케이스 작성</h3>
<ul>
  <li>
    라이브러리 추가가 완료 되었다면 해당 경로에서 특정 <strong>함수를 구현</strong>하여 개발을 시작한다.
  </li>
  <li>
    특정 함수가 구현되면 <strong>단위 테스트 케이스를 작성</strong>한다. (테스트 주도 개발 방식의 경우 함수 본문 구현 전 테스트 케이스를 먼저 작성한다).
  </li>
</ul>

<h3>1-1-4. 애플리케이션과 단위 테스트 케이스 코드 컴파일</h3>
<ul>
  <li>
    코드 작성 완료 후 <strong>API 소스 코드</strong>와 <strong>단위 테스트 케이스</strong>를 모두 컴파일 한다.
  </li>
</ul>

<h3>1-1-5. 테스트 케이스 실행</h3>
<ul>
  <li>
    컴파일이 완료된 뒤 TestNG, Pytest, NUnit 등의 <strong>테스트 도구</strong>를 통해 <strong>단위 테스트 케이스를 실행</strong>한다. (도구는 개발 환경에 따라 다름).
  </li>
</ul>

<h3>1-1-6. 애플리케이션 번들링/패키징</h3>
<ul>
  <li>
    단위 테스트와 코드 통합이 완료 되었다면 <strong>구현 결과를 라이브러리(.jar) 파일로 패키징</strong>한다.
  </li>
</ul>

<h3>1-1-7. 아티팩트 리포지터리로 릴리스</h3>
<ul>
  <li>
    라이브러리 버전이 생성되면 사용자가 다운로드 할 수 있도록 <strong>아티팩트 리포지터리로 릴리스</strong>한다.
  </li>
</ul>

<h3>1-1-8. 요약</h3>
<ul>
  <li>
    위의 단계들을 모두 수작업으로 진행한다면 번거로우면서 오류 또한 빈번하게 발생한다. 따라서 젠킨스가 필요하다.
  </li>
  <li>
    위의 작업을 자동으로 수행하는 도구들에는 아파치 앤트(Apache Ant), 메이븐(Maven), 그래들(Gradle) 등이 있으며 이들을 <strong>빌드 도구(build tool)</strong>라 한다.
  </li>
</ul>

<br>

<h2>1-2. 자바 API 프로젝트 빌드</h2>
<ul>
  <li>
    메이븐 빌드 도구와 자바 API로 프로젝트를 빌드하는 실습을 진행한다. (+ Eclipse).
  </li>
  <li>
    해당 영역은 일반적인 환경 구성으로 따라하기만 하면 된다.
  </li>
</ul>

<br>

<h2>1-3. 메이븐 프로젝트 디렉터리 구조</h2>
<ul>
  <li>
    메이븐 프로젝트 디렉터리는 프로젝트 생성 시 Artifact Id 필드에 입력한 이름으로 생성된다.
  </li>
</ul>

<h3>1-3-1. src/main/java</h3>
<ul>
  <li>
    자바 패키지의 기본 소스 코드 디렉터리로 해당 위치에 <strong>소스 코드</strong>가 위치한다.
  </li>
  <li>
    Group Id와 Artifact Id를 갖는 패키지 디렉터리가 위치한다. 현재 각 명칭은 아래와 같다. (데모 파일인 App.java는 삭제).
  </li>
    <ul>
      <li>
        <strong>Group Id</strong>: Pranodayd
      </li>
      <li>
        <strong>Artifact Id</strong>: CalculatorAPI
      </li>
    </ul>
</ul>

<h3>1-3-2. src/test/java</h3>
<ul>
  <li>
    단위 테스트 케이스 파일들이 위치한다. (Apptest.java는 테스트 케이스용 템플릿 파일로 삭제한다).
  </li>
  <li>
    Group Id와 Artifact Id로 생성된 패키지 디렉터리가 위치한다.
  </li>
</ul>

<h3>1-3-3. pom.xml</h3>
<ul>
  <li>
    뒤에서 설명.
  </li>
</ul>

<br>

<h2>1-4. 자바 API 프로젝트 코드 파일</h2>
<h3>1-4-1. API 소스 코드</h3>
<ul>
  <li>
    <strong>src/main/java</strong>의 패키지 디렉터리 구조 안에 Calculator.java 파일 생성, <strong>기본 함수</strong>가 위치한다.
  </li>
</ul>

<h3>1-4-2. API 단위 테스트 코드</h3>
<ul>
  <li>
    <strong>src/test/java</strong>의 디렉터리 구조 안에 API에 구현된 모든 함수에 대한 <strong>단위 테스트 케이스</strong>가 담긴 자바 파일을 생성한다.
  </li>
  <li>
    테스트 케이스들은 <strong>TestNG</strong>라는 단위 테스트 도구를 통해 실행된다.
  </li>
    <ul>
      <li>
        TestNG는 @BeforeClass, @AfterClass, @Test, @BeforeMethod 등의 <strong>어노테이션(annotation)</strong>으로 작성한 메서드를 통해 테스트 케이스를 제어하는 <strong>단위 테스트 도구</strong>이다.
      </li>
      <li>
        <strong>테스트 보고서</strong>를 생성할 수도 있다.
      </li>
    </ul>
</ul>

<br>

<h2>1-5. 자바 API 프로젝트의 pom.xml 파일</h2>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>Pranodayd</groupId>
  <artifactId>CalculatorAPI</artifactId>
  <version>1.0</version>

  <name>CalculatorAPI</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <!-- 
  <properties>
  - .JAVA 파일을 컴파일할 때 필요한 속성들을 정의한다.
  - 텍스트 인코딩(UTF-8, ANSI, etc), 자바 버전 등
   -->
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.release>17</maven.compiler.release>
  </properties>

  <!-- 
  <dependencies>
  - 서드 파티 라이브러리와 해당 라이브러리가 필요한 단계(컴파일, 단위 테스트, 애플리케이션
     등)를 정의한다.
   -->
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>org.junit</groupId>
        <artifactId>junit-bom</artifactId>
        <version>5.11.0</version>
        <type>pom</type>
        <!-- 
        < scope >
        - 단위 테스트 케이스를 실행할 때만 프로젝트의 CLASSPATH에 TestNG JAR파일을 
          배치한다고 정의.
        - 따라서 단위 테스트가 종료되면 TestNG JAR 파일들은 프로젝트의 CLASSPATH에서 
          제거된다.
        - 수명 주기별로 필요한 의존성을 정의 
          → 로컬 리포지터리 내부의 중앙 리포지터리에 다운로드 
          → 프로젝트 CLASSPATH에 추가.
        - 메이븐이 이렇게 기본적으로 생성하는 로컬 리포지터리 경로는 ${user.home}/.m2
          /repository 이다.
        - 빌드를 실행
          → 로컬 리포지터리 내의 필요한 의존성 가용 여부 확인
          → 가용가능 하면 CLASSPATH에 추가, 불가하다면 다음 단계
          → 중앙 리포지터리에서 로컬 리포지터리로 다운.
          → 프로젝트의 CLASSPATH에 추가.
        - 메이븐이 로컬 리포지터리에 의존성을 다운할 때 경로는 GroupId/ArtifactId/Version
          이 되며 해당 경로에 testing-7.4.0.jar 파일이 다운된다.
        -->
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>

  <dependencies>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-api</artifactId>
      <scope>test</scope>
    </dependency>
    <!-- Optionally: parameterized tests support -->
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-params</artifactId>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <!-- 
  <settings></settings>
  - 로컬 리포지터리의 기본 위치를 다른 위치로 변경할 수 있다.
   -->

  <!-- 
  < build >
  - 단계별로 필요한 메이븐 플로그인과 애플리케이션의 전체 빌드 수명 주기를 정의.
  -->
  <build>
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
      <plugins>
        <!-- clean lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle -->
        <plugin>
          <artifactId>maven-clean-plugin</artifactId>
          <version>3.4.0</version>
        </plugin>
        <!-- default lifecycle, jar packaging: see https://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_jar_packaging -->
        <plugin>
          <artifactId>maven-resources-plugin</artifactId>
          <version>3.3.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.13.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.3.0</version>
        </plugin>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.4.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-install-plugin</artifactId>
          <version>3.1.2</version>
        </plugin>
        <plugin>
          <artifactId>maven-deploy-plugin</artifactId>
          <version>3.1.2</version>
        </plugin>
        <!-- site lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#site_Lifecycle -->
        <plugin>
          <artifactId>maven-site-plugin</artifactId>
          <version>3.12.1</version>
        </plugin>
        <plugin>
          <artifactId>maven-project-info-reports-plugin</artifactId>
          <version>3.6.1</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>
```

<br>

<h2>1-6. 빌드 수명 주기 단계와 순서</h2>
<h3>1-6-1. 정리(Clean)</h3>
<ul>
  <li>
    maven-clean-plugin을 사용해 이전에 생성된 모든 컴파일 파일과 패키지 파일 정리, 새로운 빌드 수명 주기 실행.
  </li>
</ul>

- p174