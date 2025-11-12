<ul>
  <li>
    <strong>Pydantic</strong>은 파이썬 <strong>타입 힌트</strong>를 사용한 <strong>데이터 유효성 검사</strong>와 <strong>설정 관리</strong>를 한다.
  </li>
  <li>
    Pydantic 패키지는 파이썬 객체 클래스인 <strong>models</strong>로 <strong>데이터 구조</strong>를 정의한다.
  </li>
</ul>

<br>

<h1>1. 타입 힌트</h1>
<ul>
  <li>
    대부분의 컴퓨터 언어에서는 타입을 선언하지만 파이썬은 <strong>타입을 선언하지 않는다</strong>.
  </li>
  <li>
    파이썬에서는 <strong>타입 힌트</strong>를 통해 타입을 관리한다. 단, 프로그램을 실행할 때에는 타입 힌트 구문을 <strong>무시하고 존재하지 않는 것처럼 동작</strong>한다.
  </li>
    <ul>
      <li>
        단, <strong>mypy</strong>와 같은 보조 도구를 넣으면 타입 힌트가 불일치할 시 <strong>경고</strong>를 표시한다.
      </li>
    </ul>
  <li>
    개발자 입장에서는 파이썬에서 데이터 타입을 확인할 수 있기에 편리하다.
  </li>
  <li>
    파이썬에서 <strong>튜플, 리스트, 딕셔너리</strong> 등의 자료 구조에 타입 힌트를 사용할 경우 <strong>타이핑(typing) 모듈</strong>을 이용해 표준 타입 이름을 대문자 형태로 가져와야 한다.
  </li>
  <li>
    <strong>함수 반환값</strong>에 대해서는 콜론(:) 대신 <strong>화살표(->)</strong>를 사용한다.
  </li>
</ul>

```python
# 1. 각종 타입 힌트

# 타입 힌트
name: type

# 타입 힌트를 줌과 동시에 초기화
name: type = value

# str 초기화
thing: str = "yeti"
```

```python
# 2. typing 모듈 예
from typing import Tuple, List, Dict

tuple_things: Tuple = ("yeti", "bigfoot")
list_things: List = ["yeti", "bigfoot"]
dict_things: Dict = {"mountain": "yeti", "forest": "bigfoot"}
```

```python
# 3. 초기화의 몇 가지 예
physics.magic_number: float = 1.0/137.03599913
hp_lovecraft_noun: str = "ichor"
exploding_sheep: tuple = "sis", "boom", "bahi!"
responses: dict = {"Marco": "Polo", "answer": 42}

# 컬렉션의 하위 타입
#   - Any: 모든 타입
#   - Union: Union[str, int]와 같이 지정된 모든 타입
#     - python 3.10 이상부터는 type1 | type2 형태로 작성한다.
name: dict[keytype, valtype] = {key1: val1, key2: val2}

# 일반 하위 타입
from typing import Any
responses: dict[str, Any] = {"Marco": "Polo", "answer": 42}

# Union을 사용한 예
from typing import Union
responses: dict[str, Union[str, int]] = {"Marco": "Polo", "answer": 42}

# python 3.10 이상 Union 예
reponses: dict[str, str | int] = {"Marco": "Polo", "answer": 42}
```

<br><br>

<h1>2. 데이터 그룹화</h1>
<ul>
  <li>
    변수를 그룹으로 묶어 <strong>함께 유지</strong>해야하는 경우 이를 <strong>통합</strong>하고 <strong>타입 힌트로 유지</strong>하는 방법에 대해 설명한다.
  </li>
  <li>
    파이썬에는 다른 언어의 레코드(record) 혹은 구조체(struct)에 해당하는 <strong>데이터클래스(dataclass)</strong>가 있다.
  </li>
  <li>
    변수와 관련된 요구사항 확인 항목들에는 다음과 같은 것들이 있다.
  </li>
    <ul>
      <li>
        가능한 대체 타입의 집합
      </li>
      <li>
        누락된 값이나 선택적 값 적용
      </li>
      <li>
        기본값 설정
      </li>
      <li>
        데이터 유효성 검사
      </li>
      <li>
        JSON과 같은 형식으로 직렬화 또는 역직렬화
      </li>
    </ul>
</ul>

```python
# 1. 튜플 사용
tuple_thing = ("yeti", "CN", "Himalayas", "Hirsute Himalayan", 
            "Abominable Snowman")

print("Name is", tuple_thing[0])
```

```python
# 2. 리스트 사용
list_thing = ["yeti", "CN", "Himalayas", "Hirsute Himalayhan",
            "Abominable Snowman"]

print("Name is", list_thing[0])
```

```python
# 3. 튜플을 사용하되 인덱스가 아닌 이름을 통한 위치값 사용.
NAME = 0
COUNTRY = 1
AREA = 2
DESCRIPTION = 3
AKA = 4
tuple_thing = ("yeti", "CN", "Himalayas", 
            "Hirsute Himalayan", "Abominable Snowman")
print("Name is", tuple_thing[NAME])
```

```python
# 4. 딕셔너리 사용.
dict_thing = {"name": "yeti",
    "country": "CN",
    "area": "Himalayas",
    "description": "Hirsute Hiamlayan",
    "aka": "Abominable Snowman"}

print("Name is", dict_thing["name"])
```

```python
# 5. 네임드 튜플 (named tu)
#   - 정수 오프셋 혹은 이름으로 접근한다.
from collections import namedtuple
CreatureNamedTuple = namedtuple("CreatureNamedTuple",
    "name, country, area, description, aka")

namedtuple_thing = CreatureNamedTuple("yeti",
    "CN",
    "Himalaya",
    "Hirsute Himalayan",
    "Abominable Snowman")

# 딕셔너리가 아닌 tuple이기에 ["name"]과 같은 형태 불가능.
print("Name is", namedtuple_thing[0])
print("Name is", namedtuple_thing.name)
```

```python
# 6. 새 파이썬 클래스를 정의하고 모든 어트리뷰트를 self로 추가.
#   - 일반 클래스를 사용하면 더 많은 데이터를 비롯해 메서드를 추가할 수 있다.
class CreatureClass():
    
    def __init__(self,
        name: str,
        country: str,
        area: str,
        description: str,
        aka: str):

        self.name = name
        self.country = country
        self.area = area
        self.description = description
        self.aka = aka

class.thing = CreatureClass(
    "yeti",
    "CN",
    "Himalayas",
    "Hirsute Himalayan",
    "Abominable Snowman")

print({"Name is", class_thing.name})
```

```python
# 7. 데이터 클래스 활용
#   - 데이터 클래스를 사용하면 self 관련 사항이 사라진다.
from dataclasses import dataclass

@dataclass
class CreatureDataClass():
    name: str
    country: str
    area: str
    description: str
    aka: str

dataclass.thing = CreatureDataClass(
    "yeti",
    "CN",
    "Himalayas",
    "Hirsute Himalayan",
    "Abominable Snowman")

print("Name is", dataclass_thing.name)
```

<br><br>

<h1>3. 대안</h1>
<ul>
  <li>
    파이썬의 내장 데이터 구조, 특히 딕셔너리를 사용하고 싶을 수 있지만 딕셔너리는 느슨하기에 <strong>모든 것</strong>을 확인해야 한다.
  </li>
    <ul>
      <li>
        키는 선택 사항인가?
      </li>
      <li>
        키가 누락된 경우 기본값이 있는가?
      </li>
      <li>
        키가 존재하는가?
      </li>
      <li>
        키의 값이 올바른 타입인가?
      </li>
      <li>
        값이 올바른 스코프에 있거나 패턴과 일치하는가?
      </li>
    </ul>
  <li>
    위의 요구사항을 해결하는 라이브러리는 대표적으로 세 가지가 있다.
  </li>
    <ul>
      <li>
        Dataclasses (https://oreil.ly/mxANA): 파이썬의 일부
      </li>
      <li>
        attrs (https:/www.attrs.org): 서드파티 라이브러리지만 데이터클래스의 상위 호환이다.
      </li>
      <li>
        <strong>Pydantic (https://docs.pydantic.dev)</strong>: 서드파티 라이브러리지만 FastAPI에 통합돼 <strong>FastAPI를 사용한다면 좋은 선택지</strong>이다.
      </li>
    </ul>
  <li>
    <strong>Pydantic</strong>은 <strong>상속(BaseModel 클래스를 상속)</strong>에 의존하는 반면 나머지 두 개는 파이썬 데코레이터(decorator)를 사용해 객체를 정의한다.
  </li>
  <li>
    Pydantic은 <strong>표준 파이썬 타입 힌트 구문</strong>을 사용한다.
  </li>
  <li>
    Pydantic은 아래 조건들을 결합하는 방법을 제공한다.
  </li>
    <ul>
      <li>
        필수 사항과 선택 사항
      </li>
      <li>
        지정되지 않았지만 필요한 경우 기본값
      </li>
      <li>
        예상되는 하나 이상의 데이터 타입
      </li>
      <li>
        값 범위 제한
      </li>
      <li>
        필요한 경우 기타 기능 기반 검사
      </li>
      <li>
        직렬화와 역직렬화
      </li>
    </ul>
</ul>

<br>4. 간단한 예<br>
<ul>
  <li>
    문자열 외에도 다양한 타입의 데이터 묶음을 주고받는 기능을 Pydantic을 활용하여 구현한다.
  </li>
  <li>
    Pydantic은 타입 설명에 <strong>Optional</strong>이 없다면 필드에 <strong>값이 필수적</strong>으로 있어야 한다.
  </li>
</ul>

```python
# 1. model.py
#   - 생명체 모델 정의
from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

thing = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hersute Himalayan",
    aka="Abominable Snowman"
)

print("Name is", thing.name)
```

```python
# 2. data.py
#   - 가짜 데이터 정의
from model import Creature

# _creatures: Creature 객체를 여러 개 담은 리스트
_creatures: list[Creature] = [
    Creature(name="yeti",
            country="CN",
            area="Himalayas",
            description="Hirsute Himalayan",
            aka="Abominable Snowman"
            ),
    Creature(name="sasquatch",
            country="US",
            area="*",
            description="Yeti's Cousin Eddie",
            aka="Bigfoot")
]

# 데이터 은닉화
# 데이터를 모듈 내부(_creatures)에 숨기고,
# 외부에서는 get_creatures() 함수를 통해서만 접근하도록 함
def get_creatures() -> list[Creature]:
    return _creatures
```

```python
# 3. web.py
#   - FastAPI 웹 엔드포인트 정의.
from model import Creature
from fastapi import FastAPI

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()
```

<br><br>

<h1>5. 타입 유효성 검사</h1>
<ul>
  <li>
    내용 정리
  </li>
    <ul>
      <li>
        변수 및 함수에 타입 힌트 적용
      </li>
      <li>
        Pydantic 모델 정의 및 사용
      </li>
      <li>
        데이터 소스에서 모델 리스트 반환
      </li>
      <li>
        모델 리스트를 웹 클라이언트에 반환해 모델 리스트를 JSON으로 자동 변환
      </li>
    </ul>
</ul>

```python
# 1. 하나 이상의 Creature 필드에 잘못된 데이터 타입을 할당하여 유효성 검사.
#   - Pydantic에 의해 오류가 나야 한다.
from model import Creature

dragon = Creature(
    name="dragon",
    description=["incorrect", "string", "list"],
    country="*",
    area="*",
    aka="firedrake"
)

# 실행을 하면 description 필드가 문자열이 아니기에 오류가 발생한다.
```

<br><br>

<h1>6. 값 유효성 검사</h1>
<ul>
  <li>
    값의 타입 뿐만아니라 각 타입마다 몇 가지 <strong>제한을 추가</strong>할 수 있으며 해당 제한 또한 통과를 해야한다.
  </li>
</ul>

```python
# 1. 제한을 추가하여 유효성 검사를 한다.
from pydantic import BaseModel, constr

class Creature(BaseModel):
    # constr을 통해 두 글자 이상이어야 한다는 제한을 추가한다.
    name: constr(min_length=2)
    country: str
    area: str
    description: str
    aka: str

# name이 "!"로 길이가 1이기에 오류를 반환한다.
bad_creature = Creature(name="!",
    description="it's a raccoon",
    area="your attic")
```

```python
# 2. Field를 활용한 또 다른 유효성 검사.
from pydantic import BaseModel, Field

class Creature(BaseModel):
    # ...: 인수는 값이 필요하며 기본값이 없음을 의미한다.
    name: str = Field(..., min_length=2)
    country: str
    area: str
    description: str
    aka: str

bad_creature = Creature(name="!",
    area="your attic",
    description="it's a raccoon")

# 마찬가지로 name의 길이가 1이기에 오류를 반환한다.
```