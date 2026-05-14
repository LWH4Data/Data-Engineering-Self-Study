<h1>1. 사전 지식 : OAuth</h1>
<h2>OAuth란?</h2>
<ul>
  <li>
    OAuth는 제3의 서비스에 계정 관리를 맡기는 방식이다.
  </li>
    <ul>
      <li>
        <strong>리소스 오너(resource owner)</strong>: 서비스를 이용하는 사용자. 인증 서버에 자신의 정보를 사용하도록 허가하는 추체를 의미한다.
      </li>
      <li>
        <strong>리소스 서버(resource server)</strong>: 구글, 네이버 등 리소스 오너의 정보를 가지고 또 보호해주는 주체를 의미한다.
      </li>
      <li>
        <strong>인증 서버(authorization server)</strong>: 클라이언트에게 리소스 오너의 정보에 접근할 수 있는 토큰을 발급하는 역할을 하는 애플리케이션
      </li>
      <li>
        <strong>클라이언트 애플리케이션(client application)</strong>: 현재 개발 중인 서비스. 인증 서버에게 인증을 받고 리소스 오너의 리소를 사용하는 주체.
      </li>
    </ul>
  <li>
    리소스 오너 정보를 취득하는 네 가지 방법
  </li>
    <ul>
      <li>
        <strong>권한 부여 코드 승인 타입(authorization code grant type)</strong>
      </li>
        <ul>
          <li>
            OAuth 2.0에서 가장 잘 알려진 방법이다.
          </li>
          <li>
            클라이언트가 리소스에 접근하는 데 사용하며 <strong>권한에 접근할 수 있는 코드</strong>와 <strong>리소스 오너에 대한 액세스 토큰</strong>을 발급 받는 방식이다.
          </li>
        </ul>
      <li>
        <strong>암시적 승인 타입(implicit grant type)</strong>
      </li>
        <ul>
          <li>
            <strong>서버가 없는</strong> 자바스크립트 웹 애플리케이션 클라이언트에서 주로 사용한다.
          </li>
          <li>
            클라이언트가 요청을 보내면 <strong>리소스 오너의 인증 과정</strong> 이외에는 별다른 인증을 거치지 않고 액세스 토큰을 제공받는다.
          </li>
        </ul>
      <li>
        <strong>리소스 소유자 암호 자격증명 승인 타입(resource owner password credentials)</strong>
      </li>
        <ul>
          <li>
            <strong>클라이언트의 패스워드</strong>를 이용해 액세스 토큰에 대한 사용자의 자격 증명을 교환하는 방식이다.
          </li>
        </ul>
      <li>
        <strong>클라이언트 자격증명 승인 타입(client credentials grant)</strong>
      </li>
        <ul>
          <li>
            클라이언트가 <strong>컨텍스트 외부</strong>에서 액세스 토큰을 얻어 특정 리소스에 접근을 요청할 때 사용한다.
          </li>
        </ul>
    </ul>
  <li>
    이 중 권한 부여 코드 승인 타입을 도서에서 다룬다.
  </li>
    <ul>
      <li>
        사용자 데이터가 외부로 전송되지 않아 안전하다.
      </li>
      <li>
        OAuth에서 가장 잘 알려진 방식이다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 권한 부여 코드 승인 타입이란?</h2>
<ul>
  <li>
    권한 요청
    <br>→ 데이터 접근용 권한 부여
    <br>→ 인증 코드 발급
    <br>→ 액세스 토큰 발급
    <br>→ 액세스 토큰으로 데이터에 접근
  </li>
</ul>

<h3>1-2-1. 권한 요청이란?</h3>
<ul>
  <li>
    스프링 부트 서버가 특정 사용자 데이터에 접근하기 위해 권한 서버(카카오, 구글 등)에 요청을 보내는 것이다.
  </li>
  <li>
    요청 URI의 주요 파라미터
  </li>
    <ul>
      <li>
        <strong>client_id</strong>: 인증 서버가 클라이언트에게 할당한 <strong>고유 식별자</strong>이다. 클라이언트 애플리케이션을 <strong>OAuth 서비스에 등록</strong>할 때 서비스에서 생성한다.
      </li>
      <li>
        <strong>redirect_uri</strong>: 로그인 성공 시 이동해야 하는 URI이다.
      </li>
      <li>
        <strong>response_type</strong>: 클라이언트가 제공받길 원하는 <strong>응답타입</strong>이다. 인증 코드를 받을 때는 <strong>code값</strong>을 포함해야 한다.
      </li>
      <li>
        <strong>scope</strong>: 제공받고자 하는 <strong>리소스 오너의 정보 목록</strong>이다.
      </li>
    </ul>
</ul>

```java
// 1. 요청 형식.
GET spring-authorization-server.example/authorize?
  client_id=66a36b4c2&
  redirect_url=http://localhost:8080/myapp&
  response_type=code&
  scope=profile
```

<h3>1-2-2. 인증 코드 제공</h3>
<ul>
  <li>
    사용자가 로그인에 성공하면 권한 요청 시에 파라미터로 보낸 <strong>redirect_uri로 리다이렉션</strong>된다.
  </li>
    <ul>
      <li>
        이때 파라미터에 <strong>인증 코드</strong>를 함께 제공한다.
      </li>
    </ul>
</ul>

```text
GET http://localhost:8080/myapp?code=a1s2f3mcj2
```

<h3>1-2-3. 액세스 토큰 응답이란?</h3>
<ul>
  <li>
    인증 코드를 받으면, 클라이언트는 토큰 엔드포인트에 요청하여 <strong>액세스 토큰으로 교환</strong>해야 한다.
  </li>
    <ul>
      <li>
        액세스 토큰은 클라이언트가 사용자의 권한을 위임받아 보호된 리소스에 접근할 수 있음을 증명하는 <strong>자격 증명 토큰<strong>이다.
      </li>
    </ul>
  <li>
    보통 인증 서버의 <strong>/token 엔드포인트</strong>로
    <strong>POST 요청</strong>을 보낸다.
  </li>
</ul>

```JSON
// 액세스 토큰 교환 요청.
// 인가 코드(authorization code)를 액세스 토큰으로 교환하기 위해
// 인증 서버의 /token 엔드포인트로 POST 요청을 보낸다.
POST spring-authorization-server.example.com/token
{
  // OAuth 서비스에 등록된 클라이언트 식별자
  "client_id": "66a36b4c2",

  // OAuth 서비스에 등록할 때 발급받은 클라이언트 비밀키
  // 서버 사이드 애플리케이션에서 클라이언트를 인증할 때 사용한다.
  "client_secret": "aabb11dd44",

  // 인가 코드를 받을 때 사용했던 리다이렉트 URI
  // 토큰 요청 시에도 같은 값인지 검증하는 데 사용된다.
  "redirect_uri": "http://localhost:8080/myapp",

  // 토큰 발급 방식
  // 인가 코드를 액세스 토큰으로 교환하는 흐름이므로 authorization_code로 설정한다.
  "grant_type": "authorization_code",
  
  // 인증 서버가 발급한 인가 코드
  // 인증 서버는 이 코드가 유효한지 확인한 뒤, 유효하면 액세스 토큰을 응답한다.
  "code": "a1b2c3d4e5f6g7h8"
}
```

<h3>1-2-4. 액세스 토큰으로 API 응답 & 반환</h3>
<ul>
  <li>
    제공 받은 액세스 토큰으로는 <strong>리소스 오너의 정보</strong>를 가져올 수 있다.
  </li>
    <ul>
      <li>
        정보가 필요할 때마다 <strong>API 호출</strong>을 통해 정보를 가져온다.
      </li>
      <li>
        정보를 가져올 때 리소스 서버는 <strong>토큰이 유효한지 검사</strong>한 뒤에 응답한다.
      </li>
    </ul>
</ul>

```text
// 리소스 오너의 정보를 가져오기 위한 요청 사례
GET spring-authorization-resource-server.example.com/userinfo
Header: Authorization: Bearer aasdffb
```

<br>

<h2>1-3. 쿠키란?</h2>
<ul>
  <li>
    쿠키란 사용자가 어떤 웹사이트에 방문했을 때 <strong>[해당 웹사이트의 서버 → 사용자의 로컬 환경]</strong>에 저장하는 <strong>작은 데이터</strong>를 의미한다.
  </li>
    <ul>
      <li>
        쿠키를 통해 이전 방문 여부, 로그인 정보 등을 유지할 수 있다.
      </li>
      <li>
        쿠키는 키와 값으로 이루어져 있으며 만료 기간, 도메인 등의 정보를 가지고 있다.
      </li>
      <li>
        HTTP 요청을 통해 쿠키의 특정 키에 값을 추가할 수 있다.
      </li>
    </ul>
  <li>
    클라이언트의 정보 요청
    <br>→ 서버에서 정보를 값으로 넣은 쿠키를 생성하여 HTTP 헤더와 함께 반환.
    <br>→ 클라이언트의 브라우저에 쿠기를 저장.
    <br>→ 사이트 재방문 시에는 사용자가 로컬 환경에 있는 쿠키와 함께 서버에 요청.
  </li>
</ul>

<br><br>

<h1>2. 토큰 발급받기</h1>
<ul>
  <li>
    구글 로그인을 추가하기 위해 인증 서버(구글)에게 토큰을 제공받는다.
  </li>
  <li>
    p351의 과정을 그대로 따라하되 마지막의 <strong>client-id</strong>와 <strong>client-secret</strong>은 공유되어서는 안됨에 주의해야 한다.
  </li>
</ul>

<br><br>

<h1>3. 스프링 시큐리티로 OAuth2를 구현하고 적용하기</h1>
<ul>
  <li>
    스프링 시큐리티로 OAuth2를 구현한다.
  </li>
  <li>
    쿠기 관리 클래스 구현
    <br>→ OAuth2에서 제공받은 인증 객체로 사용자 정보를 가져오는 서비스 구현.
    <br>→ OAuth2 설정 파일 구현.
    <br>→ 테스트 뷰 구성.
  </li>
</ul>

<br>

<h2>3-1. 의존성 추가하기</h2>
<ul>
  <li>
    필요한 의존성을 build.gradle에 추가하고 새로고침한다.
  </li>
</ul>

<br>

<h2>3-2. 쿠기 관리 클래스 구현하기</h2>
<ul>
  <li>
    필요할 때마다 쿠기를 생성하고 삭제하는 것은 번거롭기에 쿠키 관리 클래스를 미리 구현해둔다. ("java/.../util/CookieUtil.java").
  </li>
</ul>

<br>

<h2>3-3. OAuth2 서비스 구현하기</h2>
<ul>
  <li>
    사용자 정보를 조회하여 users 테이블에 사용자 정보가 있다면 리소스 서버에서 제공해주는 이름을 업데이트하고 없다면 새 사용자를 생성해 DB에 저장한다. ("domain/User.java"에 사용자 이름을 추가).
  </li>
  <li>
    "config/oauth/OAuth2UserCustomService.java"를 생성한다.
  </li>
    <ul>
      <li>
        loadUser(): 리소스 서버에서 보내주는 사용자 정보를 불러오고 조회한다.
      </li>
      <li>
        saveOrUpdate(): users 테이블에 회원 데이터를 추가한다.
      </li>
    </ul>
</ul>

<br>

<h2>3-4. OAuth2 설정 파일 작성하기</h2>
<ul>
  <li>
    OAuth2와 JWT에 맞게 설정 파일을 수정한다.
  </li>
  <li>
    "config/WebSecurityConfig.java"를 모두 주석처리하고 "config/WebOAuthSecurityConfig.java" 파일을 생성하고 코드를 작성한다. 
  </li>
  <li>
    "config/oauth/OAuth2AuthorizationRequestBasedOnCookieRepository.java"에 OAuth2에 필요한 정보를 세션이 아닌 쿠키에 저장해서 쓸 수 있도록 인증 요청과 관련된 상태를 저장할 저장소 구현.
  </li>
  <li>
    인증 성공 시 실행할 핸들러를 구현한다. ("service/UserService.java").
  </li>
  <li>
    "config/oauth/OAuth2SuccessHandler.java"를 작성한다.
  </li>
</ul>

<br>

<h2>3-5. 글에 글쓴이 추가하기</h2>
<ul>
  <li>
    OAuth의 로직을 활용해 글에 글쓴이를 추가한다.
  </li>
  <li>
    "domain/Article.java"에 글쓴이로 사용할 author 변수를 추가한다.
  </li>
  <li>
    "dto/AddArticleRequest.java"에 toEntity() 메서드를 수정하여 author 값도 추가 저장하도록 한다.
  </li>
  <li>
    "service/BlogService.java"의 save() 메서드에서 유저 이름을 추가로 입력받고 toEntity()의 인수로 전달받은 유저 이름을 반환하도록 수정.
  </li>
  <li>
    "controller/BlogApiController.java" 파일에 현재 인증 정보를 가져오는 principal 객체를 파라미터로 추가한다.
  </li>
  <li>
    글 상세 페이지에서도 글쓴이의 정보가 보여야 하기에 "dto/ArticleViewResponse.java" 파일에서 author 필드 추가.
  </li>
  <li>
    스프링 부트가 실행될 때마다 데이터를 추가하기 위해 "resource/import.sql"에 author 컬럼 추가.
  </li>
  <li>
    뷰에서 글쓴이 정보가 보이도록 "resource/template/article.html"을 수정한다.
  </li>
</ul>

<br>

<h2>3-6. OAuth 뷰 구성하기</h2>
<ul>
  <li>
    로직은 완성되었기에 "controller/UserViewController.java"에서 login() 메서드 뷰를 oauthLogin으로 변경한다.
  </li>
  <li>
    구글 로그인을 표시할 로고는 p374의 구글 페이지에서 이미지를 받아오는 과정을 따라한다.
  </li>
  <li>
    OAuth 연결 버튼을 "templates/oauthLogin.html"파일에 코드를 입력한다.
  </li>
  <li>
    "/resource/static/js/token.js" 파일에 HTML 파일과 연결할 Js 코드를 작성한다.
  </li>
  <li>
    "resource/templates/articleList.html"에서 token.js를 가져올 수 있도록 파일을 수정한다.
  </li>
  <li>
    "/resources/static/js/article.js"의 기존 createButton을 수정하여 토큰 기반 요청을 하도록 한다.
  </li>
  <li>
    "resource/static/js/article.js"의 삭제, 수정 기능도 httpRequest() 함수를 사용하도록 수정한다.
  </li>
  <li>
    AI 기능들에는 Authorization 헤더를 추가로 보내도록 수정한다. 
  </li>
  <li>
    로그아웃 버튼을 누르면 저장하고 있던 액세스 토큰과 리프레시 토큰을 삭제할 수 있도록 코드를 추가한다.
  </li>
</ul>

<br>

<h2>3-7. 글 수정, 삭제, 글쓴이 확인 로직 추가하기</h2>
<ul>
  <li>
    자신의 글이 아닌데 수정 혹은 삭제를 시도하는 경우 예외를 발생 시키도록 코드 수정. ("service/BlogService.java").
  </li>
</ul>

<br><br>

<h1>4. OAuth2 실행 테스트하기</h1>
<ul>
  <li>
    "http://localhost:8080/login"에 접속해 [구글로 로그인하기] 버튼을 클릭한다.
  </li>
  <li>
    "/new-article"로 이동해 글을 등록해본다.
  </li>
  <li>
    개발자 도구에서 [Application → Local Storage]에 방문해서 access_token을 제거하고 다시 등록해 본다.
  </li>
</ul>

<br><br>

<h1>5. 테스트 코드 실패 해결하고 코드 수정하기</h1>
<ul>
  <li>
    지금까지의 코드를 테스트하기 위해 test 디렉터리를 우클리하고 [모든 테스트 실행]을 선택한다.
  </li>
  <li>
    "test/java/.../controller/BlogApiControllerTest"의 문제를 해결한다.
  </li>
</ul>