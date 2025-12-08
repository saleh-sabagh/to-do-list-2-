from fastapi import APIRouter, Depends, HTTPException, Query, status

from app.api.deps import get_task_service
from app.schemas import TaskPartialUpdate, TaskRead, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/",
    response_model=list[TaskRead],
    summary="List tasks",
    description="Return all tasks across projects.",
)
def list_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    task_service: TaskService = Depends(get_task_service),
) -> list[TaskRead]:
    return task_service.get_all_tasks(skip=skip, limit=limit)


@router.get(
    "/{task_id}",
    response_model=TaskRead,
    summary="Get task",
    description="Retrieve a task by its ID.",
)
def get_task(
    task_id: int,
    task_service: TaskService = Depends(get_task_service),
) -> TaskRead:
    try:
        return task_service.get_task(task_id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put(
    "/{task_id}",
    response_model=TaskRead,
    summary="Replace task",
    description="Replace all fields of a task.",
)
def replace_task(
    task_id: int,
    payload: TaskUpdate,
    task_service: TaskService = Depends(get_task_service),
) -> TaskRead:
    try:
        return task_service.update_task(
            task_id=task_id,
            title=payload.title,
            description=payload.description,
            deadline=payload.deadline,
            status=payload.status,
            title_provided=True,
            description_provided=True,
            deadline_provided=True,
            status_provided=True,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.patch(
    "/{task_id}",
    response_model=TaskRead,
    summary="Update task",
    description="Partially update a task.",
)
def update_task(
    task_id: int,
    payload: TaskPartialUpdate,
    task_service: TaskService = Depends(get_task_service),
) -> TaskRead:
    try:
        data = payload.model_dump(exclude_unset=True)
        return task_service.update_task(
            task_id=task_id,
            title=data.get("title"),
            description=data.get("description"),
            deadline=data.get("deadline"),
            status=data.get("status"),
            title_provided="title" in data,
            description_provided="description" in data,
            deadline_provided="deadline" in data,
            status_provided="status" in data,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete task",
    description="Delete a task by ID.",
)
def delete_task(
    task_id: int,
    task_service: TaskService = Depends(get_task_service),
) -> None:
    task_service.delete_task(task_id)

