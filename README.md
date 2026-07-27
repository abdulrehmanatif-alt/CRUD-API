# Task API with SQLite

## Overview

This project is a simple CRUD API built with **FastAPI**. It allows users to create, read, update, and delete tasks. The project uses **SQLite** as its database, so task data is stored permanently and remains available even after the server is restarted.

## Why SQLite?

SQLite was chosen because it is:

* Lightweight and easy to set up
* Serverless (no separate database server required)
* Included with Python through the built-in `sqlite3` module
* Perfect for small projects and learning backend development

## Technologies Used

* Python
* FastAPI
* SQLite
* sqlite3
* Uvicorn
* Pydantic

## Project Structure

```
task-api/
│
├── main.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
└── tasks.db (created automatically)
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd <repository-folder>
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Project

Start the server:

```bash
uvicorn main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

## Database

The application automatically creates a SQLite database named:

```
tasks.db
```

When the application runs for the first time:

* The database file is created automatically.
* The `tasks` table is created if it does not exist.
* Three sample tasks are inserted only if the table is empty.

## API Endpoints

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/tasks`      | Get all tasks     |
| GET    | `/tasks/{id}` | Get a task by ID  |
| POST   | `/tasks`      | Create a new task |
| PUT    | `/tasks/{id}` | Update a task     |
| DELETE | `/tasks/{id}` | Delete a task     |

## Example SQL Query

```sql
SELECT * FROM tasks;
```

## Author

Abdulrehman Atif
