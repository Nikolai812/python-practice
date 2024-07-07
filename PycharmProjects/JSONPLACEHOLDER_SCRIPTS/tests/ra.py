import requests
import pytest
import os
from dotenv import load_dotenv


class RequestAsserter:
    @classmethod
    def assert_request(cls, request_url, expected_response_code, expected_response_data):
        # Send a GET request to the endpoint
        response = requests.get(request_url)

        # Check if the request was successful
        assert response.status_code == expected_response_code, f"Failed to retrieve data. Status code: {response.status_code}"

        # Parse the JSON response
        data = response.json()

        # Assert that the response matches the expected response
        assert data == expected_response_data, f"Response does not match expected object. Response: {data}, Expected: {expected_response_data}"


@pytest.fixture(scope="session")
def api_url(pytestconfig):
    # Get the URL from the pytest configuration
    load_dotenv()
    return os.environ["BASE_URL"]


def test_api_response(api_url):
    # Define the expected response
    expected_response = {
        "userId": 1,
        "id": 9,
        "title": "molestiae perspiciatis ipsa",
        "completed": False
    }

    # Use the RequestAsserter to send the request and assert the response
    RequestAsserter.assert_request(api_url + "9", 200, expected_response)


if __name__ == "__main__":
    pytest.main()