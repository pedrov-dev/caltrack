# database.py
import sqlite3
import json

DB_PATH = "caltrack.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        sex TEXT,
        birthdate TEXT,
        weight_kg REAL,
        height_cm REAL,
        activity_level TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS food_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        entry_date TEXT,
        food_name TEXT,
        calories REAL,
        protein REAL,
        carbs REAL,
        fat REAL,
        portion TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS exercise_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        entry_date TEXT,
        exercise_name TEXT,
        duration_min REAL,
        met REAL,
        calories_burned REAL
    )""")
    conn.commit()
    conn.close()


DB_PATH = "calories.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS food_cache (
            query TEXT PRIMARY KEY,
            results_json TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def cache_food_results(query, results):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO food_cache (query, results_json)
        VALUES (?, ?)
    """, (query.lower(), json.dumps(results)))
    conn.commit()
    conn.close()

def fetch_cached_results(query):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT results_json FROM food_cache WHERE query = ?", (query.lower(),))
    row = c.fetchone()
    conn.close()
    return json.loads(row[0]) if row else None

