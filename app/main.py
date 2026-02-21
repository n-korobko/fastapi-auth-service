from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine, Base
from app.routers import user


app = FastAPI()

app.include_router(user.router)

@app.get("/status")
async def status():
    return {"status": "ok"}

@app.get("/db-check")
async def db_check():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        return {"db_response": result.scalar()}
