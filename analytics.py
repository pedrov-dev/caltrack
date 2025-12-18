# analytics.py
import pandas as pd
from models import fetch_foods, fetch_exercises

def get_daily_summary(user_id, start_date, end_date):
    """Aggregate calories and macros between two dates."""
    days = pd.date_range(start_date, end_date)
    data = []
    for d in days:
        foods = fetch_foods(user_id, d.date().isoformat())
        exs = fetch_exercises(user_id, d.date().isoformat())

        if foods:
            df_food = pd.DataFrame(foods, columns=["Food", "Calories", "Protein", "Carbs", "Fat", "Portion"])
            total_cal = df_food["Calories"].sum()
            total_protein = df_food["Protein"].sum()
            total_carbs = df_food["Carbs"].sum()
            total_fat = df_food["Fat"].sum()
        else:
            total_cal = total_protein = total_carbs = total_fat = 0

        if exs:
            df_ex = pd.DataFrame(exs, columns=["Exercise", "Duration", "Calories Burned"])
            burned = df_ex["Calories Burned"].sum()
        else:
            burned = 0

        data.append({
            "date": d.date(),
            "calories_in": total_cal,
            "calories_out": burned,
            "net": total_cal - burned,
            "protein": total_protein,
            "carbs": total_carbs,
            "fat": total_fat
        })

    df = pd.DataFrame(data)
    return df
