import unittest
import urllib2

from src.request import Request


class TestRequest(unittest.TestCase):

    def test_requests(self):
        # Assume
        url = 'https://www.ole.com.ar/river-plate/'
        # Action
        request = Request(url)
        result = request.makeRequest()
        # Assert
        self.assertIsInstance(result, str)

    def test_invalid_url(self):
        # Assume
        url = 'http:://badurl..com'
        # Action
        request = Request(url)
        # Assert
        with self.assertRaises(urllib2.URLError):
            request.makeRequest()


if __name__ == '__main__':
    unittest.main()
