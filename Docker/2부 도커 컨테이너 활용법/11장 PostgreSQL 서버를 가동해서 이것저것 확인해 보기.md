<ul>
  <li>
    container log: 백그라운드로 실행한 컨테이너의 오류 메시지를 확인할 수 있다.
  </li>
  <li>
    container exec: 컨테이너에서 원하는 명령어를 실행할 수 있다.
  </li>
</ul>
<br>

<h1>1. 컨테이너 출력 확인하기 container logs</h1>
<h2>1-1. 명령어 및 옵션</h2>
<ul>
  <li>
    명령어
  </li>
    <ul>
      <li>
        docker container logs [OPTIONS] CONTAINER
      </li>
    </ul>
  <li>
    옵션
  </li>
    <ul>
      <li>
        <strong>-f</strong> 혹은 <strong>--follow</strong>
      </li>
        <ul>
          <li>
            <strong>파일 마지막 부분</strong>을 실시간으로 표시한다.
          </li>
          <li>
            지속적으로 <strong>로그를 추적</strong>할 수 있다.
          </li>
        </ul>
    </ul>
</ul>
<br>

<h2>1-2. 백그라운드로 가동한 컨테이너 출력 확인하기</h2>
<ul>
  <li>
    처음 사용하는 컨테이너의 경우 --detach와 --rm을 설정하지 않는 것이 좋다.
  </li>
    <ul>
      <li>
        <strong>--detach</strong>: 컨테이너의 <strong>가동여부</strong>를 확인하기 어렵다.
      </li>
      <li>
        <strong>--rm</strong>: 컨테이너가 완전히 사라지기에 <strong>로그 추적</strong>이 불가하다.
      </li>
    </ul>
  <li>
    운영 자동화 등의 과정으로 인해 백그라운드(--detach)로 컨테이너를 가동하는 일이 생기기에 container logs로 확인해 보는 습관을 갖는 것이 좋다.
  </li>
  <li>
    출력되는 로그들은 원래 터미널에 출력되는 내용과 동일하다. (백그라운드라 로그를 불러오는 것 뿐).
  </li>
</ul>

```bash
# 1. PostgreSQL 컨테이너 가동
# (환경변수를 전달하지 않은 실패 사례)
docker container run        \
--name db                   \
--rm                        \
--detach                    \
--publish 5432:5432         \
postgres

# 컨테이너 ID가 출력되지만 실제로는 환경변수가 
# 전달되지 않기에 컨테이너가 가동되지 않는다.
```

```bash
# 2. --rm을 제거하고 백그라운드로 실행(--detach)
# 이번에도 환경변수를 전달하지 않기에 컨테이너는 가동 X
# 단, --rm이 제외되어 로그를 확인할 수 있다.
docker container run        \
--name db                   \
--detach                    \
--publish 5432:5432         \
postgres
```

```bash
# 3. container log를 통해 로그를 확인
docer container log db

# 로그 결과는 환경변수가 전달되지 않아 
# 컨테이너가 가동되지 않았음을 보여준다.
```

```bash
# 4. 환경변수를 전달하여 다시 postgres 컨테이너 가동.

# 단, 바로 앞에서 --rm 옵션 없이 db이름을 사용하였기에 일단 제거
docker container --rm db

# 다시 환경변수를 포함하여 postgres 컨테이너를 가동.
docker container run            \
--name db                       \
--detach                        \
--env POSTGRES_PASSWORD=secret  \
--publish 5432:5432             \
postgres

# 컨테이너 ID가 출력됨.
```

```bash
# 5. 가동된 컨테이너의 로그 확인
docker container logs db

# 정상적으로 가동되었음을 확인할 수 있다.
```

<br>
<h2>1-3. 실시간으로 출력 내용 확인하기</h2>
<h3>1-3-1. psql 명령어 설치</h3>

```bash
# 1. 윈도우
# "https://www.postgresql.org/download/windows/"에서 설치
# 파워셸에서 설치 확인 psql --version

# 2. WSL2 우분투
# apt 명령어로 다운.
sudo apt update
sudo apt install -y postgresql-client
psql --version

# 3. 맥 OS
# brew 명령어로 다운.
brew install libpq
brew link --force libpq
psql --version
```
<br>

<h3>1-3-2. 컨테이너의 psql 서버 접속하기</h3>
<ul>
  <li>
    <strong>container logs</strong>와 <strong>--follow</strong> 옵션은 디버깅의 기본이다.
  </li>
  <li>
    <strong>ctrl + c</strong>를 통해 container logs --follow를 종료할 수 있다.
  </li>
</ul>

```bash
# 1. psql 서버접속
psql --host=127.0.0.1 --port=5432 --username=postgres
# 패스워드 입력
```

```bash
# 2. 일부러 오류가 발생하는 명령어를 실행하고 로그 확인
select * from users;
# 에러 메시지가 출력됨.
```

```bash
# 3. docker container logs를 통해 로그 확인
docker container logs db
# 오류 출력이 누적되어 출력됨.
```

```bash
# 4. --follow 옵션을 통해 실시간으로 로그가 출력되도록 한다.
# 설정을 안하면 매번 전체 로그가 나오기에 가독성이 떨어짐.
docker container logs --follow db
# 오류가 발생할 때마다 로그가 새롭게 출력된다.
```

<br><br>
<h1>2. 가동 중인 컨테이너에 명령하기 container exec</h1>
<h2>2-1. 명령어 및 옵션</h2>
<ul>
  <li>
    명렁어
  </li>
    <ul>
      <li>
        docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]
      </li>
    </ul>
  <li>
    옵션
  </li>
    <ul>
      <li>
        -i 혹은 --interactive
      </li>
        <ul>
          <li>
            컨테이너 표준 입력에 접속
          </li>
          <li>
            컨테이너를 대화형으로 조작
          </li>
        </ul>
      <li>
        -t 혹은 --tty
      </li>
        <ul>
          <li>
            유사 터미널 배정
          </li>
          <li>
            컨테이너를 대화형으로 조작
          </li>
        </ul>
    </ul>
</ul>
<br>

<h2>2-2. 가동 중인 컨테이너에 명령어 실행하기</h2>

```bash
# 1. PostgreSQL 컨테이너에서 head 명령어 수행.
# /etc/os-release 파일에서 컨테이너 OS를 확인한다.
docker container exec db head -n 4 /etc/os-release
# 현재 [OPTIONS]는 없다.
# db: postgreSQL 컨테이너명.
# head: COMMAND
# -n 4 /etc/os-release: [ARG...]
```

<br>

<h2>2-3. container exec와 container run 차이점</h2>
<h3>2-3-1. container run</h3>
<ul>
  <li>
    docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]
  </li>
  <li>
    container run은 IMAGE를 컨테이너로 띄우고 <strong>PID1을 생성</strong>한다.
  </li>
  <li>
    만약 명령어가 입력된다면 해당 명령어가 PID1이 되기에 <strong>컨테이너가 종료돼 버리는 문제</strong>가 발생한다.
  </li>
  <li>
    따라서 명령어 수행을 container run으로 하는 것은 권장되지 않는다.
  </li>
</ul>

<br>
<h3>2-3-2. container exec</h3>
<ul>
  <li>
    docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]
  </li>
  <li>
    container exec는 <strong>생성된 PID1 위에 명령어를 실행</strong>한다. 따라서 명령어가 종료되어도 컨테이너가 종료되는 문제는 발생하지 않는다.
  </li>
  <li>
    따라서 명령어를 수행해야 한다면 <strong>container run을 통해 container를 가동</strong>한 뒤 <strong>container exec로 명령어를 실행</strong>하는 것이 좋다.
  </li>
</ul>
<br>

<h2>2-4. 가동 중인 컨테이너에 bash 실행하기</h2>
<ul>
  <li>
    컨테이너 내로 접속해서 대화형식으로 조작이 가능하다. (실제 리눅스 환경처럼).
  </li>
</ul>

```bash
# 1. 가동 중인 PostgreSQL에 bash 실행.
# bash로 접속해서 PostgreSQL 조작가능.
docker container exec       \
# 대화형으로 조작하기 위해 -i와 -t 설정을 추가한다.
--interactive               \
--tty                       \
# 대상이 되는 컨테이너명 지정
db                          \
# bash 명령어 수행
bash

# 이후 리눅스 환경을 직접 조작하는 것처럼 활용이 가능하다.
# (cd, ls 등의 명령어와 tab을 통한 자동 완성 가능).
```

```bash
# 2. 실습 종료를 위헤 db 컨테이너 정지
docker container stop db
```

<h2>2-5. 컨테이너에 SSH로 접속한다는 오해</h2>
<h3>2-5-1. SSH란?</h3>
<ul>
  <li>
    원격 접속을 위해 설계된 네트워크 기반 보안 프로토콜이다.
  </li>
</ul>
<br>

<h3>2-5-2. Docker와 SSH</h3>
<ul>
  <li>
    Dokcer는 bash 명령어를 통해 접속하면 되기에 SSH를 이용할 필요가 없다.
  </li>
</ul>
<br><br>

<h2>2-6. PostgreSQL 서버에 접속하는 방법 정리하기</h2>
- p150부터