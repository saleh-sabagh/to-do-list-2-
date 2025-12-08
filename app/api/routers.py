from fastapi import APIRouter

from app.api.controllers import projects_router, tasks_router

api_router = APIRouter()
api_router.include_router(projects_router)
api_router.include_router(tasks_router)

