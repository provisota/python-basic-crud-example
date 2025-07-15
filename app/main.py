from fastapi import FastAPI
from app.api.routers import router
from app.db.session import engine
from app.db.base import Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)
