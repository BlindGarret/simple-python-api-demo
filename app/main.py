from dotenv import load_dotenv
from fastapi import FastAPI
from sqlmodel import SQLModel

from .db import engine
from .routers import echo, linkme

# Load env files
load_dotenv()

# Setup DB
SQLModel.metadata.create_all(engine.get_db_engine())

app = FastAPI()

# Register Routers
app.include_router(echo.router, prefix='/echo')
app.include_router(linkme.router, prefix='/links')
