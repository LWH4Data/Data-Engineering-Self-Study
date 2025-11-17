# 2. main.py에 엔드포인트 추가.
from fastapi import FastAPI
from .web import explorer, creature

app = FastAPI()
@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def echo(thing):
    return f"echoing {thing}"

app.include_router(explorer.router)
app.include_router(creature.router)