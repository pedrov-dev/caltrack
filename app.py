# app.py
import streamlit as st
from utils.db_utils import init_db

st.set_page_config(page_title="Calorie Tracker", page_icon="🍎", layout="wide")

# Initialize DB
init_db()

st.title("🍎 Calorie Tracker")

st.sidebar.success("Select a page above to get started.")

st.markdown("""
### Welcome to your Calorie Tracker!

Use this app to:
- Log your daily meals and see calorie & macro breakdowns.
- Track progress over time.
- Stay accountable toward your fitness goals.
""")
