from fastapi import FastAPI

from .database import Base, engine
from . import models
from .routers import employees


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Employee Management API",
    description="CRUD API for employee record management",
    version="1.0.0"
)


app.include_router(employees.router)


@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }