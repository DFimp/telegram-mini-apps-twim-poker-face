import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from server.src.users.router import router as router_users


app = FastAPI(title="Poker")

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_users)


@app.get("/")
def hello():
    return "First start"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
