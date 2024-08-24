"""
   This script accepts 3 command-line parameters
   1. url - to get actual data
   2. limit - the amount of actual data records per one request
   3. file - file path to parquet file  with expected data
   The default values for these parameters allow to start script without
   command-line arguments
   The script saves results of its work to "report.txt"
"""

import requests
import pandas as pd
import argparse


def read_expected_data(parquet_file_path):
    """
    Reads the parquet file wit expected data,
    Extracts the "id", "title" and "final_price" from each item
    into the list. Sorts this list by id and returns it
    :param parquet_file_path: path to the parquet file
    """

    df = pd.read_parquet(parquet_file_path)
    id_title_price_list = df[['id', 'title', 'final_price']].to_dict('records')
    sorted_expected_items = sorted(id_title_price_list, key=lambda x: x['id'])
    return sorted_expected_items


def get_raw_actual_data(url, limit):
    """
    Gets response from the given url with given 'limit' parameter.
    Selects 'products' list from the response
    """
    request_params = {
        'limit': limit
    }
    response = requests.get(url, request_params)

    # assert that the request was successful
    assert response.status_code == 200, f"Failed to retrieve data. Status code: {response.status_code}"

    # Parse the JSON response
    data = response.json()
    raw_products = data.get("products")
    return raw_products


def verify_calculated_data(func):
    """
    This is a decorator to verify that the calculated actual data (products)
    has been calculated without errors (correct input data was provided)
    """
    def inner(raw_data):
        calculated_data = func(raw_data)
        products_with_errors = filter_objects_with_error(calculated_data)
        errors_num = len(products_with_errors)
        if errors_num > 0:
            print(f"{errors_num} products were calculated with errors:")
            print(products_with_errors)
        return calculated_data
    return inner


@verify_calculated_data
def refine_and_calculate_actual_data(raw_data):
    """
    Selects several actual fields for the products,
    calculates the 'final_price' for each product.
    returns the list of product item containing actual fields from the response
    and the calculated final_price
    """
    calculated_products = [
        {
            "id": obj["id"],
            "title": obj["title"],
            "price": obj["price"],
            "discountPercentage": obj["discountPercentage"]
        }
        for obj in raw_data
    ]

    for product_item in calculated_products:
        add_final_price(product_item)

    return calculated_products


def get_actual_data(url, limit):
    """
    Gets response from the given url with given 'limit' parameter.
    Selects 'products' list from the response, takes several actual fields
    for the products, then calculates the 'final_price' for each product.
    returns the list of product item containing actual fields from the response
    and the calculated final_price
    """

    raw_products = get_raw_actual_data(url, limit)
    calculated_products = refine_and_calculate_actual_data(raw_products)
    return calculated_products


def add_final_price(product):
    """
    Adds a 'final_price' field to the object, calculated using the 'price' and 'discountPercentage' fields.
    Handles exceptions if 'price' or 'discountPercentage' are invalid.
    """
    try:
        # Ensure the necessary fields are present in the object
        if 'price' not in product or 'discountPercentage' not in product:
            raise ValueError("Missing 'price' or 'discountPercentage' fields.")

        price = product['price']
        discount = product['discountPercentage']

        # Check if the values are not None
        if price is None or discount is None:
            raise ValueError("'price' and 'discountPercentage' cannot be None.")

        # Check if price and discount are valid numbers
        if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
            raise ValueError("'price' and 'discountPercentage' must be numeric values.")

        # Calculate the final price
        final_price = price * (100 - discount) / 100

        # Round the final price to 2 decimal points
        product['final_price'] = round(final_price, 2)

    except ValueError as e:
        product['error'] = str(e)

    return product


def filter_objects_with_error(objects):
    """
    Filters objects from the list that contain an 'error' field.
    """
    return [obj for obj in objects if 'error' in obj]


def get_product_with_max_final_price(objects):
    """
    Returns the object with the maximum 'final_price' value from a list of objects.
    """
    if not objects:
        return None

    # Use the max function with a key argument to find the object with the maximum 'final_price'
    result = max(objects, key=lambda obj: obj.get('final_price', float('-inf')))
    print(f"MAX final price has  the following product: {result} ")
    with open('report.txt', 'a') as report_file:
        print("# 1. What product is the most expensive according to actual data?", file=report_file)
        print(f"     MAX final price has  the following product: {result} ", file=report_file)
    return result


def find_actual_data_missing_in_expected_data(actual_data, expected_data):
    result = [item for item in actual_data if item['id'] not in {e['id'] for e in expected_data}]
    print(f"found {len(result)} unmatched actual products:")
    print(result)
    with open('report.txt', 'a') as report_file:
        print("# 2. What product is missing in expected data comparing with actual data?",
              file=report_file)
        print(f"     found {len(result)} unmatched actual products:", file=report_file)
        print("    ", result, file=report_file)
    return result


def calculate_where_expected_price_matches_actual(actual_data, expected_data) -> int:
    matching_list = []
    for expected_item in expected_data:
        actual_items = [item for item in actual_data if item['id'] == expected_item['id']]
        assert len(actual_items) == 1
        if actual_items[0]["final_price"] == expected_item["final_price"]:
            matching_list.append(actual_items[0])

    result = len(matching_list)
    print(f"Expected price matches actual for {result} rows")
    with open('report.txt', 'a') as report_file:
        print("#3. For how many rows final price in expected data matches with calculated price from actual data?",
              file=report_file)
        print(f"    Expected price matches actual for {result} rows", file=report_file)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url",
                        help="Dummy JSON products URL",
                        default="https://dummyjson.com/products")
    parser.add_argument("-l", "--limit", dest="limit",
                        help="Response Items limit",
                        default=200)

    parser.add_argument("-f", "--file", dest="file",
                        help="Expected Data File",
                        default="./data/product_prices_calculated.parquet")

    args = parser.parse_args()

    with open('report.txt', 'w') as file:
        print("This is the report file for Nikolai Romanenko's assessment.", file=file)
        print("The following command-line arguments are used:", file=file)
        print("url=", args.url, ", limit=", args.limit, ", file=",  args.file, file=file)
        print(" ", file=file)

    expected_items = read_expected_data(args.file)
    actual_products = get_actual_data(args.url, args.limit)

    # Questions:
    # 1. What product is the most expensive according to actual data?
    max_price_product = get_product_with_max_final_price(actual_products)

    # 2. What product is missing in expected data comparing with actual data?
    unmatched_actual_items = find_actual_data_missing_in_expected_data(actual_products, expected_items)

    # 3. For how many rows final price in expected data matches with calculated price from actual data?
    row_number = calculate_where_expected_price_matches_actual(actual_products, expected_items)
