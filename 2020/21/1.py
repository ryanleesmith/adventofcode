from collections import Counter

def main():
    allergen_map = {}
    ingredients = []
    allergenic_ingredients = {}
    input = open("input.txt", "r")
    for line in input.read().splitlines():
        (recipe, allergens) = line.split(" (contains ")
        allergens = allergens[:-1].split(", ")
        recipe = recipe.split(" ")
        for allergen in allergens:
            if allergen not in allergen_map:
                allergen_map[allergen] = recipe
            else:
                allergen_map[allergen] = list(set(allergen_map[allergen]) & set(recipe))
                if len(allergen_map[allergen]) == 1:
                    matched = allergen_map[allergen][0]
                    allergenic_ingredients[matched] = allergen
                    for (other_allergen, other_recipe) in allergen_map.items():
                        try:
                            other_recipe.remove(matched)
                        except:
                            pass
        ingredients.extend(recipe)

    for (allergen, recipe) in allergen_map.items():
        for (other_allergen, other_recipe) in allergen_map.items():
            if other_allergen == allergen:
                pass
            matching = list(set(recipe) & set(other_recipe))
            if len(matching) == 1:
                matched = recipe[0]
                allergenic_ingredients[matched] = allergen
                for (clear_allergen, clear_recipe) in allergen_map.items():
                    if clear_allergen == allergen:
                        del clear_recipe[:]
                    else:
                        try:
                            clear_recipe.remove(matched)
                        except:
                            pass

    ingredients = list(filter(lambda i: i not in allergenic_ingredients.keys(), ingredients))
    print(sum(Counter(ingredients).values()))

if __name__ == "__main__":
    main()
