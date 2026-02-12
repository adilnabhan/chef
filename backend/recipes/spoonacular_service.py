import requests
from django.conf import settings

class SpoonacularService:
    def __init__(self):
        self.api_key = settings.SPOONACULAR_API_KEY
        self.base_url = settings.SPOONACULAR_BASE_URL
    
    def search_recipes(self, query, number=10):
        """Search recipes by query"""
        url = f"{self.base_url}/recipes/complexSearch"
        params = {
            'apiKey': self.api_key,
            'query': query,
            'number': number,
            'addRecipeInformation': True,
            'fillIngredients': True
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error searching recipes: {e}")
            return None
    
    def get_recipe_by_id(self, recipe_id):
        """Get detailed recipe by ID"""
        url = f"{self.base_url}/recipes/{recipe_id}/information"
        params = {
            'apiKey': self.api_key,
            'includeNutrition': False
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting recipe: {e}")
            return None
    
    def search_by_ingredients(self, ingredients, number=10):
        """Search recipes by ingredients"""
        url = f"{self.base_url}/recipes/findByIngredients"
        params = {
            'apiKey': self.api_key,
            'ingredients': ingredients,
            'number': number,
            'ranking': 2,
            'ignorePantry': True
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error searching by ingredients: {e}")
            return None
    
    def get_random_recipes(self, number=10):
        """Get random recipes"""
        url = f"{self.base_url}/recipes/random"
        params = {
            'apiKey': self.api_key,
            'number': number
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting random recipes: {e}")
            return None