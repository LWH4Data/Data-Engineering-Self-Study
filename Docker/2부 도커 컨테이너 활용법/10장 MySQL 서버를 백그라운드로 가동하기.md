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
    환경 변수는 이미지에따라 다르다.
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