# Task API with FastAPI, PostgreSQL, SQLAlchemy & Alembic

## Overview

This project is a simple CRUD API built with **FastAPI** for managing tasks.

The application uses **PostgreSQL** for persistent data storage, **SQLAlchemy** as the ORM, **psycopg** as the PostgreSQL database driver, and **Alembic** for database migrations.

The API supports creating, reading, updating, searching, and deleting tasks.

## Technologies Used

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- psycopg
- Alembic
- Uvicorn
- Pydantic
- python-dotenv

## Architecture

```text
FastAPI
   |
   v
SQLAlchemy ORM
   |
   v
psycopg
   |
   v
PostgreSQL
   |
   ^
Alembic
(Database migrations)
```

## Project Structure

```text
CRUD API/
├── alembic/
│   ├── versions/
│   │   └── 33157c6a1971_create_tasks_table.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── .env
├── .gitignore
├── alembic.ini
├── database.py
├── main.py
├── models.py
├── requirements.txt
└── README.md
```

## Database Configuration

The application uses environment variables for the PostgreSQL connection.

Create a `.env` file in the project root:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=tasks
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
```

Replace the values with your local PostgreSQL configuration.

**Never commit `.env` to GitHub.**

The `.gitignore` file already excludes `.env`.

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd <repository-folder>
```

Create and activate a virtual environment:

### Windows

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Install the dependencies:

```cmd
pip install -r requirements.txt
```

## Database Setup

Make sure PostgreSQL is installed and running on your computer.

Create the PostgreSQL database specified in your `.env` file.

Then apply the Alembic migrations:

```cmd
alembic upgrade head
```

Check the current migration:

```cmd
alembic current
```

Check whether the database schema matches the SQLAlchemy models:

```cmd
alembic check
```

Expected result:

```text
No new upgrade operations detected.
```

## Running the API

Start the development server:

```cmd
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

## Database Migrations

Alembic is used to manage database schema changes.

Create a new migration after modifying the SQLAlchemy models:

```cmd
alembic revision --autogenerate -m "Describe your change"
```

Apply migrations:

```cmd
alembic upgrade head
```

Check the current migration:

```cmd
alembic current
```

Check for pending schema changes:

```cmd
alembic check
```

To view migration history:

```cmd
alembic history
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Get API information |
| GET | `/health` | Check API health |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks?search=term` | Search tasks by title |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Example Requests

### Create a task

```json
{
  "title": "Learn PostgreSQL"
}
```

### Update a task

```json
{
  "title": "Learn SQLAlchemy",
  "done": true
}
```

## Example SQL Query

```sql
SELECT * FROM tasks;
```

## Database Schema

The `tasks` table contains:

| Column | Type | Description |
|---|---|---|
| `id` | SERIAL | Primary key |
| `title` | TEXT | Task title |
| `done` | BOOLEAN | Task completion status |

## Development Notes

The application uses:

- **SQLAlchemy** for database interaction
- **psycopg** for PostgreSQL connectivity
- **Alembic** for database schema migrations
- **FastAPI** for the REST API


## Author

**Abdulrehman Atif**