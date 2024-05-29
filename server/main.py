from fastapi import FastAPI

app = FastAPI(title="Poker")


@app.get("/")
def hello():
    return "First start"
