# 1. 개요
- <CI/CD Pipeline Using Jenkins Unleashed>로 정리

```bash
# 1. 하단의 명령어로 컨테이너 가동.
docker container run jenkins

# 2. localhost:8081로 접근. (spring을 사용 중이기애).

# 3. 하단의 명령어로 컨테이너 내의 jenkins 비밀번호 확인
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```