<h1>1. 전역 설정 및 경로의 구성</h1>
<ul>
  <li>
    메이븐과 자바 개발 키트(JDK, Java Development Kit)과 같은 젠킨스에서 사용하는 여러 가지 도구와 소프트웨어의 구성 방법을 설명한다.
  </li>
</ul>

<br>

<h2>1-1. 젠킨스 로그인</h2>

```bash
# 1. Docker를 활용하기에 하단의 명령어로 컨테이너를 가동한다.
docker start jenkins
```

```bash
# 2. localhost:8081의 jenkins 접속을 위한 비밀번호를 가져온다.

# jenkins 컨테이너 내부 접속
docker exec -it jenkins bash

# 컨테이너 내부에서 비밀번호 암호키 출력.
cat /var/jenkins_home/secrets/initialAdminPassword
```

<br>

<h3><나머지 내용은 환경에 대한 설명으로 교재를 참고하며 된다.></h3>