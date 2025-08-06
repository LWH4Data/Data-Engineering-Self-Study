<ul>
  <li>
    나는 Docker를 통해 Jenkins 실습을 진행한다.
  </li>
  <li>
    https://www.jenkins.io/doc/book/installing/docker/ 해당 링크는 젠킨스의 공식 문서로 Docker로 활용하는 법이 나와있다.
  </li>
</ul>

```bash
# 후에 컨테이너 재가동할 일이 있을까봐 기록.
# 방법은 모두 공식 문서에 존재한다.

# 1. Docker nwtwork 부터 생성
docker network create jenkins
```

```bash
# 2. 도커를 가동하여 이미지 받기.
docker run \
  # 이름 jenkins-prac으로 수정
  --name jenkins-prac \
  --rm \
  --detach \
  --privileged \
  --network jenkins \
  --network-alias docker \
  --env DOCKER_TLS_CERTDIR=/certs \
  --volume jenkins-docker-certs:/certs/client \
  --volume jenkins-data:/var/jenkins_home \
  --publish 2376:2376 \
  docker:dind \
  --storage-driver overlay2
```

```Dockerfile
# 3. Dockerfile 작성.
# Jenkins LTS + JDK 21
FROM jenkins/jenkins:2.516.1-jdk21

#  root 사용자로 패키지를 받기위해 설정.
USER root

# ---------------------------------------------
# Docker CLI 설치 (Docker-in-Docker 실습 대비)
# ---------------------------------------------
RUN apt-get update && apt-get install -y \
    lsb-release \
    ca-certificates \
    curl \
    wget \
    unzip \
    gnupg \
    software-properties-common

RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
    https://download.docker.com/linux/debian $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" \
    | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------
# Maven 3.9.0 설치
# ---------------------------------------------
# MAVEN이 다운받아져 있지 않기 때문에 설정.
# 웹에서 URL로 접근 불가.
ENV MAVEN_VERSION=3.9.0

RUN wget https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.zip && \
    unzip apache-maven-${MAVEN_VERSION}-bin.zip -d /opt && \
    ln -s /opt/apache-maven-${MAVEN_VERSION} /opt/maven && \
    rm apache-maven-${MAVEN_VERSION}-bin.zip

ENV MAVEN_HOME=/opt/maven
ENV PATH=$MAVEN_HOME/bin:$PATH

# ---------------------------------------------
# Jenkins 플러그인 설치 (실습에 자주 쓰이는 것)
# ---------------------------------------------
# 다운로드 완료라면 일반 유저인 jenkins로 복귀
USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow git workflow-aggregator json-path-api"
```

```bash
# 4. Dockerfile을 기반으로 이미지 빌드
docker build -t myjenkins-blueocean:2.516.1-1 .
```

```bash
# 5. 설정이 완료된 이미지로 컨테이너 가동
docker run \
  # 이름은 MyJenkins로 설정.
  --name MyJenkins \
  --restart=on-failure \
  --detach \
  --network jenkins \
  --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client \
  --env DOCKER_TLS_VERIFY=1 \
  # 개발 중에 spring을 사용 중이라 호스트 머신 포트를 8081로 변경.
  --publish 8081:8080 \
  --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.516.1-1
```

<h1>1. 젠킨스의 구성 파일 및 디렉터리 구조 이해</h1>
<ul>
  <li>
    디렉터리 구조는 교재의 p40의 [리스트 3-1] 참고
  </li>
</ul>