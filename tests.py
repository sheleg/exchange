import unittest
import requests

from main import get_exchange_rate
from requests.models import Response

class Test(unittest.TestCase):
    def test_success(self):
        def test_request_adapter(url):
            the_response = Response()
            the_response.code = "success"
            the_response.status_code = 200
            the_response._content = b'{ "success" : true, "rates" : {"USD" : 2, "GBP" : 1} }'

            return the_response

        self.assertEqual(get_exchange_rate(test_request_adapter), 50)
    
    def test_retry_on_error(self):
        def test_request_adapter(url):

            the_response = Response()
            the_response.code = "success"
            if test_request_adapter.attempts < 5:
                the_response.status_code = 400
            else:
                the_response.status_code = 200

            the_response._content = b'{ "success" : true, "rates" : {"USD" : 2, "GBP" : 1} }'

            test_request_adapter.attempts += 1
            return the_response

        test_request_adapter.attempts = 0
        self.assertEqual(get_exchange_rate(test_request_adapter), 50)
        self.assertEqual(test_request_adapter.attempts, 6)


if __name__ == '__main__':
    unittest.main()
