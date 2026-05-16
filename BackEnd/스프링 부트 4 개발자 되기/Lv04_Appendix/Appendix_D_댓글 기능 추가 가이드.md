<h1>1. 댓글 기능 추가 가이드</h1>
<ul>
  <li>
    DB의 조인과 외래키를 활용해 댓글 기능을 추가한다.
  </li>
    <ul>
      <li>
        article_id를 외래키로 하는 comment 테이블을 생성하고 여기에 댓글을 저장한다.
      </li>
      <li>
        게시글과 comment는 1:N 관계로 연결연결된다.
      </li>
    </ul>
  <li>
    "domain/Comment.java"를 생성하고 코드를 작성한다. (ManyToOne).
  </li>
  <li>
    "domain/Article.java"에 Comment를 위한 코드를 추가한다. (OneToMany).
  </li>
  <li>
    "repository/CommentRepository.java" 파일에 코드를 작성한다.
  </li>
  <li>
    테이블 구조가 변경되었기에 "resource/import.sql"도 수정한다.
  </li>
  <li>
    "dto/AddCommentRequest.java"와 "dto/AddCommentResponse.java"를 생성하고 코드를 작성한다.
  </li>
  <li>
    "service/BlogService.java" 파일에 댓글을 추가하는 코드를 추가한다.
  </li>
  <li>
    "/api/comments POST" 요청이 오면 글을 추가하기 위한 addComment() 메서드를 작성한다. ("controller/BlogApiController.java")/
  </li>
  <li>
    "test/.../BlogApiController.java"에 테스트 코드를 작성한다.
  </li>
  <li>
    "dto/ArticleViewResponse.java" 파일에 comments 필드를 추가한다.
  </li>
  <li>
    "templates/article.html"에 댓글 추가를 위한 뷰 코드를 작성한다.
  </li>
  <li>
    "resource/static/js/article.js"에 코드 추가.
  </li>
</ul>
