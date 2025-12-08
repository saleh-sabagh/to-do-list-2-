from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.deps import get_project_service
from app.schemas import (
    ProjectCreate,
    ProjectPartialUpdate,
    ProjectRead,
    ProjectUpdate,
    ProjectWithTasks,
    TaskCreate,
    TaskRead,
)
from app.services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get(
    "/",
    response_model=list[ProjectRead],
    summary="List projects",
    description="Return all projects with pagination.",
)
def list_projects(
    skip: int = Query(0, ge=0, description="Number of projects to skip"),
    limit: int = Query(100, ge=1, le=500, description="Maximum projects to return"),
    project_service: ProjectService = Depends(get_project_service),
) -> list[ProjectRead]:
    return project_service.get_all_projects(skip=skip, limit=limit)


@router.post(
    "/",
    response_model=ProjectWithTasks,
    status_code=status.HTTP_201_CREATED,
    summary="Create project",
    description="Create a new project with an optional description.",
)
def create_project(
    payload: ProjectCreate,
    project_service: ProjectService = Depends(get_project_service),
) -> ProjectWithTasks:
    project = project_service.create_project(name=payload.name, description=payload.description)
    project.tasks = []
    return project


@router.get(
    "/{project_id}",
    response_model=ProjectWithTasks,
    summary="Get project",
    description="Retrieve a single project by its ID.",
)
def get_project(
    project_id: int,
    project_service: ProjectService = Depends(get_project_service),
) -> ProjectWithTasks:
    try:
        project = project_service.get_project(project_id)
        project.tasks = project_service.list_tasks_for_project(project_id=project.id)
        return project
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put(
    "/{project_id}",
    response_model=ProjectWithTasks,
    summary="Replace project",
    description="Replace a project's name and description.",
)
def replace_project(
    project_id: int,
    payload: ProjectUpdate,
    project_service: ProjectService = Depends(get_project_service),
) -> ProjectWithTasks:
    try:
        project = project_service.update_project(
            project_id, name=payload.name, description=payload.description
        )
        project.tasks = project_service.list_tasks_for_project(project_id=project.id)
        return project
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch(
    "/{project_id}",
    response_model=ProjectWithTasks,
    summary="Update project",
    description="Partially update a project's fields.",
)
def patch_project(
    project_id: int,
    payload: ProjectPartialUpdate,
    project_service: ProjectService = Depends(get_project_service),
) -> ProjectWithTasks:
    try:
        data = payload.model_dump(exclude_unset=True)
        project = project_service.update_project(
            project_id,
            name=data.get("name"),
            description=data.get("description"),
        )
        project.tasks = project_service.list_tasks_for_project(project_id=project.id)
        return project
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete project",
    description="Delete a project and its tasks.",
)
def delete_project(
    project_id: int,
    project_service: ProjectService = Depends(get_project_service),
) -> None:
    try:
        project_service.delete_project(project_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get(
    "/{project_id}/tasks",
    response_model=list[TaskRead],
    summary="List tasks in a project",
    description="Return tasks for the given project.",
)
def list_project_tasks(
    project_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    project_service: ProjectService = Depends(get_project_service),
) -> list[TaskRead]:
    try:
        return project_service.list_tasks_for_project(project_id=project_id, skip=skip, limit=limit)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/{project_id}/tasks",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create task under project",
    description="Create a task for a specific project.",
)
def create_task_for_project(
    project_id: int,
    payload: TaskCreate,
    project_service: ProjectService = Depends(get_project_service),
) -> TaskRead:
    try:
        return project_service.add_task_to_project(
            project_id=project_id,
            title=payload.title,
            description=payload.description,
            deadline=payload.deadline,
            status=payload.status,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

