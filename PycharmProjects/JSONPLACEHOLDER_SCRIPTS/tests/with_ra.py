import requests
import pytest
import os
from dotenv import load_dotenv
from processing.request_asserter import *



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
    RequestAsserter.assert_request_by_fields(api_url + "9", 200, **expected_response)


if __name__ == "__main__":
    pytest.main()