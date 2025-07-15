<ul>
  <li>
    컨테이너로 가동한 서버에 호스트 머신으로 접속하는 법.
  </li>
  <li>
    브라우저 혹은 기타 프로그램 등 평소 사용하는 도구에서도 접근이 가능하다.
  </li>
</ul><br>
<h1>1. 컨테이너 포트 공개하기 container run --publish</h1>
<h2>1-1. [OPTIONS]</h2>
<ul>
  <li>
    <strong>-p</strong> 혹은 <strong>--publish</strong>
  </li>
    <ul>
      <li>
        컨테이너 포트를 <strong>호스트 머신에 공개</strong>한다.
      </li>
      <li>
        컨테이너 <strong>내부 프로세스에 접근</strong>한다.
      </li>
    </ul>
  <li>
    '<strong>--publish 호스트 머신의 포트 번호:컨테이너의 포트 번호</strong>'로 연결.
  </li>
</ul>
<br>

<h2>1-2. Nginx 컨테이너를 가동해서 포트 공개하기</h2>
<ul>
  <li>
    컨테이너는 호스트 머신과 <strong>격리된 환경</strong>이다. 따라서 컨테이너 내부 프로세스에 접근할 수 없다.
  </li>
  <li>
    내부 프로세스에 접근할 수 없다는 이야기는 호스트머신의 브라우저에서 컨테이너 내부에서 실행 중인 서버를 확인할 수 없음을 의미한다.
  </li>
  <li>
    <strong>--publish</strong>를 통해 도커 <strong>내부의 서버의 포트</strong>를 <strong>호스트 머신의 포트</strong>와 <strong>연결(mapping)</strong> 하여 확인(공개)할 수 있다.
  </li>
</ul>

```bash
# 1. Nginx 이미지인 nginx를 사용하여 
# 컨테이너에서 Nginx 서버를 가동하고 브라우저로 접속

# 8080: 호스트 머신의 포트 (외부에서 접근할 때 사용하는 포트)
# 80: 컨테이너 내부에서 실행 중인 Nginx 서버의 포트

# 브라우저는 호스트 머신의 8080 포트에 접속
#   -> Docker가 해당 요청을 컨테이너 내부의 80 포트로 전달
#   -> 어느 컨테이너로 전달할지는 Docker가 자동으로 관리 (사용자에게는 추상화됨)
docker container run --rm --publish 8080:80 nginx

# 2. 브라우저에서 http://localhost:8080 접속
#   -> Docker가 컨테이너의 80 포트로 전달하여 Nginx 페이지 확인 가능
```
<br>

<h2>1-3. 가동 중인 컨테이너 포트 정보 확인하기</h2>
<ul>
  <li>
    가동 중인 컨테이너가 어떤 포트를 공개했는지는 <strong>container ls</strong>로 확인할 수 있다. 
  </li>
  <li>
    결과창에서는 <strong>PORTS</strong>로 표기된다.
  </li>
</ul>