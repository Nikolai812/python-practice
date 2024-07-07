import requests
import pytest
import os
from dotenv import load_dotenv
from processing.request_asserter import *
from processing.request_builder import *
from expected_data.fixer_latest_expected_template import *
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

# TC-FUNC-LATEST-12
# The test implements a request with positive response
# Base currency is specified, no symbols are specified
def test_fixer_latest_with_base_euro(env_data):
    # Define the expected response
    expected_response = FixerLatestExpected.get_latest_expected_template()

    # Building request by a request builder
    builder = RequestBuilder(env_data)
    request_url = builder.set_endpoint('latest').use_valid_access_key().with_base("EUR").get_request()

    # Use the RequestAsserter to send the request and assert the response
    response_data = RequestAsserter.assert_request_by_fields(request_url, 200, **expected_response)

    # assert the currency list provided by "ratio"
    expected_currency_codes = FixerLatestExpected.get_currency_codes()
    assert (len(response_data.get("rates")) == len(expected_currency_codes))
    actual_currency_codes = tuple(dict(response_data.get("rates")).keys())
    assert (actual_currency_codes == expected_currency_codes)

    # TODO: assert currency rates
    # can be implemented when the expected rates data source is established
    # expected_rates = FixerLatestExpected.get_rates()
    # assert(response_data.get("rates") == expected_rates)


# TC-FUNC-LATEST-13
# The test implements a request with positive response
# Base currency and symbols are specified
@pytest.mark.parametrize("symbols", [
    ("AZN", "GBP", "RSD", "RUB"),
    ("USD", "CAD", "JPY")
])
def test_fixer_latest_base_euro_with_symbols(env_data, symbols):
    # Define the expected response
    expected_response = FixerLatestExpected.get_latest_expected_template()

    # Building request by a request builder
    builder = RequestBuilder(env_data)
    request_url = builder.set_endpoint('latest').use_valid_access_key().with_base("EUR").with_symbols(
        *symbols).get_request()

    # Use the RequestAsserter to send the request and assert the response
    response_data = RequestAsserter.assert_request_by_fields(request_url, 200, **expected_response)

    # assert the currency list provided by "ratio"
    expected_currency_codes = symbols
    assert (len(response_data.get("rates")) == len(expected_currency_codes))
    actual_currency_codes = tuple(dict(response_data.get("rates")).keys())
    assert (actual_currency_codes == expected_currency_codes)

    # TODO: assert currency rates
    # can be implemented when the expected rates data source is established
    # expected_rates = FixerLatestExpected.get_rates()
    # assert(response_data.get("rates") == expected_rates)

# TC-FUNC-LATEST-14
# This test verifies the response in case of valid date for HISTORICAL point
def test_fixer_invalid_date(env_data):
    # Define the expected response
    expected_response = FixerNegativeExpected.get_invalid_date_expected_response()

    # Building request by a request builder
    builder = RequestBuilder(env_data)
    request = builder.set_endpoint('historical').set_date("2023-11-11").use_valid_access_key().get_request()

    # Use the RequestAsserter to send the request and assert the response
    response_data = RequestAsserter.assert_request(request, 200, expected_response)


if __name__ == "__main__":
    pytest.main()
