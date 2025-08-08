<h1>1. 소개</h1>
<ul>
  <li>
    Nginx 설치에 대해 다루는데 Docker container로 사용한다.
  </li>
</ul>

```bash
# 1. Nginx 이미지 가져오기
docker pull nginx

# 2. 가져온 이미지로 컨테이너 실행
docker run --name nginx -d nginx
```

<h1>2. 주요 설정 파이, 디렉터리, 명령어</h1>
<ul>
  <li>
    Nginx의 주요 디렉터리 구조와 명령어에 대해 배운다.
  </li>
  <li>
    현재는 Docker를 사용하고 있기에 컨테이너 내부에 디렉터리 구조가 존재한다.
  </li>
</ul>

```bash
# 1. Nginx 컨테이너 내부 접근
docker exec -it nginx bash

# 2. 디렉터리 확인
```

<br>

<h2>1-1. 엔진엑스 주요 설정 파일과 디렉터리</h2>
<h3>1-1-1. /etc/nginx</h3>
<ul>
  <li>
    Nginx 서버가 사용하는 기본 설정이 지정된 <strong>루트 디렉터리</strong>.
  </li>
</ul>

<h3>1-1-2. /etc/nginx/nginx.conf</h3>
<ul>
  <li>
    Nginx의 기본 설정 파일. 모든 설정에 대한 진입점. 
  </li>
    <ul>
      <li>
        워커 프로세스 개수, 튜닝, 동적 모듈 적재 등 <strong>글로벌 설정 항목</strong>.
      </li>
      <li>
        다른 Nginx 세부 설정 파일에 대한 <strong>참조</strong>.
      </li>
      <li>
        모든 설정 파일을 포함하는 <strong>최상위 http</strong>.
      </li>
    </ul>
</ul>

<h3>1-1-3. /etc/nginx/conf.d/</h3>
<ul>
  <li>
    기본 HTTP 서버 설정 파일 포함.
  </li>
  <li>
    디렉터리 내 .conf로 끝나는 파일은 앞서 다룬 /etc/nginx/ningx.conf 파일이 가진 <strong>최상위 http 블록에 포함</strong>된다.
  </li>
    <ul>
      <li>
        Nginx 설정은 <strong>include 구문</strong>을 활용해 각 설정 파일을 간결하게 구조화할 수 있다.
      </li>
    </ul>
  <li>
    배포되는 Nginx 중에 가끔 conf.d 디렉터리 대신 site-enabled 디렉터리가 있는 경우가 있는데 이제는 사용하지 않는다.
  </li>
</ul>

<h3>1-1-4. /var/log/nginx</h3>
<ul>
  <li>
    Nginx의 <strong>로그</strong>가 저장되는 디렉터리.
  </li>
  <li>
    access.log와 error.log가 있다.
  </li>
    <ul>
      <li>
        <strong>access.log</strong>: Nginx가 수신한 <strong>개별 요청</strong>에 대한 로그.
      </li>
      <li>
        <strong>error.log</strong>: <strong>오류</strong> 발생 시 이벤트 내용에 대한 로그. (+ debug 정보).
      </li>
    </ul>
</ul>

<br>

<h2>1-2. 엔진엑스 명령어</h2>
<h3>1-2-1. nginx -h</h3>
<ul>
  <li>
    Nginx 도움말
  </li>
</ul>

<h3>1-2-2. nginx -v</h3>
<ul>
  <li>
    Nginx 버전 정보 확인
  </li>
</ul>

<h3>1-2-3. nginx -V</h3>
<ul>
  <li>
    Nginx의 버전 정보 + 빌드 정보 + 바이너리에 포함된 모듈
  </li>
</ul>

<h3>1-2-4. ningx -t</h3>
<ul>
  <li>
    Nginx 설정을 시험
  </li>
</ul>

<h3>1-2-5. nginx -T</h3>
<ul>
  <li>
    Nginx 설정 시험 + 결과 화면 출력. (기술 지원 시 필요).
  </li>
</ul>

<h3>1-2-6. nginx -s signal</h3>
<ul>
  <li>
    <strong>-s</strong>: 지정된 신호(stop, quit, reload, reopen)를 Nginx 마스터 프로세스에 전송한다.
  </li>
    <ul>
      <li>
        <strong>stop</strong>: Nginx 프로세스 즉시 동작 중지
      </li>
      <li>
        <strong>quit</strong>: 현재 진행 중인 요청을 모두 처리한 뒤 Nginx 프로세스 종료.
      </li>
      <li>
        <strong>reload</strong>: Nginx가 설정을 다시 읽어들이게 한다. (변경된 설정도 reload로 적용한다).
      </li>
      <li>
        <strong>reopen</strong>: Nginx가 지정된 로그 파일을 다시 열도록 명령한다.
      </li>
    </ul>
</ul>

<br>

<h1>2. include 구문을 사용해 깔끔한 설정 만들기</h1>
<ul>
  <li>
    부피가 큰 설정 파일을 <strong>모듈화된 설정</strong>으로 <strong>논리적인 그룹</strong>을 만들어 정리.
  </li>
  <li>
    <strong>include</strong>를 통해 여러 파일 및 디렉터리를 참조하여 <strong>통합 모듈</strong>을 작성하고 활용한다. 마치 Docker의 기본 image 만드는 것과 비슷하며 include를 통해 생성된 모듈은 image처럼 <strong>다른 기능에 재사용</strong>이 가능하다.
  </li>
  <li>
    Nginx의 각 서버나 기능은 include로 모듈화된 설정을 참조한다.
  </li>
</ul>

```nginx
# 1. include는 단일 경로를 주거나
# { }로 마스크를 하여 여러 경로를 주어
# 참조할 설정 파일 혹은 디렉토리를 지정한다.
http {
    include config.d/compression.conf;
    include sites-enabled/*.conf
}
```

<h1>3. 정적 콘텐츠 서비스하기</h1>
<ul>
  <li>
    Nginx의 /etc/nginx/conf.d/default.conf에 생성된 HTTP 파일을 변경하여 실습한다.
  </li>
</ul>

```nginx
# 1. 새로운 서버 블록을 선언하여 Nginx가 처리할 새로운 context를 정의한다.
server {

    # listen 80
    # - `80포트`로 들어오는 요청을 수신한다.
    # default_server
    # - 80포트로 요청이 들어올 경우 다른 서버 블록과 일치하는 경우가 없다면 `default`로 
    #   수행할 블록임을 의미한다.
    # - 경우에 따라 포트가 여럿일 경우 `포트를 범위로 지정`할 수도 있다.
    listen 80 default_server;

    # server_name
    # - `지정한 도메인(www.example.com)`으로 접속하는 경우 처리하도록 한다.
    server_name www.example.com;

    # location
    # - Nginx 설정에서 특정 URL 경로(URI)에 대한 요청을 어떻게 처리할지를 정의하는 
    #   `매칭 블록`이다.
    # - location은 URL 경로를 기반으로 한다.
    # - 경로나 도메인 뒤에 붙은 URL을 통합 자원 식별자(URI, Uniform Resource 
    #   Identifier)라 한다.
    location / {

        # root
        # - 주어진 컨텍스트(URL)에서 어떤 경로의 파일을 찾을지 설정한다.
        # - `root 지시자에 정의된 경로 + 수신된 URI`= 요청된 파일을 찾는 기준.
        root /usr/share/nginx/html;
        # alias /usr/share/nginx/html;
        index index.html index.htm;
    }
}
```