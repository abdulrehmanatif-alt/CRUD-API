from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Task


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task API",
    description="A simple CRUD API built with FastAPI for managing tasks.",
    version="1.0.0"
)


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


@app.get(
    "/",
    summary="Get API information",
    description="Returns basic information about the Task API."
)
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get(
    "/health",
    summary="Health check",
    description="Checks whether the API server is running."
)
def health():
    return {
        "status": "ok"
    }


@app.get("/tasks")
def get_tasks(
    search: str | None = None,
    db: Session = Depends(get_db)
):
    statement = select(Task)

    if search:
        statement = statement.where(Task.title.ilike(f"%{search}%"))

    tasks = db.scalars(statement).all()

    return tasks


@app.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.post(
    "/tasks",
    status_code=201,
    summary="Create a new task",
    description="Creates a new task with a title."
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty."
        )

    new_task = Task(
        title=task.title,
        done=False
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates the title and completion status of a task."
)
def update_task(
    task_id: int,
    updated_task: TaskUpdate,
    db: Session = Depends(get_db)
):
    if not updated_task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty."
        )

    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    task.title = updated_task.title
    task.done = updated_task.done

    db.commit()
    db.refresh(task)

    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    summary="Delete a task",
    description="Deletes a task by its ID."
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    db.delete(task)
    db.commit()

    return