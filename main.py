from fastapi import FastAPI,  HTTPException
from pydantic import BaseModel

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

tasks = [
    {
        "id": 1,
        "title": "Complete Python assignment",
        "done": False
    },
    {
        "id": 2,
        "title": "Study FastAPI",
        "done": True
    },
    {
        "id": 3,
        "title": "Push project to GitHub",
        "done": False
    }
]

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

@app.get(
    "/tasks",
    summary="Get all tasks",
    description="Returns a list of all tasks."
)
def get_tasks():
    return tasks

@app.get(
    "/tasks/{task_id}",
    summary="Get a task by ID",
    description="Returns a single task using its ID."
)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
    status_code=404,
    detail=f"Task {task_id} not found"
)

@app.post(
    "/tasks",
    status_code=201,
    summary="Create a new task",
    description="Creates a new task with a title."
)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty."
        )

    new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates the title and completion status of a task."
)
def update_task(task_id: int, updated_task: TaskUpdate):

    if not updated_task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty."
        )

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["done"] = updated_task.done
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    summary="Delete a task",
    description="Deletes a task by its ID."
)
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )