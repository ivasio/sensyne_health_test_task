from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    description='A service for managing the blood glucose readings of diabetes patients',
    title='Blood Glucose Readings API',
    version='1.0.0',
)

app.include_router(router, prefix='/v1')
