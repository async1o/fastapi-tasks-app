from fastapi import APIRouter
from src.api.tasks_api import router as tasks_router

main_router = APIRouter()

main_router.include_router(tasks_router)