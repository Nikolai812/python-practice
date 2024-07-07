import requests


class RequestBuilder:
    def __init__(self, env_data):
        self.endpoint = None
        self.access_key_token = None
        self.base_code_token = None
        self.symbols_token = None
        self.date_string = None
        self.base_code_token = None
        self.symbols_token = None

        self.base_url = env_data["base_url"]
        self.api_key = env_data["api_key"]

    def get_request(self):
        if self.base_url is None or self.endpoint is None:
            raise Exception("endpoint od base_url not provided")
        result = f"{self.base_url}/{self.endpoint}"

        if self.date_string is not None:
            result += f"/{self.date_string}"

        if self.access_key_token is not None:
            result += f"?{self.access_key_token}"
        else:
            raise Exception("api key not provided")

        if self.base_code_token is not None:
            result += f"&{self.base_code_token}"

        if self.symbols_token is not None:
            result += f"&{self.symbols_token}"

        return result

    def set_endpoint(self, end_point_name):
        self.endpoint = str(end_point_name)
        return self

    def set_date(self, date_string):
        self.date_string = str(date_string)
        return self


    def use_valid_access_key(self, key_valid=True):
        if key_valid:
            self.access_key_token = str(f"access_key={self.api_key}")
        else:
            self.access_key_token = str("access_key=smth_invalid")
        return self

    def with_base(self, base_currency_code):
        self.base_code_token = str(f"base={base_currency_code}")
        return self

    def with_symbols(self, *symbols):
        self.symbols_token = str("symbols=" + ",".join(symbols))
        return self
