allowed_ingredients = [
    "earth",
    "air",
    "fire",
    "water"
]


def validate_ingredients(ingredients: str) -> str:
    ingredients = ingredients.lower()
    for ingredient in allowed_ingredients:
        if ingredient in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
