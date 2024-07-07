from datetime import datetime


class FixerNegativeExpected:
    @classmethod
    def get_invalid_key_expected_response(cls):
        expected_template = {
            "success": False,
            "error": {
                "code": 101,
                "type": "invalid_access_key",
                    #"missing_access_key"
                "info": "You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com]"
                    #"You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"
            }
        }

        return expected_template

    @classmethod
    def get_invalid_date_expected_response(cls):
        expected_template = {
            "success": False,
            "error": {
                "code": 302,
                "type": "invalid_date",
                "info": "You have entered an invalid date. [Required format: date=YYYY-MM-DD]"
    }
}

        return expected_template
