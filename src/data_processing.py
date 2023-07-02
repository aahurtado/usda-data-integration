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

def process_food_nutrients(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_data = json.load(input_file)

        # this will store all food nutrients
        food_nutrients = []

        for branded_food in input_data['BrandedFoods']:

            # here we want to grab the id of the product to insert into the food_nutrient object
            fdcId = branded_food['fdcId']
            for food_nutrient in branded_food['foodNutrients']:

                # grab the data from the food nutrient object as well as the nutrient id
                food_nutrient_id = food_nutrient['id']
                nutrient_id = food_nutrient['nutrient']['id']
                amount = food_nutrient['amount']

                # adding fields to the nutrient object to the list
                food_nutrient_to_add = {
                    'product_id': fdcId,
                    'food_nutrient_id': food_nutrient_id,
                    'nutrient_id': nutrient_id,
                    'amount': amount
                }

                # now check for duplicates
                if food_nutrient_to_add not in food_nutrients:
                    food_nutrients.append(food_nutrient_to_add)

        # Write the results to the output file
        output_data = {
            'foodNutrients': food_nutrients
        }
        with open(output_file, 'w', encoding='utf-8') as output_file:
            json.dump(output_data, output_file)

                

        


# process_nutrients('data/input_data/sample_usda_data.json', 'data/processed_data/nutrients.json')

process_products('data/input_data/sample_usda_data.json', 'data/processed_data/products.json')

# process_food_nutrients('data/input_data/sample_usda_data.json', 'data/processed_data/food_nutrients.json')

