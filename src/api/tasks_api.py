from typing import Annotated

from fastapi import APIRouter, Depends

from src.repository import TaskRepository
from src.schemas.tasks_schemas import TaskAddSchema, TaskSchema, TaskCreateShowSchema

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get('')
async def get_tasks() -> list[TaskSchema]:
    tasks = await TaskRepository().get_tasks()
    return tasks

@router.post('')
async def create_task(
        task: Annotated[TaskAddSchema, Depends()]
)-> TaskCreateShowSchema :
    task_id = await TaskRepository.add_task(task)
    return TaskCreateShowSchema(message='Task created', task_id=task_id)