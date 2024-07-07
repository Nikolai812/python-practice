import requests
import pytest
import os
from dotenv import load_dotenv
from processing.request_asserter import *
from processing.request_builder import  *
from expected_data.fixer_latest_expected_template import *



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
# The smoke test implements a minimal default request with positive response
# Only enpoint name and access ket are specified
def test_fixer_latest_smoke(env_data):
    # Define the expected response
    expected_response = FixerLatestExpected.get_latest_expected_template()
    base_url = env_data["base_url"]
    # Building request by a request builder
    builder = RequestBuilder(env_data)
    request_url = builder.empty().set_endpoint('latest').use_valid_access_key().get_request()

    # Use the RequestAsserter to send the request and assert the response
    response_data = RequestAsserter.assert_request_by_fields(request_url, 200, **expected_response)

    # assert the currency list provided by "ratio"
    expected_currency_codes = FixerLatestExpected.get_currency_codes()
    assert(len(response_data.get("rates")) == len(expected_currency_codes))
    actual_currency_codes = tuple(dict(response_data.get("rates")).keys())
    assert(actual_currency_codes == expected_currency_codes)

    # TODO: assert currency rates
    # can be implemented when the expected rates data source is established
    # expected_rates = FixerLatestExpected.get_rates()
    # assert(response_data.get("rates") == expected_rates)

if __name__ == "__main__":
    pytest.main()