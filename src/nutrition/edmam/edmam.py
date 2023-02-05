import os
from datetime import date, timedelta
from py_edamam import Edamam
import json
from random import randrange
from dotenv import load_dotenv
load_dotenv()

edamam_instance = Edamam(
                    nutrition_appid=os.getenv('nutrition_appid'),
                    nutrition_appkey=os.getenv('nutrition_appkey'),
                    recipes_appid=os.getenv('recipes_appid'),
                    recipes_appkey=os.getenv('recipes_appkey'),
                    food_appid=os.getenv('food_appid'),
                    food_appkey=os.getenv('food_appkey')
                    )

# print(json.dumps(e.search_nutrient("1 large apple"), indent=2))
# recipes = json.dumps(e.search_recipe("biryani")['hits'][0], indent=2)
# print(recipes)
# print(e.search_food("coke"))

def searchRecipe(recipe_name: str) -> dict:
    if recipe_name is None:
        response = {
            'statusCode': 401,
            'status': False,
            'message': 'Recipe Name is required',
            'data': None
        }
        return response;
    results = edamam_instance.search_recipe(recipe_name)["hits"]
    results = results[:min(10, len(results))]
    response = {
        'statusCode': 200,
        'status': True,
        'message': None,
        'data': results
    }
    return response

def fetchCalorieList() -> dict:
    date_list = []
    data_points = []
    for i in range(31, 1, -1):
        dt = (date.today() - timedelta(days=i)).isoformat()
        date_list.append(dt)
        data_points.append(randrange(2000, 2500))

    response = {
        'statusCode': 200,
        'status': True,
        'message': None,
        'data': {
            'date_list': date_list,
            'data_points': data_points
        }
    }
    return response

