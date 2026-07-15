from fastapi import FastAPI,  HTTPException

app = FastAPI()

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

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
    status_code=404,
    detail=f"Task {task_id} not found"
)