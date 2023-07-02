import json
def process_nutrients(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_data = json.load(input_file)
        
        # this will store all nutrients
        nutrients = []
        
        for branded_food in input_data['BrandedFoods']:
            for nutrient in branded_food['foodNutrients']:
                nutrient_to_add = nutrient['nutrient']
                # check if nutrient is already in list
                if nutrient_to_add not in nutrients:
                    
                    # the form of the nutrient in the json is the same format in the database so nothing to change here
                    nutrients.append(nutrient_to_add)
        
        # Write the nutrient list to the output file
        output_data = {
            'Nutrients': nutrients
        }
        with open(output_file, 'w', encoding='utf-8') as output_file:
            json.dump(output_data , output_file)

def process_products(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_data = json.load(input_file)

        # this will store all products
        products = []

        for branded_food in input_data['BrandedFoods']:
            fdcId = branded_food.get('fdcId')
            avalibleDate = branded_food.get('avalibleDate')
            brandOwner = branded_food.get('brandOwner')
            dataSource = branded_food.get('dataSource')
            description = branded_food.get('description')
            gtinUpc = branded_food.get('gtinUpc')
            householdServingFullText = branded_food.get('householdServingFullText')
            ingredients = branded_food.get('ingredients')
            modifiedDate = branded_food.get('modifiedDate')
            publicationDate = branded_food.get('publicationDate')
            servingSize = branded_food.get('servingSize')
            servingSizeUnit = branded_food.get('servingSizeUnit')
            brandedFoodCategory = branded_food.get('brandedFoodCategory')

            product = {
                'fdcId': fdcId,
                'avalibleDate': avalibleDate,
                'brandOwner': brandOwner,
                'dataSource': dataSource,
                'description': description,
                'gtinUpc': gtinUpc,
                'householdServingFullText': householdServingFullText,
                'ingredients': ingredients,
                'modifiedDate': modifiedDate,
                'publicationDate': publicationDate,
                'servingSize': servingSize,
                'servingSizeUnit': servingSizeUnit,
                'brandedFoodCategory': brandedFoodCategory
            }

            products.append(product)

        # Write the products to the output file

        output_data = {
            'Products': products
        }

        with open(output_file, 'w', encoding='utf-8') as output_file:
            json.dump(output_data, output_file)

import json
import time
import os

def process_food_nutrients(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_data = json.load(input_file)

    food_nutrients = set()
    num_branded_foods = len(input_data['BrandedFoods'])
    processed_foods = 0

    start_time = time.time()

    for branded_food in input_data['BrandedFoods']:
        fdcId = branded_food['fdcId']
        for food_nutrient in branded_food['foodNutrients']:
            food_nutrient_id = food_nutrient['id']
            nutrient_id = food_nutrient['nutrient']['id']
            amount = food_nutrient['amount']

            food_nutrient_to_add = {
                'product_id': fdcId,
                'food_nutrient_id': food_nutrient_id, 
                'nutrient_id': nutrient_id,
                'amount': amount
            }

            food_nutrients.add(json.dumps(food_nutrient_to_add, sort_keys=True))
            processed_foods += 1

            # Calculate progress
            progress = processed_foods / num_branded_foods * 100
            elapsed_time = time.time() - start_time

            # Calculate estimated time remaining
            avg_time_per_food = elapsed_time / processed_foods
            remaining_foods = num_branded_foods - processed_foods
            estimated_time_remaining = avg_time_per_food * remaining_foods

            # Clear previous line in the console
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print progress information
            print(f'Progress: {progress:.2f}%')
            print(f'Estimated time remaining: {estimated_time_remaining:.2f} seconds')

    food_nutrients = [json.loads(fn) for fn in food_nutrients]

    output_data = {
        'foodNutrients': food_nutrients
    }
    with open(output_file, 'w', encoding='utf-8') as output_file:
        json.dump(output_data, output_file)


                

        
input_file = 'data/input_data/sample_usda_data.json'
# print('program starting')
# process_products(input_file, 'data/processed_data/products.json')
# print('products complete')
# process_nutrients(input_file, 'data/processed_data/nutrients.json')
# print('nutrients complete')
print('program starting')
process_food_nutrients(input_file, 'data/processed_data/food_nutrients.json')
print('program complete')     

