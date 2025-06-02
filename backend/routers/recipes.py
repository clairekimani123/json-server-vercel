import os
import requests
from fastapi import APIRouter, HTTPException, Query
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/recipes", tags=["Recipes"])
API_KEY = os.getenv("SPOONACULAR_API_KEY")

@router.get("/")
def get_recipes(number: int = 10):
    url = "https://api.spoonacular.com/recipes/random"
    params = {
        "apiKey": API_KEY,
        "number": 40,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["recipes"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
