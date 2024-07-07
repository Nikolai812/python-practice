import requests
import pytest
import os

from dotenv import load_dotenv

# Define the endpoint URL
url = "https://jsonplaceholder.typicode.com/todos/9"

@pytest.fixture
def api_url(pytestconfig):
    # Get the URL from the pytest configuration
    # v = pytestconfig.getini("api_url")
  #  load_dotenv()
    return ''


# Define the expected response
expected_response = {
    "userId": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False
}


def test_api_response(api_url):
    # Send a GET request to the endpoint
    u = api_url

    e = os.environ

    assert os.environ["DEPLOYMENT_STAGE"] == "dev"
    #assert os.environ["API_ENDPOINT"] == "https://api.staging.example.com"
    #assert os.environ["ACCOUNT_ID"] == "56789"

    response = requests.get(url)

    # Check if the request was successful
    assert response.status_code == 200, f"Failed to retrieve data. Status code: {response.status_code}"

    # Parse the JSON response
    data = response.json()

    # Assert that the response matches the expected response
    assert data == expected_response, f"Response does not match expected object. Response: {data}, Expected: {expected_response}"

def test_api_response_0(api_url):
    # Send a GET request to the endpoint
    u = api_url
    response = requests.get(url)

    # Check if the request was successful
    assert response.status_code == 200, f"Failed to retrieve data. Status code: {response.status_code}"

    # Parse the JSON response
    data = response.json()

    # Assert that the response matches the expected response
    assert data == expected_response, f"Response does not match expected object. Response: {data}, Expected: {expected_response}"


#if __name__ == "__main__":
#    pytest.main()