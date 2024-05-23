spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = '🌶' * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    return None
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)
    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level_emojis = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    return None
    pass

def get_average_heat_level(spicy_foods):
    heat_levels = [food['heat_level'] for food in spicy_foods]
    return sum(heat_levels) / len(heat_levels)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
