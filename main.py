import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.src.users.routers import router as router_users
from server.src.pages.router import router as router_pages
from server.src.game.routers.router_card import router as router_card
from server.src.game.routers.router_table import router as router_table

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
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)

app.include_router(router_users)
app.include_router(router_pages)
app.include_router(router_card)
app.include_router(router_table)


@app.get("/")
def hello():
    return "First start"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
