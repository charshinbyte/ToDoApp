import pytest
import asyncio
from bson import ObjectId
from app.models.task import Task, TaskOut
from app.db import crud
from datetime import datetime 

def mock_timestamp():
    return int(datetime.now().timestamp())


# Simulates reading read_all functionality from mongodb
@pytest.mark.asyncio
async def test_read_all(monkeypatch):
    mock_data = [
            {
                "_id": ObjectId(),
                "title": "Task 1",
                "description": "Desc 1",
                "is_completed": False,
                "is_deleted": False,
                "updated_at": mock_timestamp(),
                "creation": mock_timestamp()
            },
            {
                "_id": ObjectId(),
                "title": "Task 2",
                "description": "Desc 2",
                "is_completed": False,
                "is_deleted": False,
                "updated_at": mock_timestamp(),
                "creation": mock_timestamp()
            }
        ]
    
    class MockCursor:
        def __init__(self, docs):
            self.docs = docs

        def __aiter__(self):
            self._iter = iter(self.docs)
            return self

        async def __anext__(self):
            try:
                return next(self._iter)
            except StopIteration:
                raise StopAsyncIteration

    def mock_find(filter):
        return MockCursor(mock_data)

    monkeypatch.setattr(crud.collection, "find", mock_find)

    results = await crud.read_all()

    assert len(results) == 2
    assert all(isinstance(task, TaskOut) for task in results)


