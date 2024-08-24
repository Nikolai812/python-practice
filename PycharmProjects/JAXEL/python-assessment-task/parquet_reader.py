import pandas as pd

# Specify the path to your Parquet file
parquet_file_path = './data/product_prices_calculated.parquet'

# Read the Parquet file into a DataFrame
df = pd.read_parquet(parquet_file_path)

# Display the first few rows of the DataFrame
print(df.head())

filtered_df = df[df['final_price'].isnull()]
print(filtered_df.head())

id_list = sorted(df['id'].tolist())

print(id_list)

id_title_price_list = df[['id', 'title', 'final_price']].to_dict('records')

sorted_expected_items = sorted(id_title_price_list, key=lambda x: x['id'])
print(sorted_expected_items)

for i in range(1,195):
    if not any(item['id'] == i for item in sorted_expected_items):
        print(i, " id is not in the sorted_expected_items")






