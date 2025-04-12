from app.models.task import Task, TaskOut, TaskCreate    
from app.db.crud import create_task as create_task_crud
from app.db.crud import read_all as read_all_crud
from app.db.crud import read_task as read_task_crud
from app.db.crud import update_task as update_task_crud
from app.db.crud import delete_task as delete_task_crud
from app.db.crud import delete_all as delete_all_crud
from app.db.crud import mark_task as mark_task_crud

from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

async def create_task_service(task: TaskCreate) -> TaskOut:
    try:
        inserted_task = await create_task_crud(task)
        return TaskOut(**inserted_task.model_dump()) 
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not create task: {str(e)}")
    
async def read_all_service() -> list[TaskOut]:
    try:
        tasks = await read_all_crud()
        return tasks
    
    except Exception as e:
        logger.exception("Unexpected error while handling data")
        raise HTTPException(status_code=500, detail="Internal server error")

async def read_task_service(task_id : str) -> TaskOut:
    try:
        tasks = await read_task_crud(task_id)
        return tasks
    except Exception as e:
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

async def update_task_service(task_id : str, updated_task : TaskCreate) -> TaskOut :
    try: 
        updated_task = await update_task_crud(task_id, updated_task)
        return updated_task
    except Exception as e:
        raise HTTPException(status_code = 500, detail="Internal Server Error")
    
async def delete_task_service(task_id : str) -> TaskOut :
    try: 
        deleted_task = await delete_task_crud(task_id)
        return deleted_task
    except Exception as e:
        raise HTTPException(status_code = 500, detail="Internal Server Error")
    
async def delete_all_service() -> int :
    try: 
        deleted_items = await delete_all_crud()
        return deleted_items
    except Exception as e:
        raise HTTPException(status_code = 500, detail="Internal Server Error")
    
async def mark_task_service(task_id : str) -> TaskOut :
    try: 
        completed_item = await mark_task_crud(task_id)
        return completed_item
    except Exception as e:
        raise HTTPException(status_code = 500, detail="Internal Server Error")