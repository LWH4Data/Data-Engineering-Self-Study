# Data Pipelines with Apache Airflow 로 학습

# 1. 실행 docker 코드

```bash
docker run -it --name airflow -p 8080:8080 \
  -v /mnt/c/Users/SSAFY/Desktop/Airflow-prac:/opt/airflow/dags \
  --entrypoint /bin/bash \
  apache/airflow:2.0.0-python3.8 \
  -c 'airflow db init && \
      airflow users create \
        --username admin \
        --password admin \
        --firstname Anonymous \
        --lastname Admin \
        --role Admin \
        --email admin@example.org ; \
      airflow webserver -p 8080 & \
      airflow scheduler'
```