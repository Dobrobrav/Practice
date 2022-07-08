from F3_3_STR_REPR_LEN_ABS.CODE_3_3_9 import *

if __name__ == '__main__':
    recipe = Recipe()
    recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
    recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
    recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
    ings = recipe.get_ingredients()
    n = len(recipe)  # n = 3
    print(n)
