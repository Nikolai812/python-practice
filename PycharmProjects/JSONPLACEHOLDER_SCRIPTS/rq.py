import requests

# Endpoint URL
url = "https://jsonplaceholder.typicode.com/todos/9"

# Sending a GET request to the endpoint
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response to a Python dictionary
    data = response.json()

    # Printing the Python object
    print("User ID:", data["userId"])
    print("ID:", data["id"])
    print("Title:", data["title"])
    print("Completed:", data["completed"])
else:
    print("Failed to retrieve data. Status code:", response.status_code)



if __name__ == "main":
    pass