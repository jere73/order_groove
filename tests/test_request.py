import unittest
import urllib2

from src.request import Request


class TestRequest(unittest.TestCase):

    def test_requests(self):
        # Assume
        url = 'https://www.ole.com.ar/river-plate/'
        # Action
        request = Request()
        result = request.makeRequest(url)
        # Assert
        self.assertIsInstance(result, str)

    def test_invalid_url(self):
        # Assume
        url = 'http:://badurl..com'
        # Action
        request = Request()
        # Assert
        with self.assertRaises(urllib2.URLError):
            request.makeRequest(url)


if __name__ == '__main__':
    unittest.main()
