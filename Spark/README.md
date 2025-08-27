- < 스파크 완벽 가이드 > 도서를 통해 학습한 것을 정리.
- 도서의 버전이 낮기에 실습 코드는 최신 버전으로 리팩토링 필요.

# 1. 도커로 접근
```bash
# 현재는 단순 명령엉로 접근하여 실습.
docker run --rm -it apache/spark:3.5.2 /opt/spark/bin/pyspark
```

<br><br>

# 2. Job, Stage, Task
## 2-1. Job
- Action 1회 호출로 만들어지는 최상위 실행 단위이다(일반적으로 1개 생성).
- **Structured Streaming에서는** Trigger 1회 = Job 1개.
- 잡 내부에 셔플이 있으면 스테이지가 여러 개로 나뉜다.

## 2-2. Stage: Shuffle 사이의 구간
- 셔플이 없는 연산들을 한 덩어리로 묶은 단위이다.
- 셔플 경계에서 스테이지가 끊긴다. (예: `groupBy/agg`, `join`, `orderBy/sort`, `repartition`)

## 2-3. Task: Stage의 병렬 처리 단위
- 스테이지 안에서 **파티션 하나를 처리하는 최소 실행 조각**이다.
- **해당 스테이지의 Task 수 = 그 시점의 파티션 수**(입력 파티션 또는 `spark.sql.shuffle.partitions`에 의해 결정).
