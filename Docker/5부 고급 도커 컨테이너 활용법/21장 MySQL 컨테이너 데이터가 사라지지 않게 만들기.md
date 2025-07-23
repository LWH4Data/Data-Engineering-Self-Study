<ul>
  <li>
    볼륨을 활용하여 컨테이너를 삭제하더라도 컨테이너 데이터가 사라지지 않게 하는 방법.
  </li>
  <li>
    볼륨을 사용하면 <strong>컨테이너 내부</strong>에서 생성된 액세스 로그나 동작 기록 등 중요한 데이터를 <strong>컨테이너 외부에 안전하게 보존</strong>할 수 있다.
  </li>
</ul>

<br>

<h1>1. 볼륨 작성하기 volume create</h1>
<h2>1-1. 명령어 설명</h2>

```bash
docker volume create [OPTIONS] [VOLUME]

# [OPTIONS]
#   ▷ --name: 볼륨명을 지정하여 무작위 값을 피한다. 
```

<br>

<h2>1-2. 볼륨 작성하기</h2>
<ul>
  <li>
    볼륨을 작성할 때에는 volume create 명령어를 활용한다.
  </li>
  <li>
    무작위 ID가 배정되지 않도록 --name을 지정할 수 있다. ([VOLUME] 매개변수로 지정도 가능하다).
  </li>
</ul>

```bash
# 1. my-volume이라는 이름의 볼륨 생성.
docker volume create --name my-volume
```

```bash
# 2. 생성한 볼륨 확인
docker volume ls
```

<br><br>

<h1>2. 컨테이너 가동할 때 볼륨 마운트하기 container run --mount</h1>
<ul>
  <li>
    --mount 옵션을 이용하여 마운트 실습
  </li>
  <li>
    요약
  </li>
    <ul>
      <li>
        볼륨: 데이터가 저장되는 외부 공간.
      </li>
      <li>
        컨테이너: 실행되는 가상 환경
      </li>
      <li>
        마운트: 볼륨과 컨테이너를 연결하는 다리.
      </li>
    </ul>
</ul>

<br>

<h2>2-1. 작성한 볼륨을 우분투 컨테이너에 마운트하기</h2>

```bash
# 1. mount 옵션을 추가하여 우분투 컨테이너 가동.
docker container run                                        \
--name ubuntu1                                              \
--rm                                                        \
--interactive                                               \
--tty                                                       \
# 공백 없어야 함.
--mount type=volume,source=my-volume,destination=/my-work \
ubuntu:24.04

# type: 마운트의 유형을 지정. 볼륨을 마운트할 경우에는 volume으로 설정.
# source: 마운트의 원본. 미리 생성된 도커 볼륨 이름을 지정.
# destination: 마운트의 대상. 컨테이너 내부에서 데이터를 접근하고 저장할 경로를 지정.

# 즉, 컨테이너 내부의 destination 경로에 쓰거나 읽는 데이터는 
# 컨테이너 외부의 source(볼륨)에 저장된다.
```

```bash
# 2. 컨테이너 내에서(프롬프트창) ls를 통해 my-work 디렉터리가 있는지 확인.
ls
```

```bash
# 3. my-work 디렉터리 내부는 비어있어야 한다.
ls /my-work/
```

```bash
# 4. my-work 디렉터리 내부에 ehco 명령어와 리다이렉트(>)를 통해 텍스트 파일 작성
echo 'hello from container.' > /my-work/hello.txt
```

```bash
# 5. my-work 내부에 텍스트 파일이 잘 들어갔는지 확인.
cat /my-work/hello.txt
```

```bash
# 6. 현재 컨테이너(ubuntu1)를 삭제한다.
docker container stop ubuntu1
```

```bash
# 7. 볼륨이 제대로 작동하는지 확인하기 위해 볼륨을 마운트하여 ubuntu2 컨테이너 가동.
docker container run                                        \
--name ubuntu2                                              \
--rm                                                        \
--interactive                                               \
--tty                                                       \
--mount type=volume,source=my-volume,destination=/my-work   \
```

```bash
# 8. 가동된 ubuntu2 컨테이너에서 마운트된 my-work 확인
 ls /my-work/
```

```bash
# 9. my-work 디렉토리 내의 텍스트 파일 확인.
cat /my-work/hello.txt
# ubuntu1에 있던 hello.txt 파일이 그대로 ubuntu2에도 있음을 확인할 수 있다.
```

<br>

<h2>2-2. 새로운 볼륨을 작성해서 MySQL 컨테이너에 마운트하기</h2>

```bash
# 1. MySQL에 사용할 volume을 생성.
docker volume create --name db-volume
```

```bash
# 2. MySQL 서버가 데이터를 보관하는 디렉터리에 볼륨을 마운트.
# MySQL은 기본적으로 /var/lib/mysql에 데이터를 적재한다.
# 명령어를 통해 MySQL의 디렉터리 확인.
docker container run --rm mysql:8.4.2 cat /etc/my.cnf
```

```bash
# 3. 볼륨을 마운트하여 MySQL 컨테이너 가동.
docker container run                                                \
--name db1                                                          \
--rm                                                                \
--detach                                                            \
--env MYSQL_ROOT_PASSWORD=secret                                    \
--env MYSQL_DATABASE=sample                                         \
--publish 3306:3306                                                 \
--mount type=volume,source=db-volume,destination=/var/lib/mysql     \
mysql:8.4.2
```

```bash
# 2. 볼륨 확인을 위해 mysql 컨테이너 서버 접속.
mysql --host=127.0.0.1 --port=3306 --user=root --password=secret sample
```

```sql
-- 3. 마운트를 할 작업을 수행.
-- 테이블 생성
create table user ( id int, name varchar(32) );

-- 데이터 삽입
insert into user ( id, name ) values ( 1, 'John Doe' );
insert into user ( id, name ) values ( 2, 'Jane Doe' );

-- 테이블 조회
select * from user;
```

```bash
# 4. 볼륨에 데이터가 보관 되었는지 확인하기 위해 db1 컨테이너 정지.
docker container stop db1
```

```bash
# 5. 마운트 볼륨을 확인하기 위한 새로운 컨테이너 db2를 가동
docker container run                                            \
--name db2                                                      \
--rm                                                            \
--detach                                                        \
--publish 3306:3306                                             \
--mount type=volume,source=db-volume,destination=/var/lib/mysql \
```

```bash
# 6. 확인을 위해 db2의 컨테이너 서버 접속
mysql --host=127.0.0.1 --port=3306 --user=root --password=secret sample
```

```sql
-- 7. 이미 마운트한 데이터가 있기에 바로 조회
select * from user;
-- db1에서 생성한 user 테이블이 출력된다.

exit
```