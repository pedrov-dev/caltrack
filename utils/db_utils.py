# utils/db_utils.py
import sqlite3
import pandas as pd
from datetime import datetime
import os

DB_PATH = "data/local_db.sqlite3"
os.makedirs("data", exist_ok=True)

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS food_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        portion REAL,
        calories REAL,
        protein REAL,
        fat REAL,
        carbs REAL,
        date TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_food_log(name, portion, nutrition):
    conn = get_connection()
    conn.execute(
        "INSERT INTO food_log (name, portion, calories, protein, fat, carbs, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, portion, nutrition["calories"], nutrition["protein"], nutrition["fat"], nutrition["carbs"], datetime.now().strftime("%Y-%m-%d")),
    )
    conn.commit()
    conn.close()

def get_recent_food_logs(limit=10):
    conn = get_connection()
    df = pd.read_sql_query(f"SELECT * FROM food_log ORDER BY id DESC LIMIT {limit}", conn)
    conn.close()
    return df

