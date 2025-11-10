<h1>1. FastAPI 소개</h1>
<ul>
  <li>
    FastAPI의 장점
  </li>
    <ul>
      <li>
        <strong>성능</strong>: 특정한 경우에서 Node.js와 Go에 견줄만 하다.
      </li>
      <li>
        <strong>빠른 개발</strong>: 이해하기 어렴거나 이상한 부분이 없다.
      </li>
      <li>
        <strong>향상된 코드 품질</strong>: 타입 힌트와 Pydantic 모델은 버그를 줄이는 데 유용하다.
      </li>
      <li>
        <strong>자동 생성된 문서 및 테스트 페이지</strong>: OpenAPI 설명을 직접 편집하는 것보다 쉽다.
      </li>
    </ul>
  <li>
    FastAPI가 주로 사용하는 기능
  </li>
    <ul>
      <li>
        파이썬 <strong>타입 힌트</strong>
      </li>
      <li>
        <strong>비동기 지원</strong>을 포함한 웹 머신용 Starlette
      </li>
      <li>
        데이터 정의 및 유효성 검사를 위한 <strong>Pydantic</strong>
      </li>
      <li>
        다른 기능을 활용하고 확장할 수 있는 특별한 <strong>통합 기능</strong>
      </li>
    </ul>
</ul>

<br><br>

<h1>2. FastAPI 애플리케이션</h1>
<ul>
  <li>
    <strong>docker 컨테이너</strong>로 작업할 것이기에 포함된 실습 폴더 참고
  </li>
  <li>
    많은 테스트 방법을 알려주는데 Spring boot에서 사용하던 방식으로 <strong>python으로 .py 스크립트를 실행</strong>하고 <strong>localhost로 확인</strong>하는 방법으로 실습을 진행할 것임.
  </li>
  <li>
    다른 확인 방법으로는 Requests, HTTPX, uvicorn 명령어 등으로 실행이 가능하다.
  </li>
</ul>

```python
# FastAPI 라이브러리에서 FastAPI 클래스를 가져옴
# → 이 클래스를 사용해서 웹 애플리케이션 인스턴스를 생성함
from fastapi import FastAPI

# app은 전체 웹 앱을 나타내는 최상위 FastAPI 객체이다.
app = FastAPI()

# 경로 데코레이터로 FastAPI에 다음 사항들을 알려준다.
#   - URL "/hi"에 대한 요청은 다음 함수로 전달돼야 한다.
#   - 데코레이터는 HTTP GET 동사에만 적용된다. 다른 동사(PUT, POST 등)도 가능.
@app.get("/hi")
# 경로 함수로 HTTP 요청과 응답의 주요 접점이다. 인수를 포함할 수 있다.
def greet():
    return "Hello? World"

# 현재 스크립트가 직접 실행될 때만 아래 코드 실행
# (다른 모듈에서 import될 때는 실행되지 않음)
if __name__ == "__main__":
    import uvicorn  # ASGI 서버(Uvicorn)를 임포트

    # Uvicorn으로 FastAPI 앱 실행
    # "hello:app" → hello.py 파일 안의 app 객체를 의미
    # host="0.0.0.0" → 외부 접속 허용 (Docker나 클라우드에서 필수)
    # port=8000 → 8000번
```

<br><br>

<h1>3. HTTP 요청</h1>

<table border="1" cellspacing="0" cellpadding="10" style="border-collapse: collapse; width: 100%; text-align: center; background-color: #2e2e2e; color: #f2f2f2; font-family: sans-serif;">
  <thead style="background-color: #394b61;">
    <tr>
      <th>종류</th>
      <th>이름</th>
      <th>위치</th>
      <th>예시</th>
      <th>사용 목적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1️⃣</td>
      <td><strong>Path Parameter<br>(경로 매개변수)</strong></td>
      <td>URL 경로</td>
      <td><code style="color:#ffd369;">/users/10</code></td>
      <td>🎯 특정 리소스 지정<br>(어떤 유저/아이템인지)</td>
    </tr>
    <tr>
      <td>2️⃣</td>
      <td><strong>Query Parameter<br>(쿼리 매개변수)</strong></td>
      <td><code>?</code> 뒤</td>
      <td><code style="color:#ffd369;">/users?active=true&amp;page=2</code></td>
      <td>🔎 옵션/필터/검색 조건 전달</td>
    </tr>
    <tr>
      <td>3️⃣</td>
      <td><strong>Header<br>(요청 헤더)</strong></td>
      <td>HTTP 헤더</td>
      <td>
        <code style="color:#ffd369;">Authorization: Bearer token</code><br>
        <code style="color:#ffd369;">User-Agent: Chrome</code>
      </td>
      <td>🛡️ 인증 정보·환경 정보 전달<br>(토큰/브라우저 등)</td>
    </tr>
    <tr>
      <td>4️⃣</td>
      <td><strong>Body<br>(요청 본문)</strong></td>
      <td>HTTP 메시지 내부</td>
      <td><code style="color:#ffd369;">{ "id": "abc", "pw": "1234" }</code></td>
      <td>📦 실제 데이터 전달<br>(로그인, 회원가입, JSON)</td>
    </tr>
  </tbody>
</table>

<ul>
  <li>
    HTTP 요청은 Swagger 웹 UI 혹은 Postman으로 보다 쉽게 확인할 수 있다.
  </li>
  <li>
    FastAPI는 Swagger를 내장하고 있고 도서에서는 <strong>HTTPie</strong>를 활용해서 <strong>CLI로 Swagger를 확인하는 방법</strong>을 사용한다.
  </li>
  <li>
    HTTP 요청에서 데이터가 전달되는 네 가지 위치는 다음과 같다.
  </li>
</ul>

```bash
# 1. HTTPie 
#   - URL을 입력해 확인을 한다.
http localhost:8000/hi

# === 결과 ===
# a) 요청
#   - 동사(GET) 및 경로(/hi)
#   - 모든 쿼리 매개변수 (? 뒤의 텍스트, 현재 요청에는 없다).
#   - 기타 HTTP 헤더
#   - 요청 본문 콘텐츠 없음

# b) FastAPI 해석
#   - Header: HTTP 헤더
#   - Path: URL
#   - Query: 쿼리 매개변수(URL 끝의 ? 뒤)
#   - Body: HTTP 본문

# URL(경로 + 쿼리)
GET /hi HTTP/1.1
# Header
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/3.2.4
# Body는 현재 없음.

# 결과
HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Sun, 09 Nov 2025 14:59:13 GMT
server: uvicorn

"Hello? World?"
```

<br><br>

<h2>3-1. URL 경로</h2>

```python
# 1. 매개변수 추가.
from fastapi import FastAPI

app = FastAPI()

# RUL에 {who}를 추가하여 who라는 변수를 예상하도록 FastAPI에 지시
@app.get("/hi/{who}")

# greet 함수에 who 인수를 할당.
def greet(who):
    return f"Hello? {who}?"
```

```bash
# 2. .py 재실행
python hello.py

# 결과 확인
http localhost:8000/hi/Mom

# === 결과 ===
HTTP/1.1 200 OK
content-length: 15
content-type: application/json
date: Sun, 09 Nov 2025 14:59:13 GMT
server: uvicorn

"Hello? World?"
```

<br>

<h2>3-2. 쿼리 매개변수</h2>
<ul>
  <li>
    <strong>쿼리 매개변수(query parameter)</strong>는 URL에서 <strong>?</strong> 뒤에 오는 <strong>이름=값</strong> 형태의 문자열로 <strong>&로 구분</strong>된다.
  </li>
</ul>

```python
# 1. 쿼리 매개변수로 코드 수정
from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")

# 데코레이터의 URL에 {who}가 없기에 who가 쿼리 매개변수라 가정한다.
#   - 즉, 쿼리 매개변수에 '값'을 주어야 한다.
def greet(who):
    return f"Hello? {who}?"
```

```bash
# 2. 수정된 코드 재실행
python hello.py

# 2-1) 결과 확인
# - ? 방식
http -b localhost:8000/hi?who=Mom
# - 공백 방식
http -b localhost:8000/hi who == Mom

# === 결과 ===
"Hello? Mom?"
```

<br>

<h2>3-3. 본문</h2>
<ul>
  <li>
    <strong>GET 엔드포인트</strong>에 경로 또는 쿼리 매개변수를 제공할 수 있지만 <strong>요청 본문(request body)의 값은 제공할 수 없다</strong>.
  </li>
  <li>
    HTTP에서 GET은 <strong>멱등성(idempotent)</strong>을 지녀야 한다. 즉, <strong>같은 질문을 하면 같은 답</strong>을 얻어야 한다.
  </li>
  <li>
    요청 본문은 생성(POST)하거나 업데이트(PUT 혹은 PATCH)할 때 <strong>서버로 정보를 전송</strong> 하는 데 사용된다. (9장에서 다른 요청에 대해 알아본다).
  </li>
</ul>

```python
# 1. GET 효청을 POST로 변경
from fastapi import FastAPI, Body

app = FastAPI()

# POST로 변경
@app.post("/hi")

# Body(embed=True)
#   - JSON 요청 형식에서 who의 값을 가져온다는 것을 FastAPI에 알린다.
#   - embed 부분은 단순히 "Mom"이 아니라 {"who": "Mom"} 처럼 보이도록 한다.
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"
```

```bash
# 2. 결과 반환.
http -v localhost:8000/hi who=Mom

# === 결과 ===
POST /hi HTTP/1.1
Accept: application/json, */*;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 14
Content-Type: application/json
Host: localhost:8000
User-Agent: HTTPie/3.2.4

{
    "who": "Mom"
}


HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Mon, 10 Nov 2025 05:16:44 GMT
server: uvicorn

"Hello? Mom?"
```

<br>

<h2>3-4. HTTP 헤더</h2>

```python
# 1. greeting 인자를 HTTP 헤더로 전달.
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hi")
def greet(who: str = Header()):
    return f"Hello? {who}?"
```

```bash
# 2. 결과 확인
http -v localhost:8000/hi who:Mom

# === 결과 ===
GET /hi HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/3.2.4
who: Mom

HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Mon, 10 Nov 2025 05:37:22 GMT
server: uvicorn

"Hello? Mom?"
```

```python
# 3. User-Agent 헤더를 반환.
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hi")
def greet(who: str = Header()):
    # 요청 보낸 쪽(클라이언트)이 보낸 헤더 값 "who"를 받음
    return f"Hello? {who}?"

@app.get("/agent")
def get_agent(user_agent: str = Header()):
    # 브라우저나 앱이 자동으로 넣는 "User-Agent" 헤더를 받음
    return user_agent
```

```bash
# 4. 결과 확인
http -v localhost:8000/agent

# === 결과 ===
GET /agent HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/3.2.4

HTTP/1.1 200 OK
content-length: 14
content-type: application/json
date: Mon, 10 Nov 2025 05:52:50 GMT
server: uvicorn

"HTTPie/3.2.4"
```

<br>

<h2>3-5. 다중 요청 데이터</h2>
<ul>
  <li>
    동일한 경로 함수에서 앞서 설명한 메서드를 <strong>두 개 이상</strong> 사용할 수 있다.
  </li>
    <ul>
      <li>
        즉, URL, 쿼리 매개변수, HTTP 본문, HTTP 헤더, 쿠기 등의 데이터를 가져올 수 있다.
      </li>
    </ul>
  <li>
    또한 데이터를 처리하는 의존성 함수를 직접 작성할 수 있다.
  </li>
  <li>
    페이지네이션(pagenation)이나 인증 같은 특별한 방법으로 결합하는 것은 3부에서 소개한다.
  </li>
</ul>

<br>

<h2>3.6 요청 권장 사항</h2>
<ul>
  <li>
    URL에 인수를 전달할 때에는 <strong>RESTful 가이드라인</strong>을 따르는 것이 표준 관행이다.
  </li>
  <li>
    <strong>쿼리 문자열</strong>은 대개 페이지네이션 같은 <strong>선택적 인수</strong>를 제공하는 데 사용한다.
  </li>
  <li>
    <strong>본문</strong>은 대개 전체 모델이나 부분 모델과 같이 <strong>더 큰 입력</strong>에 사용한다.
  </li>
</ul>

<br><br>

<h1>HTTP 응답</h1>
<ul>
  <li>
    기본적으로 FastAPI는 엔드포인트 함수에서 반환하는 모든 것을 <strong>JSON으로 변환</strong>한다.
  </li>
  <li>
    HTTP 응답(response)의 헤더 행은 <strong>Content-type: application/json</strong>이다.
  </li>
    <ul>
      <li>
        즉, greet() 함수가 "Hello? World?"라는 문자열을 반환해도 FastAPI는 이를 JSON으로 변환한다.
      </li>
    </ul>
</ul>

<br>

<h2>4-1. 상태 코드</h2>
<ul>
  <li>
    기본적으로 FastAPI는 <strong>200 상태 코드</strong>를 반환하며 <strong>예외의 경우에는 4xx 코드</strong>를 반환한다.
  </li>
</ul>

```python
# 1. HTTP 200 상태 코드 추가.
@app.get("/happy")
def happy(status_code=200):
    return ":)"
```

```bash
# 2. 결과 확인
http localhost:8000/happy

# === 결과 ===
HTTP/1.1 200 OK
content-length: 4
content-type: application/json
date: Mon, 10 Nov 2025 07:17:03 GMT
server: uvicorn

":)"
```

<br>

<h2>4-2. 헤더</h2>

```python
# 1. 응답 헤더 삽입.
from fastapi import Response

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"
```

```bash
# 2. 결과 확인
http localhost:8000/header/marco/polo

# === 결과 ===
HTTP/1.1 200 OK
content-length: 13
content-type: application/json
date: Mon, 10 Nov 2025 07:24:26 GMT
marco: polo
server: uvicorn

"normal body"
```

<br>

<h2>4-3. 응답 유형</h2>
<ul>
  <li>
    fastapi.responses에서 관련 클래스를 가져오는 응답 유형은 다음과 같다.
  </li>
    <ul>
      <li>
        JSONResponse (기본값)
      </li>
      <li>
        HTMLResponse
      </li>
      <li>
        PlainTextResponse
      </li>
      <li>
        RedirectResponse
      </li>
      <li>
        FileResponse
      </li>
      <li>
        StreamingResponse
      </li>
    </ul>
  <li>
    다른 출력 형식의 경우 response 클래스에는 일반적으로 다음이 필요하다.
  </li>
    <ul>
      <li>
        <strong>content</strong>: 콘텐츠, 문자열 또는 바이트
      </li>
      <li>
        <strong>media_type</strong>: 미디어 유형, 문자열 형태의 MIME 유형 값
      </li>
      <li>
        <strong>status_code</strong>: 상태 코드, HTTP 정수 상태 코드
      </li>
      <li>
        <strong>headers</strong>: 헤더, 문자열로 구성된 dict
      </li>
    </ul>
</ul>

<br>

<h2>4-4. 타입 변환</h2>
<ul>
  <li>
    경로 함수는 무엇이든 반환이 가능하며 기본적인 JSONResponse를 사용하는 FastAPI는 <strong>JSON 문자열</strong>로 변환해 일치하는 <strong>HTTP 응답 헤더 Content-Length</strong> 및 <strong>Content-Type</strong>과 함께 반환한다.
  </li>
  <li>
    FastAPI는 <strong>jsonable_encoder() 내부 함수</strong>를 통해 모든 데이터 구조를 <strong>JSON과 비슷한 파이썬 데이터 구조</strong>로 변환한 다음 <strong>json.dumps()</strong>를 호출해 <strong>JSON 문자열</strong>로 변환한다.
  </li>
</ul>

```python
# 1. jsonable_encoder()를 사용해 JSON 폭발 방지
import datetime
import pytest
from fastapi.encoders import jsonable_encoder
import json

@pytest.fixture
def data():
    return datetime.datetime.now()

def test_json_dump(data):
    with pytest.raises(Exception):
        _ = json.dumps(data)

def test_encoder(data):
    out = jsonable_encoder(data)
    assert out
    json_out = json.dumps(out)
    assert json_out
```

<br>

<h2>4-5. 모델 타입과 response_model</h2>
<ul>
  <li>
    <strong>속성이 동일한 클래스가 여러 개</strong> 있을 수 있다. 이때 하나는 <strong>사용자 입력용</strong>, 하나는 <strong>출력용</strong>, 다른 하나는 <strong>내부용</strong>으로 지정할 수 있다.
  </li>
  <li>
    위처럼 나누는 경우는 <strong>민감한 정보를 출력에서 제거</strong>하거나 <strong>사용자 입력에 속성을 추가</strong>하는 경우가 있다.
  </li>
  <li>
    FastAPI는 반환한 객체에는 있지만 <strong>response_model로 지정한 객체에 없는 속성을 모두 제거</strong>한다.
  </li>
</ul>

```python
# 1. 세 가지 클래스를 활용한 실습 (model/tag.py)
#   - TagIn: 사용자가 제공해야 하는 정보
#   - Tag: TagIn에 created(Tag가 생성된 시점)와 secret(DB에 저장되지만 외부 노출 X)
#     두 개의 필드 추가.
#   - TagOut: 조회 또는 검색 엔드퐁니트에서 사용자에게 반환할 수 있는 항목 정의. 기존 
#     TagIn 객체와 Tag 객체가 지닌 tag 속성과 Tag 객체가 지닌 created 속성을 갖는다.
from datetime import datetime
from pydantic import BaseModel

class TagIn(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

class TagOut(BaseModel):
    tag: str
    created: datetime
```

```python
# 2. 웹 모듈에 무언가를 제공하는 모듈 (service/tag.py)
from datetime import datetime
from model.tag import Tag

def create(tag: Tag) -> Tag:
    """태그를 생성한다."""
    return tag

def get(tag_str: str) -> Tag:
    """태그를 반환한다."""
    return Tag(tag=tag_str, created=datetime.utcnow(), secret="")
```

```python
# 3. 앞서 작성한 코드를 사용하는 웹 모듈 web/tag.py를 작성한다.
#   - 중요한 것은 get_one() 경로 함수와 경로 코레이터의 response_model=TagOut이다.
#   - 해당 함수는 자동으로 내부 Tag 객체를 필터링한 TagOut 객체로 변경한다.
from datetime import datetime
from model.tag import TagIn, Tag, TagOut
import service.tag as service
from fastapi import FastAPI

app = FastAPI()

@app.post('/')
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.utcnow(),
        secret="shhhh")
    service.create(tag)
    return tag_id

@app.get('/{tag_str}', response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web.tag:app", host="0.0.0.0", port=8000, reload=True)
```

```bash
# 2. 결과 확인
http -b localhost:8000/GoodTag

# === 결과 ===
{
    "created": "2025-11-10T08:34:07.918369",
    "tag": "GoodTag"
}
```

<br><br>

<h1>5. 자동 문서화</h1>
<ul>
  <li>
    <strong>localhost:8000/docs</strong>에 접근하면 swagger 웹 처럼 테스트를 수행할 수 있다.
  </li>
    <ul>
      <li>
        FastAPI는 코드로 OpenAPI 사양을 생성하며, <strong>모든 엔드포인트를 표시하고 테스트하는 페이지</strong>를 첨부한다.
      </li>
    </ul>
</ul>

<br>

<h2>5-1. 복잡한 데이터</h2>
<ul>
  <li>
    GET 또는 DELETE 엔드포인트는 인자가 필요 없거나 문자열이나 숫자 같은 간단한 인자만 몇 개 필요할 수 있다.
  </li>
  <li>
    그러나 리소스를 생성하는 POST이나 수정하는 PUT 혹은 PATCH는 대개 더 복잡한 데이터 구조가 필요하다.
  </li>
</ul>