from fastapi import FastAPI, HTTPException
from app.models.task import Task, TaskOut
from app.service.todo import *
from app.api.web import tasks 

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(tasks.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Or replace "*" with the exact origin (e.g., ["http://localhost:5500"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
