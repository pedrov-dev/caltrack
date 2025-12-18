# charts.py
import plotly.express as px

def calorie_trend_chart(df):
    fig = px.line(
        df,
        x="date",
        y=["calories_in", "calories_out", "net"],
        labels={"value": "Calories", "date": "Date"},
        title="Calories Consumed vs Burned (Weekly Trend)",
        markers=True
    )
    return fig

def macro_breakdown_chart(df):
    avg_prot = df["protein"].mean()
    avg_carbs = df["carbs"].mean()
    avg_fat = df["fat"].mean()
    fig = px.pie(
        names=["Protein", "Carbs", "Fat"],
        values=[avg_prot, avg_carbs, avg_fat],
        title="Average Macro Distribution"
    )
    return fig
