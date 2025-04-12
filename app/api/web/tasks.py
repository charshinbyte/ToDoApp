from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskOut, TaskCreate
from app.service.todo import *

router = APIRouter(prefix='/tasks')

@router.get("/", response_model=list[TaskOut])
async def read_all():
    return await read_all_service()

@router.post("/", response_model=TaskOut)
async def create_task(task: TaskCreate):
    return await create_task_service(task)

@router.get("/{task_id}", response_model=TaskOut)
async def read_task(task_id: str):
    return await read_task_service(task_id)

@router.put("/update")
async def update_task(task_id: str, task: TaskCreate):
    return await update_task_service(task_id, task)

@router.delete("/delete")
async def delete_task(task_id: str):
    return await delete_task_service(task_id)

@router.delete("/purge")
async def purge():
    return await delete_all_service()

@router.put("/complete")
async def mark_complete(task_id : str):
    return await mark_task_service(task_id)