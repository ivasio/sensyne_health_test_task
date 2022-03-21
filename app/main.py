from fastapi import FastAPI

from api.routes import router
from api.db import database

app = FastAPI(
    description='A service for managing the blood glucose readings of diabetes patients',
    title='Blood Glucose Readings API',
    version='1.0.0',
)

app.include_router(router, prefix='/v1')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
