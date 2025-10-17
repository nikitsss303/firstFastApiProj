from fastapi import FastAPI

from app.routers.api import router as api_router
from app.config.database import Base, engine



app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(api_router)