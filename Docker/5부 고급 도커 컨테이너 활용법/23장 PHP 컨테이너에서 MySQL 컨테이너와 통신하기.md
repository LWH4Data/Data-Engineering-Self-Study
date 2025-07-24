<ul>
  <li>
    컨테이너에서 컨테이너로 소통하는 방법.
  </li>
</ul>

<br>

<h1>1. 네트워크 작성하기 network create</h1>
<h2>1-1. 명령어</h2>

```bash
docker network create [OPTIONS] NETWORK
```

<br>
<h2>1-2. 네트워크 작성하기</h2>

```bash
# 1. docker network create를 통해 네트워크 생성.

# 동일한 도커 엔진에서 컨테이너끼리 통신할 때에는 브릿지 드라이버의 네트워크를 이용한다.

# network create를 사용할 때 명시적으로 지정하지 않으면 브릿지 네트워크로 자동 설정된다. 
docker network create my-network
```

```bash
# 2. network ls를 통해 전체 네트워크 확인
docker network ls
# 앞서 생성한 my-network 네트워크가 존재한다.
```

<br>

<h2>1-3. PHP 이미지에 ping 명령어 설치하기</h2>
<ul>
  <li>
    ping 명령어는 네트워크 개통을 확인하는 명령어이다.
  </li>
</ul>

```Dockerfile
# 1. PHP에는 ping이 없기에 설치를 위해 Dockerfile을 세팅한다.
FROM php:8.2.23

RUN apt-get update
RUN apt-get install -y iputils-ping
```

```bash
# 2. 생성한 Dockerfile을 기준으로 이미지를 빌드한다.
docker image build --tag my-php:ping
```

```bash
# 3. ping 명령어로 도커를 가동하여 localhost 통신을 확인한다.
docker container run my-php:ping ping -c 3 -t 1 localhost
# packets 세 개를 수신하고 손실이 0%면 성공.
```

<br><br>

<h1>2. 컨테이너 가동 시 네트워크에 접속하기 container run --network</h1>
<h2>2-1. 옵션 설명</h2>
<ul>
  <li>
    <strong>-</strong> 혹은 <strong>--network</strong>
  </li>
    <ul>
      <li>
        컨테이너를 네트워크에 접속한다. 다른 컨테이너와 통신할 수 있다.
      </li>
    </ul>
</ul>

<br>

<h2>2-2. MySQL 컨테이너 가동하기</h2>

```bash
# 1. 호출되는 쪽인 MySQL 컨테이너를 먼저 가동.
docker container run                \
--name db                           \
--rm                                \
--detach                            \
--env MYSQL_ROOT_PASSWORK           \
# 환경 변수를 통해 sample 데이터베이스 이용
--env MYSQL_DATABASE=sample         \
# 컨테이너끼리의 통신에는 포트 공개가 필요 없으나
# 호스트 머신에서 접속하여 디버깅할 수 있게 하기위해 공개
--publish 3306:3306                 \
--network my-network                \
mysql:8.4.2
```

```bash
# 2. MySQL 서버에 접속
mysql --host=127.0.0.1 --port=3306 --user=root --password=secret sample
```

```sql
-- 3. 네트워크 테스트를 위한 MySQL DB 작성.
-- 테이블 생성
create table user ( id int, name varchar(32) );

-- 데이터 입력
insert into user ( id, name ) values ( 1, 'John Doe' );
insert into user ( id, name ) values ( 2, 'Jane Doe' );

-- 결과 확인
select * from user

exit
```

<br>

<h2>2-3. PHP 컨테이너에서 MySQL 컨테이너와 통신할 수 있는지 확인하기</h2>

```bash
# 1. 바로 php 컨테이너를 가동하기 전 네트워크를 먼저 확인한다.
# 이를 통해 디버깅할 범위를 줄일 수 있다.
docker container run --network my-network my-php:ping ping -c 3 -t 1 db

# 패킷 소실이 0%라면 완료.
```

<br>

<h2>2-4. PHP 컨테이너에서 MySQL 서버에 접속하는 코드 구현하기</h2>

```Dockerfile
# 1. PHP에서 MySQL 서버에 접근하기 위해서는 pdo_mysql이 필요하다.

# 앞서 작성한 PHP의 Dockerfile을 활용하여 이미지를 빌드할 때 다룬로드 한다.

FROM php:8.2.23

RUN apt-get update
RUN apt-get install -y iputils-ping

RUN docker-php-ext-install pdo_mysql
```

```bash
# 2. 수정한 Dockerfile을 기반으로 다시 이미지 빌드.
docker image build --tag my-php:pdo_mysql .
```

```php
# 3. 데이터베이스에 접속하는 코드를 php 파일로 작성.
<?php

// 데이터베이스에 접속
$dsn = 'mysql:host=db;port=3306;dbname=sample';
$username = 'root';
$password = 'secret';
$pdo = new PDO($dsn, $username, $password);

// user 테이블 내용을 전부 출력
$statement = $pdo->query('select * from user');
$statement->execute();
while ($row = $statement->fetch()) {
    echo '-id: ' . $row['id'] . ', name: ' . $row['name'] . PHP_EOL;
}

// 접속 종료
$pdo = null;
```

<br>

<h2>2-5. PHP 컨테이너에서 MySQL 컨테이너와 통신하기</h2>

```bash
docker container run                                   \
--rm                                                   \
# 호스트 머신에 있는 main.php를 컨테이너에서 실행할 것이기에 바인드 마운트.
--mount type=bind,source="$(pwd)",destination=/my-work \
--network my-network                                   \
my-php:pdo_mysql                                       \
php /my-work/main.php
```

<br>

<h2>2-6. 잘 안될 때 확인 방법</h2>
<ul>
  <li>
    container ls --all을 통해 컨테이너가 가동 중인지 확인.
  </li>
  <li>
    --detach 옵션을 제외하여 오류가 발생하는지 확인.
  </li>
  <li>
    network inspect에 연결된 컨테이너와 container ls를 통해 가동 중인 컨테이너의 일름이 일치하는지 확인.
  </li>
  <li>
    바인드 마운트하려는 파일의 경로 확인. 이후 옵션까지 확인.
  </li>
</ul>

<br><br>

<h1>3. 기본 브릿지 네트워크를 사용한 컨테이너 통신</h1>
<ul>
  <li>
    기본 브릿지 네트워크를 추천하지 않는 이유를 설명한다.
  </li>
</ul>

<br>

<h2>3-1. IP 주소를 사용하는 통신</h2>
<ul>
  <li>
    컨테이너의 IP 주소는 가동할 때마다 <strong>매번 변경</strong>되기에 확인하기 번거롭다.
  </li>
  <li>
    기본 브릿지 네트워크는 통신 대상을 <strong>컨테이너명</strong>으로 지정할 수 없기에 IP 주소를 사용해야 하며 그렇기에 권장되지 않는다.
  </li>
</ul>

```bash
# 1. 네트워크를 지정하지 않고 기본 브릿지 네트워크로 컨테이너 가동
docker container run --name called --rm --detach nginx:1.25
```

```bash
# 2. IP 주소를 활용하여 통신할 것이기에 called 컨테이너의 IP 주소 확인
docker container inspect called

# 'ctrl + F'에서 "IPAddress"를 검색
# 127.17.0.2
```

```bash
# 3. calling 컨테이너를 가동하고 ping 명령어로 called 컨테이너에 접근한다.
# 두 컨테이너 모두 기본 브릿지 네트워크를 사용하기에 네트워크는 설정 X.
docker container run        \
--name calling              \
--rm                        \
my-php:ping                 \
ping -c 3 -t 1 172.17.0.2
```

<br>

<h2>3-2. --link를 사용하는 통신</h2>
<ul>
  <li>
    --link는 컨테이너명을 활용하지만, 결국 <strong>'컨테이너명 → IP'</strong>로 정적 매핑되므로 재시작 시 유효하지 않을 수 있어 권장되지 않는다.
  </li>
  <li>
    또한 --link는 통신하는 컨테이너의 <strong>일부 환경 변수를 함께 공유</strong>하므로 보안상 문제가 발생할 수 있다.
  </li>
</ul>

```bash
# 1. 일단 통신 확인을 위해 컨테이너를 가동한다.
docker container run            \
--name calling                  \
--rm                            \
--interactive                   \
--tty                           \
--link called:web-server        \
my-php:ping                     \
bash
```

```php
# 2. 컨테이너에 접속하여 환경 변수를 확인하면 공유되는 것을 알 수 있다.
env | sort | grep WEB_SERVER_ENV_
```