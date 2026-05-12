<h1>1. 사전 지식: 토큰 기반 인증</h1>
<h2>1-1. 토큰 기반 인증이란?</h2>
<ul>
  <li>
    대표적인 사용자 인증 확인 방법으로는 <strong>서버 기반 인증</strong>과 <strong>토큰 기반 인증</strong>이 있다.
  </li>
    <ul>
      <li>
        서버 기반 인증은 앞서 배운 스프링 시큐리티가 기본적으로 제공하는 <strong>세션 기반 인증</strong>이다.
      </li>
        <ul>
          <li>
            <strong>사용자마다 사용자의 정보를 담은 세션</strong>을 생성하고 저장해서 인증을 한다.
          </li>
        </ul>
      <li>
        토큰 기반 인증은 <strong>토큰</strong>을 사용하는 방식이다.
      </li>
        <ul>
          <li>
            토큰은 서버가 클라이언트를 구분하기 위한 유일한 값이다.
          </li>
          <li>
            서버가 토큰을 생성하여 클라이언트에게 제공하면 클라이언트는 토큰을 가지고 있고, <strong>토큰을 요청과 함께 전달</strong>하면 서버는 이를 보고 유효한 사용자인지 검증한다.
          </li>
        </ul>
    </ul>
  <li>
    토큰 기반 방식은 <strong>세션에 대한 부담</strong>은 줄이고 서버를 <strong>stateless</strong>하게 만들어준다. 다만 <strong>토큰 관리</strong>와 <strong>보안 설계</strong>가 더 중요해지는 특징도 생긴다.
  </li>
</ul>

<h3>1-1-1. 토큰을 전달하고 인증받는 과정</h3>
<ul>
  <li>
    클라이언트가 아이디와 비밀번호를 서버에 전달한다.
    <br>→ 서버는 클라이언트가 유요하면 토큰을 생성해 반환한다.
    <br>→ 클라이언트는 반환 받은 토큰을 저장한다.
    <br>→ 이후 인증이 필요한 API를 사용할 때 클라이언트는 토큰을 함께 보낸다.
    <br>→ 서버는 전달받은 요청과 함께 토큰이 유효한지 확인한다.
    <br>→ 토큰이 유효하다면 서버는 요청을 처리한다.
  </li>
</ul>

<h3>1-1-2. 토큰 기반 인증의 특징</h3>
<h4>1-1-2-1. 무상태성</h4>
<ul>
  <li>
    사용자의 인증 정보가 담긴 토큰은 서버가 아닌 <strong>클라이언트에 저장</strong>되기에 <strong>서버는 토큰을 저장할 필요가 없으며 이를 무상태성</strong>이라 한다.
  </li>
    <ul>
      <li>
        서버는 토큰을 저장하지 않는만큼 자원을 아낄 수 있다.
      </li>
    </ul>
  <li>
    클라이언트는 토큰을 저장한 상태에서 <strong>사용자의 인증 상태를 유지</strong>하면서 이후 요청을 처리하는데 이를 <strong>상태 관리</strong>라고 한다.
  </li>
</ul>

<h4>1-1-2-2. 확장성</h4>
<ul>
  <li>
    무상태성은 확장성에 영향을 준다.
  </li>
    <ul>
      <li>
        서버를 확장할 때에 <strong>상태 관리</strong>를 신경 쓸 필요가 없기 때문에 서버 확장이 유리하다.
      </li>
      <li>
        예를 들어 주문 서버와 결제 <strong>서버가 분리된 경우</strong>에도 클라이언트가 저장하고 있는 <strong>토큰 하나</strong>로 요청을 보낼 수 있다.
      </li>
      <li>
        페이스북 로그인, 구글 로그인 등 토큰 기반 인증을 사용하는 다른 시스템에 접근해 <strong>로그인 방식 확장</strong>이 가능하다.
      </li>
    </ul>
</ul>

<h4>1-1-2-3. 무결성</h4>
<ul>
  <li>
    토큰 방식은 <strong>HMAC(hash-based message authentication)</strong> 기법이라고도 부른다.
  </li>
    <ul>
      <li>
        토큰을 발급한 이후에는 <strong>토큰 정보를 변경</strong>하는 행위를 할 수 없다. 즉 <strong>무결성</strong>이 보장된다.
      </li>
    </ul>
</ul>

<br>

<h2>1-2. JWT</h2>
<ul>
  <li>
    발급받은 JWT를 통해 인증하기 위해서는 <strong>HTTP 요청 헤더</strong>에 <strong>Authorization 키 값에 Bearer + JWT 토큰값</strong>을 넣어 전송한다.
  </li>
  <li>
    JWT는 <strong>"."을 기준으로 헤더(header), 내용(payload), 서명(signature)</strong>으로 이루어져 있다.
  </li>
    <ul>
      <li>
        aaaaa. bbbbbb. cccccc
      </li>
      <li>
        헤더(aaaaa)는 <strong>토큰의 타입</strong>과 <strong>해싱 알고리즘</strong>을 지정하는 정보를 담는다.
      </li>
        <ul>
          <li>
            typ: 토큰 타입을 지정한다.
          </li>
          <li>
            alg: 해싱 알고리즘을 지정한다.
          </li>
        </ul>
      <li>
        내용(bbbbbb)에는 <strong>토큰과 관련된 정보</strong>를 담는다.
      </li>
        <ul>
          <li>
            내용의 한 덩어리를 <strong>클레임(claim)</strong>이라고 한다.
          </li>
            <ul>
              <li>
                클레임은 <strong>키값의 한 쌍</strong>으로 이루어져 있다.
              </li>
              <li>
                클레임에는 다음 세 가지 종류가 있다.
              </li>
                <ul>
                  <li>
                    <strong>등록된 클레임(registered claim)</strong>: 토큰에 대한 정보를 담는 데 사용한다. (정보에 대해서는 p319 참고).
                  </li>
                  <li>
                    공개 클레임(public claim)
                  </li>
                    <ul>
                      <li>
                        <strong>공개</strong>되어도 상관없는 클레임을 의미한다.
                      </li>
                      <li>
                        <strong>충돌을 방지</strong>할 수 있는 이름을 가져야하며 보통 클레임 이름을 <strong>URI</strong>로 짓는다.
                      </li>
                    </ul>
                  <li>
                    비공개 클레임(private claim)
                  </li>
                    <ul>
                      <li>
                        <strong>공개되면 안되는 클레임</strong>을 의미한다.
                      </li>
                      <li>
                        클라이언트와 서버 간의 <strong>통신</strong>에 사용된다.
                      </li>
                    </ul>
                </ul>
            </ul>
        </ul>
      <li>
        내용(cccccc)은 해당 토큰이 <strong>조작되었거나 변경되지 않았음</strong>을 확인하는 용도이다.
      </li>
        <ul>
          <li>
            <strong>헤더의 인코딩값</strong>과 <strong>내용의 인코딩값</strong>을 합친 후에 주어진 <strong>비밀키</strong>를 사용해 <strong>해시값을 생성</strong>한다.
          </li>
        </ul>
    </ul>
</ul>

```JSON
// 1. JWT 헤더의 예.
{
  "typ": "JWT",     // JWT 토큰
  "alg": "HS256"    // HS256 해싱 알고리즘.
}

// 2. JWT 내용의 예.
{
  // 등록된 클레임
  "iss": "ajufresh@gamil.com",
  // 등록된 클레임
  "iat": 1622370878,
  // 등록된 클레임
  "exp": 1622372678,
  // 공개 클레임
  "https://shinsunyoung.com/jwt_claims/is_admin": true,
  // 비공개 클레임.
  "email": "ajufresh@gmail.com",
  // 비공개 클레임.
  "hello": "안녕하세요!"
}
```

<h3>1-2-1. 토큰 유효기간</h3>
<ul>
  <li>
    토큰이 노출되어 생길 수 있는 문제를 어떻게 다룰 것인가에 대해 다룬다.
  </li>
</ul>

<h4>1-2-1-1. 리프레시 토큰이 있다면?</h4>
<ul>
  <li>
    토큰의 유효기간이 너무 길면 하나의 토큰으로 너무 많은 작업을 할 수 있고 반면 너무 짧음녀 유저가 짧은 시간만 활용가능하여 불편하다.
  </li>
  <li>
    위의 문제를 해결하고자 나온 것이 <strong>리프레시 토큰</strong>이다. 리프레시 토큰은 액세스 토큰과는 <strong>별개의 토큰</strong>이다.
  </li>
    <ul>
      <li>
        사용자를 인증하기 위한 용도가 아니라 액세스 토큰이 만료 되었을 때 <strong>새로운 액세스 토큰을 발급</strong>하기 위해 사용한다.
      </li>
      <li>
        리프레시 토큰 유효기간을 길게하고 액세스 토큰 유효 기간을 짧게하여 보안의 안전성을 높일 수도 있다.
      </li>
    </ul>
  <li>
    클라이언트가 서버에 인증 요청
    <br>→ 서버는 클라이언트 요청을 기반으로 인증 정보가 유효한지 확인.
    <br>→ 액세스 토큰과 리프레시 토큰을 만들어 클라이언트에게 전달.
    <br>→ 클라이언트는 전달받은 토큰을 저장.
    <br>→ 서버에서 생성한 리프레시 토큰은 DB에도 저장.
    <br>→ 인증이 필요한 경우 클라이언트는 액세스 토큰과 함께 요청 전달.
    <br>→ 서버는 액세스 토큰이 유효한지 확인 후 유효한 경우 요청 처리.
    <br>→ 액세스 토큰이 만료된 요청 전달.
    <br>→ 서버는 토큰 만료 에러를 전달.
    <br>→ 클라이언트는 리프레시 토큰과 새로운 액세스 발급 요청을 전달.
    <br>→ 서버는 전달받은 리프레시 토큰이 유효한지 DB의 토큰과 비교 확인.
    <br>→ 유효한 리프레시 토큰인 경우 새로운 액세스 토큰을 전달.
  </li>
</ul>

<br><br>

<h1>2. JWT 서비스 구현하기</h1>
<ul>
  <li>
    의존성과 토큰 제공자를 추가하고 리프레시 토큰 도메인과 토큰 필터를 구현한다.
  </li>
</ul>

<br>

<h2>2-1. 의존성 추가하기</h2>
<ul>
  <li>
    "build.gradle"에 의존성을 추가한다. 
  </li>
</ul>

<br>

<h2>2-2. 토큰 제공자 추가하기</h2>
<ul>
  <li>
    jwt를 사용해 JWT를 생성하고 유효한 토큰인지 검증하는 역할을 하는 클레스를 추가한다.
  </li>
  <li>
    <strong>"application.yml"</strong> 파일에서 JWT 사용을 위해 <strong>이슈 발급자(issuer)</strong>와 <strong>비밀키(secret_key)</strong>를 필수로 설정한다.
  </li>
  <li>
    application.yml에 작성한 값들을 변수로 접근하는 데 사용할 JwtProperties 클래스를 만든다. ("config/jwt/JwtProperties.java")
  </li>
    <ul>
      <li>
        jwt.issuer와 secretKey의 값이 aplication.yml과 매핑된다.
      </li>
    </ul>
  <li>
    "config/jwt/TokenProvider.java"에 계속해서 토큰을 생성, 유효성 검사, 토큰에 필요한 정보를 가져오는 클래스를 작성한다.
  </li>
  <li>
    "test/java/me.shinsunyoung.springbootdeveloper.config.jwt/JwtFactory.java"를 생성하여 테스트 실행.
  </li>
  <li>
    "TokenProvider 클래스를 테스트하는 클래스를 생성한다. ("test/java/me.~~~/config/jwt/TokenProviderTest.java).
  </li>
</ul>

<br>

<h2>2-3. 리프레시 토큰 도메인 구현하기</h2>
<ul>
  <li>
    리프레시 토큰은 DB에 저장하는 정보이기 때문에 엔티티와 리포지터리를 추가해야 한다.
  </li>
  <li>
    "domain/RefreshToken.java"에 코드 작성.
  </li>
  <li>
    "repository/RefreshTokenRepository.java"에 리포지터리 파일 작성.
  </li>
</ul>

<br>

<h2>2-4. 토큰 필터 구현하기</h2>
<ul>
  <li>
    <strong>토큰 필터</strong>는 각종 요청을 처리하기 위한 <strong>로직으로 전달되기 전후</strong>에 URL 패턴에 맞는 <strong>모든 요청을 처리</strong>하는 기능을 제공한다.
  </li>
  <li>
    요청이 오면 <strong>헤더값을 비교</strong>하여 토큰이 있는지 확인하고 유효 토큰이라면 <strong>시큐리티 콘텍스트 홀더(security context holder)</strong>에 <strong>인증 정보</strong>를 저장한다.
  </li>
  <li>
    시큐리티 컨텍스트(security context)는 <strong>인증 객체가 저장</strong>되는 보관소이다.
  </li>
    <ul>
      <li>
        인증 객체가 필요할 때 언제든지 인증 객체를 사용할 수 있다.
      </li>
      <li>
        스레드마다 공간을 할당하는 <strong>스레드 로컬(thread local)</strong>에 저장되기에 코드 아무 곳에서나 참조가 가능하다.
      </li>
      <li>
        시큐리티 컨텍스트 객체를 저장하는 객체를 <strong>시큐리티 컨텍스트 홀더(security context holder)</strong>라 한다.
      </li>
    </ul>
  <li>
    "config/TokenAuthenticationFilter.java" 파일에 액세스 토큰값이 담긴 Authorization 헤더값을 가져와 액세스 토큰이 유효한 경우 인증 정보를 설정한다.
  </li>
</ul>

<br><br>

<h1>3. 토큰 API 구현하기</h1>
<ul>
  <li>
    리프레시 토큰을 검증하고, 유효한 리프레시 토큰인 경우 새로운 액세스 토큰을 생성하는 토큰 API를 구현한다.
  </li>
</ul>

<br>

<h2>3-1. 토큰 서비스 추가하기</h2>
<ul>
  <li>
    기능 구현을 위해 필요한 토큰 서비스 클래스와 관련 코드를 작성한다. ("service/UserService.java"에 findById() 메서드 추가).
  </li>
  <li>
    "service/RefreshTokenService.java"에 전달받은 리프레시 토큰으로 리프레시 토큰 객체를 검색하고 전달하는 findByRefreshToken() 메서드 구현.
  </li>
  <li>
    "service/TokenService.java" 파일에 전달받은 리프레시 토큰으로 <strong>토큰 유효성 검사</strong>를 진행하고 유효한 토큰일 때 <strong>리프레시 토큰으로 사용자 ID를 찾는 createNewAccessToken() 메서드</strong>와 사용자 ID로 사용자를 찾은 후 토큰 제공자의 <strong>새로운 액세스 토큰을 생성</strong>하는 <strong>generateToken() 메서드</strong>를 작성한다.
  </li>
</ul>

<br>

<h2>3-2. 컨트롤러 추가하기</h2>
<ul>
  <li>
    실제 토큰을 발급받는 API를 생성한다.
  </li>
  <li>
    "dto/CreateAccessTokenRequest"와 "dto/CreateAccessTokenResponse"를 작성해 토큰 생성 및 요청 응답을 담당할 DTO를 생성한다.
  </li>
  <li>
    실제로 요청을 받고 처리할 컨트롤러를 생성한다.
  </li>
  <li>
    "controller/TokenApiController.java" 파일을 생성하고 "/api/token POST" 요청을 처리한다.
  </li>
  <li>
    "test/.../controller/TokenApiControllerTest.java" 파일을 만들고 코드를 작성하며 이때까지의 내용을 정리한다.
  </li>
</ul>