

from sqlalchemy import select

from src.databases.database import new_session
from src.models.models import TaskORM
from src.schemas.tasks_schemas import TaskAddSchema, TaskSchema


class TaskRepository():
    @classmethod
    async def add_task(cls, data: TaskAddSchema) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskORM(**task_dict)

            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[TaskSchema]:
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            #task_schemas = [TaskSchema.model_validate(task_model) for task_model in task_models]
            return task_models