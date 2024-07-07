import requests
import pytest
import os
from dotenv import load_dotenv

# Define the endpoint URL
base_url = ""

@pytest.fixture(scope="session")
def api_url(pytestconfig):
    # Get the URL from the pytest configuration
    load_dotenv()
    return os.environ["BASE_URL"]


# Define the expected response
expected_response = {
    "userId": 1,
    "id": 9,
    "title": "molestiae perspiciatis ipsa",
    "completed": False
}


def test_api_response(api_url):
    # Send a GET request to the endpoint

    assert os.environ["DEPLOYMENT_STAGE"] == "dev"

    url = api_url + "9"
    response = requests.get(url)

    # Check if the request was successful
    assert response.status_code == 200, f"Failed to retrieve data. Status code: {response.status_code}"

    # Parse the JSON response
    data = response.json()

    # Assert that the response matches the expected response
    assert data == expected_response, f"Response does not match expected object. Response: {data}, Expected: {expected_response}"

#def test_api_response_0(api_url):
    # Send a GET request to the endpoint

#    url = api_url + "9"
    response = requests.get(url)

    # Check if the request was successful
#    assert response.status_code == 200, f"Failed to retrieve data. Status code: {response.status_code}"

    # Parse the JSON response
 #   data = response.json()

    # Assert that the response matches the expected response
#  assert data == expected_response, f"Response does not match expected object. Response: {data}, Expected: {expected_response}"


#if __name__ == "__main__":
#    pytest.main()