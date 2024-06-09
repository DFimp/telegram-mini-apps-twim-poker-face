import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.src.database import get_async_session
from server.src.game.models.TableUsers import TableUsers
from server.src.game.services.services_table_users import (
    join_user_to_the_table,
    disconnection_user_from_table,
)

router = APIRouter(prefix="/table", tags=["Table"])


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws/{user_id}/{table_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    user_id: int,
    table_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    await manager.connect(websocket)

    query = select(TableUsers).filter_by(user_id=user_id, table_id=table_id)
    result = await session.execute(query)
    user = result.scalars().first()

    if user:
        await websocket.send_text(json.dumps({"action": "status", "status": "joined"}))
    else:
        await websocket.send_text(
            json.dumps({"action": "status", "status": "not_joined"})
        )
        print(True)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            action = message.get("action")
            if action == "join":
                await join_user_to_the_table(user_id, table_id, session)
                await manager.broadcast(f"User {user_id} joined the table.")
                await websocket.send_text(
                    json.dumps({"action": "status", "status": "joined"})
                )
            elif action == "leave":
                await disconnection_user_from_table(user_id, table_id, session)
                await manager.broadcast(f"User {user_id} left the table.")
                await websocket.send_text(
                    json.dumps({"action": "status", "status": "not_joined"})
                )
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"User #{user_id} disconnected")
