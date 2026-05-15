<h1>1. 값 검증 가이드</h1>
<ul>
  <li>
    값 검증(validation)은 사용자가 요청을 보냈을 때 올바른 값인지 <strong>유효성을 검사</strong>하는 것이다.
  </li>
    <ul>
      <li>
        서버에서 비즈니스 로직을 수행하기 전에 올바른 데이터인지 검증하는 예가 있다.
      </li>
    </ul>
  <li>
    스프링의 <strong>자바 빈 벨리데이션(java bean validation) API</strong>를 사용하면 애너테이션 기반으로 다양한 검증 규칙을 간편하게 사용할 수 있다.
  </li>
  <li>
    값 검증은 <strong>계층에 상관없이</strong> 수행할 수 있다.
  </li>
    <ul>
      <li>
        컨트롤러에서 요청이 오는 순간, 퍼시스턴스 계층에서 엔티티에 적용하는 순간 모두 포함.
      </li>
      <li>
        보통은 <strong>프레젠테이션 계층</strong>에 검증 코드를 작성하여 <strong>불필요한 서비스 로직 수행을 방지</strong>한다. 
      </li>
    </ul>
  <li>
    <strong>Faker 오픈소스 라이브러리</strong>를 통해 검증할 데이터를 자동 생성할 수도 있다.
  </li>
    <ul>
      <li>
        의존성을 추가하고 "test/.../BlogApiControllerTest.java"에 테스트 작성.
      </li>
      <li>
        유효값 검증 로직을 "dto/AddArticleRequest.java"에 검증 애너테이션을 추가한다.
      </li>
      <li>
        "contorller/BlogApiController.java"에 유효값 검증 애너테이션을 추가하여 검증을 수행하도록 한다.
      </li>
    </ul>
</ul>

```java
// 자주 사용하는 자바 빈 벨리데이션 예.
// 1. 문자열.
@NotNull  // null을 허용하지 않음.
@NotEmpty // null, 빈 문자열(공백) 또는 공백만으로 채워진 문자열을 허용하지 않음.
@NotBlank // null, 빈 문자열(꽁백)을 허용하지 않음.
@Size(min=?, max=?) // 최소 길이, 최대 길이 제한.
@Null  // null만 가능.

// 2. 숫자.
@Positive  // 양수만 허용.
@PositiveOrZero  // 양수와 0만 허용.
@Negative  // 음수만 허용.
@NegativeOrZro  // 음수와 0만 허용.
@Min(?)  // 최솟값 제한.
@Max(?)  // 최댓값 제한.

// 3. 정규식 관련.
@Email  // 이메일 형식만 허용.
@Pattern(regexp="?")  // 직접 작성한 정규식에 맞는 문자열만 허용.
```