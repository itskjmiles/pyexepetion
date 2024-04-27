def adjust_recipe(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        print("Adjusted recipe quantities:")
        for ingredient, quantity in recipe.items():
            adjusted_quantity = quantity * adjustment_factor
            print(f"{ingredient}: {adjusted_quantity}")
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")
    except ValueError:
        print("Error: Please enter valid numerical values for servings.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Enjoy your cooking!")

def main():
    try:
        original_servings = int(input("Enter the number of servings the recipe is originally for: "))
        desired_servings = int(input("Enter the number of servings you wish to make: "))
        adjust_recipe(original_servings, desired_servings)
    except ValueError:
        print("Error: Please enter valid numerical values for servings.")

recipe = {
    "flour (cups)": 2,
    "sugar (cups)": 1,
    "eggs": 2,
    "butter (cups)": 0.5,
    "baking powder (teaspoons)": 1
}

if __name__ == "__main__":
    main()
