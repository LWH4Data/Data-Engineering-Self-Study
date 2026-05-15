<h1>1. 예외 처리 가이드</h1>
<ul>
  <li>
    스프링 부트는 기본으로 제공되는 오류 메시지에 <strong>ErrorAttributes>를 구현하여 빈으로 등록하면 구현한 ErrorAttributes에 맞게 에러 메시지를 만들 수 있다.
  </li>
  <li>
    <strong>에러 메시지용 객체</strong>를 만들어 사용하면 간편하게 어떤 키값이 있는지 보기 좋다.
  </li>
    <ul>
      <li>
        "config/error/ErrorCode.java"를 생성하고 에러 객체 코드 enum으로 작성한다. 
      </li>
      <li>
        에러 코드를 한 곳에 모아 관리하는 역할을 한다.
      </li>
    </ul>
  <li>
    "config/error/ErrorResponse.java"를 생성하고 코드를 입력한다.
  </li>
  <li>
    "config/error/exception/BusinessBaseException.java"를 생성하고 코드를 작성한다.
  </li>
    <ul>
      <li>
        비즈니스 로직을 작성하다 발생하는 예외를 모아둘 최상위 클래스이다.
      </li>
      <li>
        다른 비즈니스 에러들은 BusinessBaseException을 상속받아 구현한다.
      </li>
    </ul>
  <li>
    "config/error/excepton/NotFoundException.java"와 "config/error/excepton/ArticleNotFoundException.java"파일을 만들고 코드를 작성한다.
  </li>
  <li>
    "config/error/GlobalExceptionHandler.java"를 생성하고 코드를 작성한다.
  </li>
  <li>
    테스트를 위해 "test/.../BlogApiControllerTest.java" 파일에 코드를 작성한다.
  </li>
  <li>
    블로그 조회 로직의 예외도 테스트하기 위해 "test/.../BlogApiController.java"에 테스트 코드를 작성하고 현재 응답을 확인한다.
  </li>
  <li>
    IllegalArgumentException을 ExceptionHandler에 정의하여 예외처리 되도록 "service/BlogService" 코드를 수정한다.
  </li>
</ul>