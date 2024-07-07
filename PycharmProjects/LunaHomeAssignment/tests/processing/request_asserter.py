import requests


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

    @classmethod
    def assert_request_by_fields(cls, request_url, expected_response_code, **expected_fields):
        # Send a GET request to the endpoint
        response = requests.get(request_url)

        # Check if the request was successful
        assert response.status_code == expected_response_code, f"Failed to retrieve data. Status code: {response.status_code}"

        # Parse the JSON response
        data = response.json()

        # Assert that the response contains the expected fields
        for field, expected_value in expected_fields.items():
            assert data.get(
                field) == expected_value, f"Field '{field}' does not match expected value. Response: {data.get(field)}, Expected: {expected_value}"

        # return data for futher processing
        return data