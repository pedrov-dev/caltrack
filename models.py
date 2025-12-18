# models.py
from database import get_connection

def add_user(username, sex, birthdate, weight, height, activity):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""INSERT OR IGNORE INTO users 
                 (username, sex, birthdate, weight_kg, height_cm, activity_level)
                 VALUES (?, ?, ?, ?, ?, ?)""",
              (username, sex, birthdate, weight, height, activity))
    conn.commit()
    c.execute("SELECT id FROM users WHERE username=?", (username,))
    res = c.fetchone()
    conn.close()
    return res[0] if res else None

def get_user(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()
    return row

def add_food(user_id, entry_date, name, calories, protein, carbs, fat, portion):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""INSERT INTO food_entries 
                 (user_id, entry_date, food_name, calories, protein, carbs, fat, portion)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
              (user_id, entry_date, name, calories, protein, carbs, fat, portion))
    conn.commit()
    conn.close()

def add_exercise(user_id, entry_date, name, duration_min, met, calories_burned):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""INSERT INTO exercise_entries 
                 (user_id, entry_date, exercise_name, duration_min, met, calories_burned)
                 VALUES (?, ?, ?, ?, ?, ?)""",
              (user_id, entry_date, name, duration_min, met, calories_burned))
    conn.commit()
    conn.close()

def fetch_foods(user_id, d):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""SELECT food_name, calories, protein, carbs, fat, portion 
                 FROM food_entries WHERE user_id=? AND entry_date=?""", (user_id, d))
    rows = c.fetchall()
    conn.close()
    return rows

def fetch_exercises(user_id, d):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""SELECT exercise_name, duration_min, calories_burned 
                 FROM exercise_entries WHERE user_id=? AND entry_date=?""", (user_id, d))
    rows = c.fetchall()
    conn.close()
    return rows
