from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import initialize_database, get_connection

initialize_database()

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
def get_tasks(search: str | None = None):
    conn = get_connection()
    cursor = conn.cursor()

    if search:
        cursor.execute(
            "SELECT * FROM tasks WHERE title ILIKE %s",
            (f"%{search}%",)
        )
    else:
        cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    conn.close()

    return rows


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (task_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return row


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

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, done)
        VALUES (%s, %s)
        RETURNING id, title, done
        """,
        (task.title, False)
    )

    new_task = cursor.fetchone()

    conn.commit()
    conn.close()

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

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = %s, done = %s
        WHERE id = %s
        RETURNING id, title, done
        """,
        (
            updated_task.title,
            updated_task.done,
            task_id
        )
    )

    task = cursor.fetchone()

    if task is None:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    conn.commit()
    conn.close()

    return task


@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    summary="Delete a task",
    description="Deletes a task by its ID."
)
def delete_task(task_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(
            status_code=404,
            detail=f"Task {task_id} not found"
        )

    conn.commit()
    conn.close()

    return