import uvicorn
from fastapi import FastAPI, Depends

from server.src.users.router import router as router_users

app = FastAPI(title="Poker")

app.include_router(router_users)


@app.get("/")
def hello():
    return "First start"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
