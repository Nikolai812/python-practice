import requests
import pytest
import os
from dotenv import load_dotenv
from processing.request_asserter import *
from processing.request_builder import *
from expected_data.fixer_negative_expected import *


@pytest.fixture(scope="session")
def env_data(pytestconfig):
    # Get the env data from the pytest configuration
    load_dotenv()
    env_data = {
        "base_url": os.environ["BASE_URL"],
        "api_key": os.environ["API_KEY"]
    }
    return env_data

# TC-FUNC-LATEST-01
# This test verifies the response in case of invalid access key
def test_fixer_invalid_key(env_data):
    # Define the expected response
    expected_response = FixerNegativeExpected.get_invalid_key_expected_response()

    # Building request by a request builder
    builder = RequestBuilder(env_data)
    request = builder.set_endpoint('latest').use_valid_access_key(False).get_request()

    # Use the RequestAsserter to send the request and assert the response
    response_data = RequestAsserter.assert_request(request, 200, expected_response)

# TC-FUNC-LATEST-02
# This test verifies the response in case of invalid date for HISTORICAL point
def test_fixer_invalid_date(env_data):
    # Define the expected response
    expected_response = FixerNegativeExpected.get_invalid_date_expected_response()

    # Building request by a request builder
    builder = RequestBuilder(env_data)
    request = builder.set_endpoint('historical').set_date("invalid").use_valid_access_key().get_request()

    # Use the RequestAsserter to send the request and assert the response
    response_data = RequestAsserter.assert_request(request, 200, expected_response)

if __name__ == "__main__":
    pytest.main()
