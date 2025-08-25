<ul>
  <li>
    교재는 로컬 환경을 가정하고 환경 구성을 하지만 나는 Docker를 활용하기에 환경 구성을 수정해야 한다.
  </li>
  <li>
    전역 도구 페이지에서 JDK와 메이븐을 구성하는 방법을 배운다.
  </li>
</ul>

<br>

<h1>1. 전역 도구 구성 설정</h1>
<ul>
  <li>
    http://localhost:8081/manage/configureTools/
  </li>
  <li>
    설치된 전역도구의 설정을 확인할 수 있다.
  </li>
</ul>

<br>

<h2>1-1. 전역 도구 구성의 이해</h2>
<h3>1-1-1. Maven</h3>
<ul>
  <li>
    Jenkins의 공식 문서를 통해 Docker를 실행하고 URL로 MAVEN을 받을 경우 네트워크 문제로 불가하다. 따라서 Dockerfile 내에서 MAVEN과 여러 플러그인들을 미리 받아둔다.
  </li>
  <li>
    수동으로 설치를 하였기에 Maven installations에서 add Maven을 할 때 install automatically를 설정하지 않는다.
  </li>
</ul>

```Dockerfile
# 1. Maven 다운을 위해 Dockerfile 수정.
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
# 2. 컨테이너 내부로 접속하여 Maven 설치 여부 확인
docker exec -it MyJenkins bash
```

```bash
# 3. Maven 확인
mvn -v
```

<br>

<h3>1-1-2. JDK</h3>
<ul>
  <li>
    JDK는 이미 이미지 내에 포함되어 있기에 설치가 필요없다.
  </li>
  <li>
    단, add JDK를 할 때 jenkins는 자바를 관리하지 않기에 컨테이너 내부의 JDK 경로를 JAVA_HOME으로 주어야 한다.
  </li>
</ul>

```bash
# 1. MyJenkins 컨테이너 접속
docker exec -it MyJenkins bash
```

```bash
# 2. JDK 경로 확인.
readlink -f $(which java) | sed 's:/bin/java::'

# 위의 결과를 JAVA_HOME으로 설정한다.
```