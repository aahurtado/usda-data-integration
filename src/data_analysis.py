import json

def analyze_nutrients(input_file, output_file):
    # Read the input JSON file
    with open(input_file, "r") as f:
        input_structure = json.load(f)

    nutrients = input_structure["Nutrients"]

    # Determine the shortest and longest strings for each field
    shortest_id = min((nutrient["id"] for nutrient in nutrients))
    longest_id = max((nutrient["id"] for nutrient in nutrients))

    shortest_number = min((nutrient["number"] for nutrient in nutrients), key=len)
    longest_number = max((nutrient["number"] for nutrient in nutrients), key=len)

    shortest_name = min((nutrient["name"] for nutrient in nutrients), key=len)
    longest_name = max((nutrient["name"] for nutrient in nutrients), key=len)

    shortest_unit_name = min((nutrient["unitName"] for nutrient in nutrients), key=len)
    longest_unit_name = max((nutrient["unitName"] for nutrient in nutrients), key=len)

    
    # Create the nutrient_data list with a single dictionary element
    nutrient_data = [
        {
            "shortest_id": shortest_id,
            "longest_id": longest_id,
            "shortest_number": shortest_number,
            "longest_number": longest_number,
            "shortest_name": shortest_name,
            "longest_name": longest_name,
            "shortest_unit_name": shortest_unit_name,
            "longest_unit_name": longest_unit_name,
            "total_nutrients": len(nutrients),
        }
    ]

    # Write the nutrient_data list to the output JSON file
    with open(output_file, "w") as f:
        json.dump(nutrient_data, f)






def analyze_products(input_file, output_file):
    # Read the input JSON file
    with open(input_file, "r") as f:
        input_structure = json.load(f)

    products = input_structure["Products"]

    longest_fdc_id = max((product["fdcId"] for product in products))
    longest_avalible_date = max(((product["avalibleDate"], len(str(product["avalibleDate"]))) for product in products if isinstance(product["avalibleDate"], str) and product["avalibleDate"]), key=lambda x: x[1], default=("", 0))
    longest_brand_owner = max(((product["brandOwner"], len(product["brandOwner"])) for product in products if isinstance(product["brandOwner"], str) and product["brandOwner"]), key=lambda x: x[1], default=("", 0))
    longest_data_source = max(((product["dataSource"], len(product["dataSource"])) for product in products if isinstance(product["dataSource"], str) and product["dataSource"]), key=lambda x: x[1], default=("", 0))
    longest_description = max(((product["description"], len(product["description"])) for product in products if isinstance(product["description"], str) and product["description"]), key=lambda x: x[1], default=("", 0))
    longest_gtin_upc = max(((product["gtinUpc"], len(product["gtinUpc"])) for product in products if isinstance(product["gtinUpc"], str) and product["gtinUpc"]), key=lambda x: x[1], default=("", 0))
    longest_household_serving_full_text = max(((product["householdServingFullText"], len(product["householdServingFullText"])) for product in products if isinstance(product["householdServingFullText"], str) and product["householdServingFullText"]), key=lambda x: x[1], default=("", 0))
    longest_ingredients = max(((product["ingredients"], len(product["ingredients"])) for product in products if isinstance(product["ingredients"], str) and product["ingredients"]), key=lambda x: x[1], default=("", 0))
    longest_modified_date = max(((product["modifiedDate"], len(product["modifiedDate"])) for product in products if isinstance(product["modifiedDate"], str) and product["modifiedDate"]), key=lambda x: x[1], default=("", 0))
    longest_publication_date = max(((product["publicationDate"], len(product["publicationDate"])) for product in products if isinstance(product["publicationDate"], str) and product["publicationDate"]), key=lambda x: x[1], default=("", 0))
    longest_serving_size_unit = max(((product["servingSizeUnit"], len(product["servingSizeUnit"])) for product in products if isinstance(product["servingSizeUnit"], str) and product["servingSizeUnit"]), key=lambda x: x[1], default=("", 0))
    longest_branded_food_category = max(((product["brandedFoodCategory"], len(product["brandedFoodCategory"])) for product in products if isinstance(product["brandedFoodCategory"], str) and product["brandedFoodCategory"]), key=lambda x: x[1], default=("", 0))


    total_products = len(products)

    # Create the product_analysis dictionary
    product_analysis = {
        "longest_fdc_id": longest_fdc_id,
        "longest_avalible_date": longest_avalible_date,
        "longest_brand_owner": longest_brand_owner,
        "longest_data_source": longest_data_source,
        "longest_description": longest_description,
        "longest_gtin_upc": longest_gtin_upc,
        "longest_household_serving_full_text" : longest_household_serving_full_text,
        "longest_ingredients": longest_ingredients,
        "longest_modified_date": longest_modified_date,
        "longest_publication_date": longest_publication_date,
        "longest_serving_size_unit": longest_serving_size_unit,
        "longest_branded_food_category": longest_branded_food_category,
        "total_products": total_products,
    }

    # Write the product_analysis dictionary to the output JSON file
    with open(output_file, "w") as f:
        json.dump(product_analysis, f)





def analyze_food_nutrients(input_file, output_file):

    # Read the input JSON file
    with open(input_file, "r") as f:
        input_structure = json.load(f)

    food_nutrients = input_structure["foodNutrients"]

    # Determine the minimum and maximum values for each field
    min_product_id = min(nutrient["productId"] for nutrient in food_nutrients)
    max_product_id = max(nutrient["productId"] for nutrient in food_nutrients)

    min_food_nutrient_id = min(nutrient["foodNutrientId"] for nutrient in food_nutrients)
    max_food_nutrient_id = max(nutrient["foodNutrientId"] for nutrient in food_nutrients)

    min_nutrient_id = min(nutrient["nutrientId"] for nutrient in food_nutrients)
    max_nutrient_id = max(nutrient["nutrientId"] for nutrient in food_nutrients)

    min_amount = min(nutrient["amount"] for nutrient in food_nutrients)
    max_amount = max(nutrient["amount"] for nutrient in food_nutrients)

    total_food_nutrients = len(food_nutrients)

    # Create the analysis results dictionary
    analysis_results = {
        "min_product_id": min_product_id,
        "max_product_id": max_product_id,
        "min_food_nutrient_id": min_food_nutrient_id,
        "max_food_nutrient_id": max_food_nutrient_id,
        "min_nutrient_id": min_nutrient_id,
        "max_nutrient_id": max_nutrient_id,
        "min_amount": min_amount,
        "max_amount": max_amount,
        "total_food_nutrients": total_food_nutrients,
    }

    # Write the analysis results to the output JSON file
    with open(output_file, "w") as f:
        json.dump(analysis_results, f)




# analyze_nutrients('data/processed_data/nutrients.json', 'data/analysis_data/nutrient_analysis.json')
# analyze_products('data/processed_data/products.json', 'data/analysis_data/product_analysis.json')
# analyze_food_nutrients('data/processed_data/food_nutrients.json', 'data/analysis_data/food_nutrient_analysis.json')



from collections import Counter

def extract_product_descriptions(input_file, field, output_file):
    # Read the input JSON file
    with open(input_file, "r") as f:
        input_structure = json.load(f)

    products = input_structure["Products"]

    # Count the frequency of each description
    frequency_counter = Counter()
    for product in products:
        if isinstance(product[field], str):
            frequency_counter[product[field]] += 1

    # Sort descriptions by frequency (in descending order)
    sorted_descriptions = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)

    # Write the descriptions and frequencies to the output JSON file
    output_file = output_file + field + ".json"
    with open(output_file, "w") as f:
        json.dump(sorted_descriptions, f)

        total_categories = len(sorted_descriptions)
        f.write('\n')
        f.write(f"Total Categories: {total_categories}")


# Usage example:
#extract_product_descriptions('data/processed_data/products.json', "brandedFoodCategory", "data/analysis_data/field_frequency/")
# Read the JSON file
with open('data/analysis_data/field_frequency/brandedFoodCategory.json') as json_file:
    data = json.load(json_file)

# Prepare the list of objects in the desired format
result = []
for item in data:
    category = item[0]
    frequency = item[1]
    obj = {
        "name": category + " " + str(frequency),
        "paneIndex": 0
    }
    result.append(obj)

# Convert the list to JSON format
json_data = json.dumps(result, indent=2)

# Write the JSON data to a file
with open('output.json', 'w') as output_file:
    output_file.write(json_data)