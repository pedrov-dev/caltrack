# components/nutrition_api.py
import requests
import os

API_KEY = os.getenv("USDA_API_KEY")
BASE_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def search_food(query: str, limit=5):
    """Search for foods from USDA FoodData Central."""
    if not query:
        return []
    params = {
        "api_key": API_KEY,
        "query": query,
        "pageSize": limit,
        "dataType": ["Foundation", "Survey (FNDDS)"],  # clean datasets
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return []

    foods = response.json().get("foods", [])
    results = []
    for food in foods:
        results.append({
            "name": food["description"].title(),
            "fdcId": food["fdcId"],
            "brand": food.get("brandOwner", ""),
            "serving_unit": "100g",
            "photo": None,  # USDA has no images
        })
    return results
