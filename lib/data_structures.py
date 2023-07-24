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
    list_of_foods = [food["name"] for food in spicy_foods]
    return list_of_foods

get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    list_of_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    # return list_of_foods
    # list_of_foods = []
    # for food in spicy_foods:
    #     if food["heat_level"] > 5:
    #         list_of_foods.append(food)

    return list_of_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spicy_foods_string = "{} ({}) | Heat Level: {}".format(food["name"], food["cuisine"], food["heat_level"] * "🌶")
        print (spicy_foods_string)
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    by_cuisine = [food for food in spicy_foods if food["cuisine"] == cuisine]
    return by_cuisine[0]
    pass

def print_spiciest_foods(spicy_foods):
    # list_of_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    list_of_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(list_of_foods)
    pass

def get_average_heat_level(spicy_foods):
    list_of_heat = [food["heat_level"] for food in spicy_foods]
    return (sum(list_of_heat)/len(list_of_heat)) 
    pass


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
