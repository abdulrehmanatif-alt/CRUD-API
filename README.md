# Task API

A simple REST API built with FastAPI that allows users to create, read, update, and delete tasks. This project was developed as part of a backend internship assignment.

## Features

- Create tasks
- View all tasks
- View a single task by ID
- Update tasks
- Delete tasks
- Automatic Swagger API documentation
- Input validation
- Proper HTTP status codes

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Git

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd task-api
```

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{task_id} | Get task by ID |
| POST | /tasks | Create a task |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Example Request

POST /tasks

```json
{
    "title": "Complete assignment"
}
```

Example Response

```json
{
    "id": 4,
    "title": "Complete assignment",
    "done": false
}
```

## Project Structure

```
task-api/
│
├── .venv/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Author

Abdulrehman Atif