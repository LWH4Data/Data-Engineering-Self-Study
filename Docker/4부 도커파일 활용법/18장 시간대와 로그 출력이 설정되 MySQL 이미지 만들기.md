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
- 여기서 부터