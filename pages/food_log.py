# pages/food_log.py
import streamlit as st
from components.nutrition_api import search_food
from utils.db_utils import save_food_log, get_recent_food_logs
from utils.calculations import calculate_nutrition_usda

st.title("🍽️ Log Your Food")

query = st.text_input("Search for a food (e.g., chicken, rice, apple)")

if query:
    results = search_food(query)
    if results:
        st.write("### Results:")
        for food in results:
            with st.container():
                cols = st.columns([3, 2])
                with cols[0]:
                    st.subheader(food["name"])
                    if food["brand"]:
                        st.caption(food["brand"])
                with cols[1]:
                    portion = st.slider(
                        f"Portion (grams) for {food['name']}",
                        50, 500, 100, 10,
                        key=f"portion_{food['fdcId']}"
                    )
                    if st.button(f"Add {food['name']}", key=f"add_{food['fdcId']}"):
                        nutrition = calculate_nutrition_usda(food["fdcId"], portion)
                        if nutrition:
                            save_food_log(food["name"], portion, nutrition)
                            st.success(f"✅ Added {food['name']} ({portion}g)")
                        else:
                            st.error("⚠️ Unable to fetch nutrition info. Try again.")
    else:
        st.warning("No foods found. Try another search.")

# Show recent logs
st.divider()
st.write("### Recent Foods Logged")
logs = get_recent_food_logs(limit=10)
if not logs.empty:
    st.dataframe(logs)
else:
    st.info("No foods logged yet.")
