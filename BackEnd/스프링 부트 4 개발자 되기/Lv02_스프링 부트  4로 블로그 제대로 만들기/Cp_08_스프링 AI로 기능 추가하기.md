<h1>1. 사전 지식:AI</h1>
<h2>1-1. LLM이란?</h2>
<ul>
  <li>
    최근에는 LLM을 챗봇, 요약, 번역, 코드 생성 등의 기능에 도입하여 동적인 서비스를 제공할 수 있다.
  </li>
</ul>

<br>

<h2>1-2. 스프링 AI란?</h2>
<ul>
  <li>
    LLM을 서비스에 추가하기 위해서는 AI 연동 코드가 더 복잡해지는 상황(LLM API HTTP 요청, 인증 헤더 추가, 요청 바디에 프롬프트 추가, 응답 JSON 파싱, 임베딩 등...)이 발생한다.
  </li>
  <li>
    스프링 AI는 LLM을 스프링 자체의 문법으로 도입할 수 있게 하여 발생하는 오버헤드를 최소화한다.
  </li>
  <li>
    즉, LLM을 <strong>스프링 생태계 안에서 사용</strong>할 수 있도록 추상화해 주는 도구이다.
  </li>
    <ul>
      <li>
        이를 통해 개발자는 비즈니스 로직에 더 집중할 수 있다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 오픈AI 토큰 발급받기</h1>
<ul>
  <li>
    아쉽게도 OpenAi는 무료 API를 제공하지 않는다. 도서를 따라가며 5$만 충전.
  </li>
  <li>
    .env 설정 할 것!!!
  </li>
</ul>

<br><br>

<h1>3. 블로그 글 작성 도우미 기능 추가하기</h1>
<h2>3-1. 의존성 추가하기</h2>
<ul>
  <li>
    도서 작성일 기준으로 공식적으로 스프링 AI 2 버전이 릴리즈되어 있지 않아 마일스톤 버전을 사용한다.
  </li>
</ul>

<br>

<h2>3-2. 글 작성 도우미 기능 추가하기</h2>
<ul>
  <li>
    "/dto/WritingSuggestionRequest.java"와 "/dto/WritingSuggestionResponse.java"파일을 생성.
  </li>
  <li>
    이번에는 <strong>record</strong>를 사용한다. record는 <strong>DTO와 같이 단순히 데이터를 전달하기 위한 객체</strong>를 정의할 때 유용하게 사용할 수 있다.
  </li>
  <li>
    기능 구현을 위한 <strong>프롬프트</strong>를 "resources/prompts/writing-assistant.st"로 작성한다.
  </li>
  <li>
    작성한 DTO와 프롬프트를 활용한 <strong>기능을 구현</strong>하기 위해 "service/WritingAssistantService.java"를 생성한다.
  </li>
</ul>

<h3>3-2-1. getWritingAssist() 메서드</h3>
<ul>
  <li>
    사용자가 입력한 제목, 본문, 질문을 프롬프트 템플릿에 주입
    <br>→ 최종 프롬프트 생성
    <br>→ ChatClient를 통해 LLM 호출
    <br>→ 호델이 반환한 JSON 형식의 응답을 Writing Suggestions 객체로 반환.
    <br>→ 반환된 Writing Suggestions 객체에서 글쓰기 제안 목록만 추출하여 최종 결과로 반환.
  </li>
  <li>
    "/conroller/BlogApiController.java"에 "/api/ai-suggestions POST" 요청이 들어오면 AI를 통해 목록을 받아오는 getWritingAssist() 메소드 작성.
  </li>
</ul>

<br>

<h2>3-3. 실행 테스트하기</h2>
<ul>
  <li>
    HTTP 메소드에서 [POST]로 http://localhost:8080/api/ai-suggestions"로 body를 넣어 요청을 보낸다.
  </li>
</ul>

<br>

<h2>3-4. 글 생성 뷰 수정하기</h2>
<ul>
  <li>
    글 생성 뷰에 [AI 도움 받기] 버튼을 추가한다. ("resource/templates/newArticle.html")
  </li>
  <li>
    "static/js/article.js" 파일에 [AI 도움받기] 버튼을 누르면 입력칸에 있는 데이터를 가져와 API를 호출해 AI 제안을 받는 Js 코드 추가.
  </li>
</ul>

<br>

<h2>3-5. 실행 테스트하기</h2>
<ul>
  <li>
    "http://localhost:8080/new-article"에 접속하여 제목과 내용을 입력하고 [AI 도움받기] 버튼 클릭.
  </li>
</ul>

<br><br>

<h1>4. 섬네일 자동 생성 기능 추가하기</h1>
<h2>4-1. 이미지 업로드 기능 추가하기</h2>
<ul>
  <li>
    "domain/Article.java"에 이미지 경로를 저장할 컬럼을 추가한다.
  </li>
  <li>
    "dto/AddArticleRequest.java", "dto/UpdateArticleRequest.java", "dto/ArticleResponse.java", "dto/ArticleViewResponse.java", "dto/ArticleListViewResponse.java" 파일에 이미지 경로 파일 추가.
  </li>
  <li>
    테스트를 위해 import.sql에도 이미지 컬럼을 생성 추가.
  </li>
  <li>
    "service/BlogService.java" 파일의 블로그 업데이트 메소드에 이미지 경로를 넘겨준다.
  </li>
  <li>
    엔티티 변경을 완료하였기에 업로드 로직을 작성한다. ("dto/UploadResponse.java").
  </li>
  <li>
    "service/FileStorageService.java" 인터페이스 추가.
  </li>
    <ul>
      <li>
        다른 코드는 class 이지만, 해당 영역을 interface로 작업하는 이유는 <strong>의존성 역전 원칙(DIP)</strong>을 적용하기 위해서이다.
      </li>
        <ul>
          <li>
            의존성 역전 원칙이란 <strong>상위 계층</strong>이 구체적인 구현이 아니라 <strong>추상화</strong>에 의존하도록 설계하는 원칙이다.
          </li>
          <li>
            추상화에 의존하도록 하여 시스템의 결합도를 낮추고 변경에 유연하게 대응할 수 있다.
          </li>
        </ul>
      <li>
        만약 클래스를 사용할 경우 AWS S3(Simple Stroage Service), Azure Storage 등을 사용한다면 저장 방식이 바뀔 때 마다 모두 수정이 필요하다. 반면 인터페이스는 필요한 곳만 수정하면 된다. 
      </li>
      <li>
        각각의 경우를 구현하고 매번 수정하는 것은 객체지향과 맞지 않다.
      </li>
    </ul>
  <li>
    FileStorageService 인터페이스를 구현할 클래스를 생성한다. ("service/LocalStorageService.java").
  </li>
</ul>

<h3>4-1-1. store() 메서드</h3>
<ul>
  <li>
    업로드 디렉터리가 존재하지 않을 경우 디렉터리 생성.
  </li>
    <ul>
      <li>
        컨트롤러로부터 전달받은 파일과 원본 파일명 UUID를 이용해 고유한 파일명을 생성한다.
      </li>
      <li>
        파일 스트림을 로컬 파일 시스템에 복사하여 저장한다.
      </li>
    </ul>
  <li>
    "controller/UploadController.java"를 생성하고 "/api/upload POST" 요청이 오면 파일을 업로드하는 uploadFile() 메소드 작성.
  </li>
</ul>

<br>

<h2>4-2. 실행 테스트하기</h2>
<ul>
  <li>
    HTTP 메서드를 [POST]로 설정하고 "http://localhost:8080/api/upload"로 요청을 보낸다.
  </li>
</ul>

<br>

<h2>4-3. 글 생성 뷰 수정하기</h2>
<ul>
  <li>
    글 생성 뷰에 이미지 업로드 기능을 추가한다. ("resource/templates/newArticle.html").
  </li>
  <li>
    "static/js/article.js" 파일에 이미지 업로드와 관련된 Js 코드를 추가한다.
  </li>
  <li>
    article.js의 생성 기능에서 이미지 URL도 넘기도록 수정.
  </li>
  <li>
    "resources/templates/article.html" 파일을 이미지를 표시하도록 코드 추가.
  </li>
  <li>
    "resources/templates/articleList.html" 파일에서 글 리스트도 이미지를 표시하도록 코드를 추가.
  </li>
  <li>
    스프링 부트는 기본적으로 classpath:/static, classpath:/public과 같은 <strong>정적 리소스 디렉터리</strong>만 <strong>자동으로 서빙</strong>한다.
  </li>
    <ul>
      <li>
        이미지 업로드에 사용되는 "uploads/"와 같이 <strong>런타임에 생성되는 로컬 파일 시스템 경로</strong>는 접근이 불가하기에 config 설정이 필요하다.
      </li>
        <ul>
          <li>
            실습은 서버에 데이터를 저장해서 문제가 되지만 S3 등을 사용하면 해당하지 않는다.
          </li>
          <li>
            "main/java/me/shinsunyoung/springbootdeveloper/config/WebMvcConfig"를 생성하고 설정을 작성한다.
          </li>
        </ul>
    </ul>
</ul>

<br>

<h2>4-4. 실행 테스트하기</h2>
<ul>
  <li>
    "http://localhost:8080/new-article"에 접속하여 제목과 내용을 채우고 이미지 업로드 버튼을 눌러 이미지를 추가한다.
  </li>
</ul>

<br>

<h2>4-5. 섬네일 자동 생성 기능 추가하기</h2>
<ul>
  <li>
    "dto/GeneratorThumbnailRequest.java"와 "dto/GeneratorThumbnailResponse.java" 레코드 생성.
  </li>
    <ul>
      <li>
        AI가 섬네일을 생성할 때 참고할 내용을 담을 <strong>요청, 응답에 사용할 레코드</strong>이다.
      </li>
    </ul>
  <li>
    필요한 프롬프트를 작성하기 위해 "resources/prompts/thumbnail-generator.st" 파일을 생성한다.
  </li>
  <li>
    생성된 dto와 프롬프트를사용해 비즈니스 로직을 "service/ThumbnailGeneratorService.java"에 작성한다.
  </li>
</ul>

<h3>4-4-1. generateThumbnail() 메서드</h3>
<ul>
  <li>
    "controller/BlogApiController.java"에 "/api/ai-thumbnails POST" 여청이 오면 AI를 활용해 섬네일을 생성하는 thumbnailGenerator() 메서드를 작성한다.
  </li>
</ul>