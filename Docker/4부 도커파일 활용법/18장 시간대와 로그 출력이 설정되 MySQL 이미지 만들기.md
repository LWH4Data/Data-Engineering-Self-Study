<ul>
  <li>
    ENV와 COPY 명령으로 이미지를 확장하는 방법
  </li>
</ul>
<br>

<h1>1. 이미지 환경 변수 지정하기 ENV</h1>
<h2>1-1. 명령어</h2>
<ul>
  <li>
    메타데이터에 환경 변술글 추가한다.
  </li>
</ul>

```Dockerfile
ENV <key>=<value> ...
```

<br>

<h2>1-2. MySQL 컨테이너의 시간대 확인하기</h2>

```bash
# 1. 이전에 배운 것처럼 MySQL 컨테이너 가동
docker conatiner run            \
--name db                       \
--rm                            \
--detach                        \
--env MYSQL_ROOT_PASWORD=secret \
--publich 3306:3306             \
mysql:9.0.1
```

```bash
# 2. mysql을 통해 프롬프트 접속
mysql --host=127.0.0.1 --port=3306 --user=root --password=secret
```

```sql
-- 3. select now()를 통해 MySQL 시간대 확인
select now();
```

```sql
-- 4. 한국과 시간 차이가 나기에 서버 시간대를 확인한다.
-- (도커 허브는 전세계 공유이기에 한국 시간대가 아니다)
show variables like '%time_zone%';
```

```bash
# 5. docker container exec를 통해 시간 환경 변수(TZ) 설정 여부 확인
# 당연히 비어있음.
docker container exec db printenv TZ
```

<br>

<h2>1-3. ENV 명령으로 환경 변수를 설정해서 시간대 변경하기</h2>

```Dockerfile
# 1. 아래와 같이 Dokcerfile 내에서 시간 환경 변수 설정.
FROM mysql:9.0.1

ENV TZ=Asia/Seoul
```

```bash
# 2. 작성한 Dockerfile 이미지로 빌드
docker image build --tag my-mysql:seoul .
```

```bash
# 3. 다시 컨테이너 가동
docker container run             \
--name db                        \
--rm                             \
--detach                         \
--env MYSQL_ROOT_PASSWORD=secret \
--publish 3306:3306              \
my-mysql:seoul
```

```sql
-- 4. 다시 mysql 접속 후 시간 조회
select now();
```

```sql
-- 5. 서버 시간이 변경 되었는지 확인
show variables like '%time_zone%';
-- KST로 한국 시간대로 변경 되었음을 확인할 수 있다.
```

<br>

<h2>1-4. ENV와 container run --env</h2>
<ul>
  <li>
    <strong>메타데이터</strong>를 <strong>이미지 수준</strong>에서 주는가, <strong>컨테이너 수준</strong>에서 주는가의 차이를 갖는다.
  </li>
    <ul>
      <li>
        <strong>ENV</strong>: 이미지에 설정하기에 해당 이미지를 기반으로 하는 모든 컨테이너에 적용된다.
      </li>
      <li>
        <strong>container run --env</strong>: 컨테이너를 가동할 때 적용되기에 컨테이너마다 개별적으로 적용된다.
      </li>
    </ul>
</ul>

<br><br>

<h1>2. 호스트머신의 파일을 이미지에 추가하기 COPY</h1>
<h2>2-1. 명령어</h2>
<ul>
  <li>
    COPY 명령은 <strong>호스트 머신의 파일</strong>을 <strong>이미지에 복사</strong>하여 레이어를 작성한다.
  </li>
</ul>

```bash
COPY [--chown=<user>:<group>] [--chmod=<perms>] <src>... <dest>

# <src>... <dest>: 다수의 원본 파일을 <dest>로 복사할 수 있음.
```
<br>

<h2>2-2. 로그 출력 설정과 설정 파일</h2>
<ul>
  <li>
    컨테이너는 <strong>일반 쿼리 로그</strong>를 출력하지 않는다. 다수의 요청이 발생하면 로그 파일이 너무 커지기 때문이다.
  </li>
  <li>
    단, 개인용으로는 <strong>디버깅</strong>이 용이하고 파일 크기가 문제가 되지 않기에 사용할만 하다.
  </li>
  <li>
    로그 설정 파일을 해당 컨테이너에서만 상용하고 싶다면 <strong>vi</strong>를 통해 설정 파일을 만든다. 만약 모든 컨테이너에 적용하고 싶다면 <strong>이미지</strong>를 설정해야 한다.
  </li>
</ul>
<br>

<h2>2-3. COPY 명령으로 설정 파일을 추가하고 로그 출력 활성화하기</h2>
<ul>
  <li>
    이때까지는 vscode로 실습하였는데 터미널 차이로 인해 <strong>Ubuntu</strong>를 실습환경으로 사용하기 시작하였다.
  </li>
    <ul>
      <li>
        docker container에서 WSL integration 설정에 Ubuntu를 활성화 한다.
      </li>
      <li>
        <strong>vscode</strong>에서 <strong>ctrl + shift + p</strong>를 입력한 후 <strong>WSL:connect</strong>을 통해 우분투 환경을 vscode에서 사용할 수 있다.
      </li>
    </ul>
</ul>

```text
# 1. my.cnf 파일을 생성.
# 가동시킬 MySQL 컨테이너가 로그를 기록할 파일을 생성하는 설정을 담는 파일이다.
[mysqld]
general_log = 1
general_log_file = /var/log/query.log
```

```Dockerfile
# 2. 같은 경로에 Dockerfile 생성.
FROM mysql:9.0.1

# 현재 디렉토리의 my_cnf을 참조하여 컨테이너 내의 .etc/my.cnf를 생성.
COPY ./my_cnf /etc/my.cnf
```

```bash
# 3. 생성한 Dockerfile로 이미지 빌드
docker image build --tag my-mysql:log .
```

```bash
# 4. 로그 확인을 위한 컨테이너 가동
docker container run             \
--name db                        \
--rm                             \
--detach                         \
--env MYSQL_ROOT_PASSWORD=secret \
--publish 3306:3306              \
my-mysql:log
```

```bash
# 5. mysql 컨테이너 접속(서버)
mysql --host=127.0.0.1 --port=3306 --user=root --password=secret
```

```sql
-- 6. 잘 작동 되는지 확인
select now();

-- exit;
```

```bash
# 7. 도커에 exec로 명령어를 전달하여 my.cnf로 생성한 쿼리 로그 확인.
docker container exec db ls /var/log
```

```bash
# 8. 일반 쿼리 로그의 마지막 5줄 확인.
docker container exec db tail -n 5 /var/log/query.log
```

<br>

<h2>2-4. 도커파일 작성에 필요한 지식</h2>
<ul>
  <li>
    도커파일 작성에는 도커 외에도 사용하려는 <strong>애플리케이션</strong>에 대한 지식도 필요하다. (MySQL 예).
  </li>
    <ul>
      <li>
        RUN: 리눅스 명령어를 지정하기에 apt 명령어 사용법 등.
      </li>
      <li>
        ENV: 환경 변수를 지정하기에 TZ와 같은 환경 변수나 시간대 관련 지식.
      </li>
      <li>
        COPY: my.cnf와 같은 설치 파일을 사용할 겨우 복사할 위치.
      </li>
    </ul>
  <li>
    따라서 디버깅을 할 때에 <strong>도커의 문제인지 도커 외의 문제</strong>인지를 판단하고 접근해야 한다.
  </li>
  <li>
    도커 문서에는 도커파일 등 파일 참조 문서도 있기에 옵션, 각종 주의사항, 권한 설정 등에 대해 찾아볼 수 있다.
  </li>
</ul>