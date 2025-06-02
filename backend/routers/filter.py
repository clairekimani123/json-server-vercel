from fastapi import APIRouter, Query
from typing import List
import requests

router = APIRouter()

SPOONACULAR_API_KEY = "your_api_key"

@router.get("/filtered-recipes")
def get_filtered_recipes(required_ingredients: List[str] = Query([])):
    response = requests.get(
        f"https://api.spoonacular.com/recipes/random",
        params={
            "number": 40,
            "apiKey": SPOONACULAR_API_KEY
        }
    )
    recipes = response.json().get("recipes", [])

    filtered = []
    for recipe in recipes:
        found_ingredients = set()
        for instruction in recipe.get("analyzedInstructions", []):
            for step in instruction.get("steps", []):
                for ing in step.get("ingredients", []):
                    found_ingredients.add(ing["name"].lower())

        if all(ingredient.lower() in found_ingredients for ingredient in required_ingredients):
            filtered.append(recipe)

    return filtered
