# FastAPI 실습 프로젝트

## 프로젝트 구조

```
FastAPI_Prac/
├── compose.yaml: Docker Compose 설정 파일
├── Dockerfile: Docker 이미지 빌드 설정
├── requirements.txt: Python 패키지 의존성
└── src/: 모든 웹사이트의 코드를 포함한다.
    ├── main.py: FastAPI 애플리케이션 진입점
    ├── data/: 저장소와의 인터페이스 계층
    │   ├── __init__.py: 디렉터리를 패키지로 취급
    │   ├── creature.py: 현재 계층에서 다루는 생명체에 대한 코드
    │   └── explorer.py: 현재 계층에서 다루는 탐험가에 대한 코드
    ├── fake/: 미리 하드코딩된(스텁) 데이터
    │   ├── __init__.py
    │   ├── creature.py
    │   └── explorer.py
    ├── model/: Pydantic 모델 정의
    │   ├── __init__.py
    │   ├── creature.py
    │   └── explorer.py
    ├── service/: 비즈니스 로직 계층
    │   ├── __init__.py
    │   ├── creature.py
    │   └── explorer.py
    ├── test/: 테스트 코드
    │   ├── full/: End-to-end 또는 context 테스트라고도 하며 모든 계층에 걸쳐 한 번만 수행된다.
    │   └── unit/: 단일 기능을 실행하되 계층 경계를 넘지 않는다.
    │       ├── data/: 데이터 계층 단위 테스트
    │       ├── service/: 서비스 계층 단위 테스트
    │       └── web/: 웹 계층 단위 테스트
    └── web/: FastAPI 웹 계층
        ├── __init__.py
        ├── creature.py
        └── explorer.py
```

## 실행 방법

```bash
docker compose up
```

서버 실행 후 http://localhost:8000 접속

## API 문서

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 개발 환경

- 바인드 마운트를 통해 코드 변경사항이 즉시 반영됨
- `--reload` 옵션으로 파일 수정 시 자동 서버 재시작
- 컨테이너 접속: `docker exec -it fastapi-app bash`
