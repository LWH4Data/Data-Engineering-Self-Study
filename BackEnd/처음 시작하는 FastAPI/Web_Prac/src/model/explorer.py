# 1. 탐험가 모델 정의 (model/explorer.py)
#   - 계층 간에 전달할 기본적인 데이터를 정의한다.
#   - 이후에 데이터가 추가될 수 있지만 현재는 기본 스키마로 구성한다.
from pydantic import BaseModel

class Explorer(BaseModel):
    name: str
    country: str
    description: str = ""