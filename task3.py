inventory = {    
    "herb": 3,
    "water": 5,
    "mushroom": 2,
    "crystal": 0}

recipes = {    
    "health_potion": {"herb": 2, "water": 1},
    "mana_potion": {"crystal": 1, "water": 2},
    "invisibility_potion": {"mushroom": 3, "water": 2, "herb": 1}}

def add_ingredient(inventory, ingridient, amount):
    inventory[ingridient] = inventory.get(ingridient, 0) + amount

def brew_potion(inventory, recipes, potion_name):
    if potion_name not in recipes:
        return False
    
    for ingr in recipes[potion_name].items():
        if ingr[0] in inventory:
            if inventory[ingr[0]] >= ingr[1]:
                inventory[ingr[0]] -= ingr[1]
                if inventory[ingr[0]] == 0:
                    del inventory[ingr[0]]
            else:
                return False
        else:
            return False
    return True
