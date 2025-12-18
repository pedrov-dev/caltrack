# utils/calculations.py
import requests
import os

API_KEY = os.getenv("USDA_API_KEY")

def calculate_nutrition_usda(fdc_id: int, portion_grams: float):
    """Fetch nutrition info for a specific USDA food and portion size."""
    url = f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}?api_key={API_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        return None

    data = res.json()
    nutrients = {n["nutrientName"]: n["value"] for n in data.get("foodNutrients", [])}

    # Helper to extract safely
    def get(n):
        return nutrients.get(n, 0)

    scale = portion_grams / 100.0  # USDA data is per 100g
    return {
        "calories": get("Energy") * scale,
        "protein": get("Protein") * scale,
        "fat": get("Total lipid (fat)") * scale,
        "carbs": get("Carbohydrate, by difference") * scale,
    }
