# 1. 최상위 디렉터리에 생성한 error.py 파일
class Missing(Exception):
    def __init__(self, msg: str):
        self.msg = msg

class Duplicate(Exception):
    def __init__(self, msg: str):
        self.msg = msg