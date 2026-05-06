<h1>0. 그림으로 이해하는 프로젝트</h1>
<ul>
  <li>
    웹 브라우저의 POST 요청
    <br>→ BlogApiController 클래스의 특정 메소드 addArticle() 메소드가 요청을 받음.
    <br>→ 받은 요청을 BlogService 클래스의 save() 메소드를 실행.
    <br>→ save() 메소드는 BlogRepository 클래스, Ariticle 클래스를 거쳐 실제 테이블에 데이터를 저장한다.
  </li>
</ul>

<br><br>

<h1>1. 사전 지식: API와 REST API</h1>
<ul>
  <li>
    네트워크에서 API는 <strong>프로그램 간에 상호작용하기 위한 매개체</strong>를 의미한다.
  </li>
</ul>

<br>

<h2>1-1. 식당으로 알아보는 API</h2>
<ul>
  <li>
    식당으로 비유하면 "손님: 클라이언트", "점원: API", "요리사: 서버"로 이해할 수 있다.
  </li>
  <li>
    API는 클라이언트의 요청을 서버에 전달하고, 서버의 결과물을 클라이언트에게 돌려주는 역할을 한다.
  </li>
</ul>

<br>

<h2>1-2. 웹의 장점을 최대한 활용하는 REST API</h2>
<ul>
  <li>
    REST API는 <strong>웹의 장점</strong>을 최대한 활용한 API이다.
  </li>
  <li>
    REST는 Representational State Transfer를 줄인 표현으로 자원을 <strong>이름으로 구분</strong>해 자원의 상태를 주고받는 API 방식이다. (명확하고 이해하기 쉽다).
  </li>
  <li>
    REST API는 스프링 부트, 리액트, Vue.js 등의 특정 기술이 아니라 <strong>URL의 설계 방식</strong>이다.
  </li>
</ul>

<h3>1-2-1. REST API의 특징</h3>
<ul>
  <li>
    REST API는 서버/클라이언트 구조, 무상태, 캐시 처리 가능, 게층화, 인터페이스 일관성과 같은 특징이 있다.
  </li>
    <ul>
      <li>
        개발하며 익히면 된다.
      </li>
    </ul>
</ul>

<h3>1-2-2. REST API의 장점과 단점</h3>
<ul>
  <li>
    REST API의 장점은 <strong>URL(주소와 메소드)만 보고도</strong> 무슨 행동을 하는 API인지 명확하게 알 수 있다는 점이다.
  </li>
  <li>
    상태가 없다는 점은 클라이언트와 서버의 <strong>역할이 명확히 분리</strong>되고 <strong>HTTP 표준</strong>을 사용하는 모든 플랫폼에서 사용할 수 있다는 장점이 있다.
  </li>
    <ul>
      <li>
        단점은 HTTP 메소드(GET, POST 등) 방식의 <strong>개수 제한</strong>이 있고, 설계를 위한 <strong>공식적인 표준 규약</strong>이 없다는 점이다.
      </li>
    </ul>
</ul>

<h3>1-2-3. REST API를 사용하는 방법</h3>
<h4>1-2-3-1. 규칙 1. URL에는 동사를 쓰지 말고, 자원을 표시해야 한다</h4>
<ul>
  <li>
    자원은 <strong>가져오는 데이터</strong>를 의미한다.
  </li>
  <li>
    자원의 명칭은 동일하짐만 동사(메소드)의 명칭은 개발자마다 다를 수 있어 <strong>동사 사용을 지양</strong>해야 한다.
  </li>
  <li>
    예를 들어 "/student/1 (O) ↔ /get-student?student_id=1 (X)", get-student는 동사이다.
  </li>
</ul>

<h4>1-2-3-2. 동사는 HTTP 메소드로</h4>
<ul>
  <li>
    URL에 쓰지 못하는 동사는 <strong>HTTP 메소드</strong>로 해결된다.
  </li>
  <li>
    HTTP 메소드란 <strong>서버에 요청을 하는 방법</strong>을 나눈 것이다.
  </li>
    <ul>
      <li>
        자주 사용되는 HTTP 메소드는 <strong>POST, GET, PUT, DELETE</strong>가 있으며 각각 <strong>만들기(create), 읽기(read), 업데이트(update), 삭제(delete)</strong>를 의미하며 <strong>CRUD</strong>라고도 부른다.
      </li>
      <li>
        GET, POST, PUT, CELETE는 URL에 입력하는 것이 아니라 <strong>내부적으로 처리하는 방식을 미리 정한 것</strong>이다.
      </li>
      <li>
        HTTP 메소드는 내부에서 서로 다른 함수로 처리한다.
      </li>
    </ul>
  <li>
    슬래시는 계층 관계, 밑줄 대신 하이픈, 자원의 종류 등 다양한 기준도 존재한다.
  </li>
</ul>

<br><br>

<h1>2. 블로그 개발을 위한 엔티티 구성하기</h1>
<ul>
  <li>
    엔티티를 구성하고, 구성한 엔티티를 위한 리포지터리를 추가한다.
  </li>
</ul>

<br>

<h2>2-1. 프로젝트 준비하기</h2>
<ul>
  <li>
    보통 디렉터리는 <strong>계층</strong>별로 분리하거나 <strong>도메인 단위</strong>로 구분해서 분리한다.
  </li>
    <ul>
      <li>
        도서는 계층별로 코드를 디렉터리에 넣어 분리한다.
      </li>
    </ul>
</ul>

<br>

<h2>2-2. 엔티티 구성하기</h2>
<ul>
  <li>
    빌더 패턴이라는 디자인 패턴을 사용하면 어느 필드에 어떤 값이 들어가는지 명시적으로 파악할 수 있다.
  </li>
  <li>
    <strong>롬복</strong>을 통해 Getter와 protected 생성자를 코드로 구현하지 않고 <strong>애너테이션으로 대체</strong>할 수 있다.
  </li>
</ul>

```java
// 1. 빌더 패턴.
// 1-1. 빌더 패턴 사용 X
new Article("abc", "def");
// 1-2. 빌더 패턴 사용 O
Article.builder()
  .title("abc")
  .content("def")
  .build();
```

<br>

<h2>2-3. 리포지터리 만들기</h2>
<ul>
  <li>
    내용이 없으므로 필기 skip.
  </li>
</ul>

<br><br>

<h1>3. 블로그 글 작성을 위한 API 구현하기</h1>
<ul>
  <li>
    엔티티 구성이 완료 되었으니 API를 하나씩 구현한다.
  </li>
  <li>
    서비스 클래스에서 메소드 구현
    <br>→ 컨트롤러에서 사용할 메소드 구현.
    <br>→ API 테스트.
  </li>
</ul>

<br>

<h2>3-1. 서비스 메서드 코드 작성하기</h2>
<ul>
  <li>
    서비스 계층에서 요청을 받을 객체 AddArticleRequest 생성.
    <br>→ BlogService 클래스를 생성.
    <br>→ 블로그 글 추가 메소드 save() 구현.
  </li>
  <li>
    DTO(Data Transfer Object)는 <strong>계층끼리 데이터를 교</strong>하기 위해 사용하는 객체이다.
  </li>
    <ul>
      <li>
        DAO는 DB와 연결되어 데이터를 조회하고 수정하는 객체라 데이터 수정 로직이 포함되지만 DTO는 단순히 데이터를 <strong>옮기는 역할</strong>을 하기 때문에 <strong>비즈니스 로직을 포함하지 않는다</strong>.
      </li>
    </ul>
</ul>

<br>

<h2>3-2. 컨트롤러 메소드 코드 작성하기</h2>
<ul>
  <li>
    URL을 매핑하기 위한 컨트롤러 메소드 추가.
  </li>
  <li>
    컨트롤러 메소드에는 URL 매핑 애너테이션 @GetMapping, @PostMapping, @PutMapping, @DeleteMapiing 등을 사용할 수 있다.
  </li>
  <li>
    BlogService의 save() 메소드를 호출하고, 생성된 블로그 글을 반환하는 작업을 할 addArticle() 메소드를 작성.
  </li>
</ul>

<br>

<h2>3-3. API 실행 테스트하기</h2>
<ul>
  <li>
    실제 데이터를 확인하기 위해 H2 콘솔을 활성화한다.
  </li>
  <li>
    build.gradle에 의존성 추가.
    <br>→ application.yml에 코드 추가.
    <br>→ 스프링 부트 서버 시작.
    <br>→ HTTP로 요청 보내기.
    <br>→ 응답 확인 후 실제 DB 저장 여부 확인.
  </li>
</ul>

<br>

<h2>3-4. 반복 작업을 줄여 줄 테스트 코드 작성하기</h2>
<ul>
  <li>
    직접 매번 H2 콘솔에 접속하는 것은 번거롭기 때문에 이를 간편화할 테스트 코드를 작성한다.
  </li>
  <li>
    HTTP에서는 JSON을, 자바에서는 객체를 사용한다. 따라서 <strong>형식을 맞게 변환</strong>하는 작업이 필요하며 이를 <strong>직렬화, 역직렬화</strong>라 한다.
  </li>
    <ul>
      <li>
        자바의 직렬화란 자바 시스템 내부에서 사용되는 객체를 외부에서 사용하도록 데이터를 변환하는 작업을 의미한다.
      </li>
      <li>
        자바의 역직렬화란 외부에서 사용하는 데이터를 자바의 객체 형태로 변환하는 작업을 의미한다.
      </li>
    </ul>
</ul>

<br><br>

<h1>4. 블로그 글 목록 조회를 위한 API 구현하기</h1>
<ul>
  <li>
    모든 글을 조회하는 API와 글 내용을 조회하는 API를 순서대로 구현한다.
  </li>
</ul>

<br>

<h2>4-1. 서비스 메서드 코드 작성하기</h2>
<ul>
  <li>
    내용이 없으므로 정리는 skip.
  </li>
</ul>

<br>

<h2>4-2. 컨트롤러 메소드 코드 작성하기</h2>
<ul>
  <li>
    /api/articles GET 요청이 들어오면 글 목록을 조회할 findAllArticles() 메소드 작성.
  </li>
  <li>
    먼저 DTO를 작성.
    <br>→ controller 디렉터리의 BlogApiController.java에 findAllArticle() 메소드 추가.
  </li>
</ul>

<br>

<h2>4-2. 실행 테스트하기</h2>
<ul>
  <li>
    직접 데이터를 주입하고 포스트맨으로 요청을 보내 확인한다.
  </li>
</ul>

<br>

<h2>4-3. 테스트 코드 작성하기</h2>
<ul>
  <li>
    글 조회 테스트 역시 편의를 위해 테스트 코드를 활용할 수 있다.
  </li>
</ul>

<br><br>

<h1>5. 블로그 글 조회 API 구현하기</h1>
<ul>
  <li>
    글 하나를 조회하는 API를 생성한다.
  </li>
</ul>

<br>

<h2>5-1. 서비스 메서드 코드 작성하기</h2>
<ul>
  <li>
    BlogService.java 파일을 열어 블로글 하나를 조회하는 메소드 findById()를 작성한다.
  </li>
</ul>

<br>

<h2>5-2. 컨트롤러 메소드 코드 작성하기</h2>
<ul>
  <li>
    "/api/articles/{id} GET 요청이 들어오면 블로그 글을 조회하기 위해 매핑할 findArticle() 메소드를 작성한다. (BlogApiController.java).
  </li>
</ul>

<br>

<h2>5-3. 테스트 코드 작성하기</h2>
<ul>
  <li>
    마찬가지로 편리한 테스트를 위해 테스트 코드를 작성하며 given, when, then 구조를 활용한다.
  </li>
</ul>

<br><br>

<h1>6. 블로그 글 삭제 API 구현하기</h1>
<h2>6-1. 서비스 메소드 코드 작성하기</h2>
<ul>
  <li>
    BlogService.java 파일에 delete() 메소드를 추가한다.
  </li>
    <ul>
      <li>
        블로그 글의 ID를 받아 JPA에서 제공하는 deleteById() 메소드를 통해 DB의 데이터를 삭제한다.
      </li>
    </ul>
</ul>

<br>

<h2>6-2. 컨트롤러 메서드 코드 작성하기</h2>
<ul>
  <li>
    "/api/articles/{id} DELETE" 요청이 오면 글을 삭제하기 위한 deleteArticle() 메소드를 작성한다.
  </li>
</ul>

<br>

<h2>6-3. 실행 테스트하기</h2>
<ul>
  <li>
    포스트맨을 활용하여 데이터를 삭제하고 조회하는 테스트를 진행한다.
  </li>
</ul>

<br>

<h2>6-4. 테스트 코드 작성하기</h2>
<ul>
  <li>
    간편하게 테스트하기 위해 테스트 코드를 작성한다.
  </li>
</ul>

<br>

<h1>7. 블로그 글 수정 API 구현하기</h1>
<h2>7-1. 서비스 메서드 코드 작성하기</h2>
<ul>
  <li>
    수정 API를 위해 서비스 메소드를 작성한다. (일종의 Setter).
  </li>
    <ul>
      <li>
        Article.java에 update() 메소드를 추가한다.
      </li>
    </ul>
  <li>
    이후 수정 요청을 받을 DTO를 작성한다.
  </li>
  <li>
    BlogService 파일에 글을 수정하는 update() 메소드 추가.
  </li>
</ul>

<br>

<h2>7-2. 컨트롤러 메서드 코드 작성하기</h2>
<ul>
  <li>
    "/api/articles/{id} PUT" 요청이 오면 글을 수정하기 위한 updateArticle() 메소드를 작성한다.
  </li>
</ul>

<br>

<h2>7-3. 실행 테스트 하기</h2>
<ul>
  <li>
    포스트맨을 통해 테스트 확인.
  </li>
</ul>

<br>

<h2>7-4. 테스트 코드 작성</h2>
<ul>
  <li>
    포스트맨을 사용하지 않고 간편히 테스트하기 위한 테스트 코드를 작성한다. (given, when, then).
  </li>
</ul>