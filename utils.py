# utils.py
from datetime import datetime

activity_multipliers = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very active": 1.9
}

def calculate_bmr(sex, weight, height, birthdate):
    dob = datetime.fromisoformat(birthdate)
    age = (datetime.now() - dob).days // 365
    if sex.lower() in ("m", "male"):
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return bmr

def calculate_tdee(bmr, activity_level):
    multiplier = activity_multipliers.get(activity_level, 1.375)
    return bmr * multiplier

def calories_burned_by_exercise(met, weight, duration_min):
    return met * weight * (duration_min / 60.0)
