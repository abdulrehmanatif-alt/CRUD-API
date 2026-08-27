import os

import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        row_factory=dict_row
    )


def initialize_database():
    conn = get_connection()

    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                done BOOLEAN NOT NULL
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM tasks")
        count = cursor.fetchone()["count"]

        if count == 0:
            sample_tasks = [
                ("Learn FastAPI", False),
                ("Build CRUD API", False),
                ("Learn PostgreSQL", False)
            ]

            cursor.executemany(
                "INSERT INTO tasks (title, done) VALUES (%s, %s)",
                sample_tasks
            )

    conn.commit()
    conn.close()