from app.models.task import Task, TaskOut, TaskCreate
from app.config import collection
from bson import ObjectId

# Create
async def create_task(new_task: TaskCreate) -> TaskOut:
    task = Task(**new_task.model_dump()) #.dict() as it is deprecated
    task_dict = task.model_dump() 
    result = await collection.insert_one(task_dict)
    return TaskOut(id=str(result.inserted_id), **task_dict)

# Read All Tasks (excluding soft-deleted)
async def read_all() -> list[TaskOut]:
    tasks = []
    cursor = collection.find({"is_deleted" : False})  # Filter out soft-deleted tasks
    async for doc in cursor:
        tasks.append(TaskOut(
            id=str(doc["_id"]),
            title=doc["title"],
            is_completed=doc["is_completed"],
            is_deleted=doc["is_deleted"],
            updated_at=doc["updated_at"],
            creation=doc["creation"]
        ))
    return tasks

# Read One Task
async def read_task(task_id: str) -> TaskOut:
    id = ObjectId(task_id)
    result = await collection.find_one({"_id" : id})
    return TaskOut(id=str(id), **result)

# Update Task
async def update_task(task_id : str, updated_task : TaskCreate) -> TaskOut:
    id = ObjectId(task_id)
    result = await collection.find_one_and_update({"_id" : id }, {"$set" : updated_task.model_dump()})
    return TaskOut(id=str(id), **result)

# Delete Task (Soft Delete)
async def delete_task(task_id : str) -> TaskOut:
    id = ObjectId(task_id)
    result = await collection.find_one_and_update({"_id" : id }, {"$set" : {"is_deleted": True}}, return_document=True)
    return TaskOut(id=str(id), **result)

# Hard delete all soft-deleted tasks
async def delete_all() -> int:
    result = await collection.delete_many({"is_deleted": True})
    return result.deleted_count

async def mark_task(task_id: str) -> TaskOut:
    id = ObjectId(task_id)
    result = await collection.find_one_and_update({"_id": id}, {"$set" : {"is_completed": True}}, return_document=True)
    return TaskOut(id=str(id), **result)