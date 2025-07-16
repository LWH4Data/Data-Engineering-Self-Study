<ul>
  <li>
    환경 변수를 이용해 컨테이너에서 실행되는 애플리케이션에 <strong>매개변수</strong> 전달.
  </li>
  <li>
    백그라운드로 컨테이너를 가동하면 컨테이너를 가동할 때마다 <strong>터미널</strong>을 열 필요가 없어진다.
  </li>
</ul>
<br>

<h1>1. 컨테이너 환경 변수 설정하기 container run --env</h1>
<h2>1-1. [OPTIONS]</h2>
<ul>
  <li>
    -e 혹은 --env
  </li>
    <ul>
      <li>
        컨테이너 환경변수 설정.
      </li>
      <li>
        가동할 컨테이너에 매개변수 전달.
      </li>
    </ul>
</ul>
<br>

<h2>1-2. MySQL 서버 가동하기</h2>
<ul>
  <li>
    환경 변수는 이미지에 따라 다르다.
  </li>
  <li>
    container run을 실행한 터미널은 컨테이너 내의 애플리케이션 서버가 작동하는 동안에는 사용할 수 없다. 따라서 <strong>새로운 터미널</strong>을 열어야 한다.
  </li>
</ul>

```bash
# 1. MySQL 서버 컨테이너로 띄우기
docker container run --name db --rm mysql

# 실행 결과로 나오는 환경 변수들 중 하나를 지정하라는 오류가 발생한다.

# 2. 환경 변수를 지정하여 다시 컨테이너 가동.
# (윈도우 셸에서는 '\' 대신 '`(백틱)' 사용.)
docker container run \
--name db \
--rm \
# 환경 변수 추가.
--env MYSQL_ROOT_PASSWORD=secret \
--publish 3306:3306
mysql
```

<h2>1-3. MySQL 서버에 접속하기</h2>
<h3>1-3-1. OS별 MySQL 설치 방법</h3>

```bash
# 1. Windows 설치
# MySQL 사이트: "https://dev.mysql.com/downloads/mysql/"에서 다운로드.
# 등록 화면이 뜰 경우 [No thanks, just start my download.]를 선택하여 등록없이 다운.

# 파워셸에서 설치확인
mysql --version
```

```bash
# 2. WSL 2 우분투 설치
apt update
apt install -y mysql -client
mysql --version
```

```bash
# 3. 맥 OS 확인
brew install mysql-client
mysql --version
```

<br>
<h3>1-3-2. 컨테이너 내의 MySQL 서버 접속</h3>
<ul>
  <li>
    --host로 IP를 지정하는 이유
  </li>
    <ul>
      <li>
        --host를 지정하여 현재 <strong>호스트 머신의 TCP/IP</strong>로 접근한다.
      </li>
      <li>
        지정하지 않을 경우 UNIX 소켓을 사용하기에 로컬 환경에 MySQL이 다운되어 있어야 한다.
      </li>
        <ul>
          <li>
            UNIX는 네트워크(IP/PORT) <strong>운영체제 내부</strong>에서 직접 연결을 하는 방식이다.
          </li>
          <li>
            따라서 컨테이너라는 독립된 공간에 접속하기 위해서는 --host를 주어 TCP/IP로 접근한다.
          </li>
      <li>
        현재 호스트 mysql 클라이언트 → 127.0.0.1:3306 (도커가 Listening 중)
        → 연결된 컨테이너의 3306 포트 → 컨테이너 내부의 MySQL 서버
      </li>
        </ul>
    </ul>
</ul>

```bash
# MySQL 서버 접속
mysql --host=127.0.0.1 --port=3306 --user=root --password = secret
# --host=127.0.0.1: 로컬 서버 지정. (localhost와 동일)
# --port=3306: MySQL의 기본서버 3306을 제외. 전체는 3306:3306
# --user=root: 루트 사용자로 접속 (일반적으로 root 사용)
# --password=secret: --env MYSQL_ROOT_PASSWORD=secret에서 정한 값.
```

```bash
# 2. MySQL 서버 정지.
docker container stop db
```

<br>
<h2>1-4. MySQL 서버를 가동해서 사용자와 데이터베이스 작성하기</h2>

```bash
docker container run              \
--name db                         \
--rm                              \
# 루트 사용자의 암호
--env MYSQL_ROOT_PASSWORD=secret  \
# 일반 사용자 생성
--env MYSQL_USER=app              \
# 일반 사용자의 패스워드
--env MYSQL_PASSWORD=pass1234     \
# sample이라는 데이터베이스 생성
--env MYSQL_DATABASE=sample       \
--publish 3306:3306               \
mysql
```

- 132p 부터