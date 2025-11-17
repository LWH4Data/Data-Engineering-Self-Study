# 2. 생명체 모델 정의 (model/creature.py)
#   - 마찬가지로 계층 간에 전달할 기본적인 데이터를 정의한다.
from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str