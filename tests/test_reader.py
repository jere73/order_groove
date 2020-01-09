import unittest

from src.reader import Reader
from src.request import Request


class TestReader(unittest.TestCase):

    def test_invalid_feed(self):
        # Assume
        value = 5
        # Action
        reader = Reader()
        # Assert
        with self.assertRaises(TypeError):
            reader.feed(value)

    def test_success_reader(self):
        # Assume
        html = '<HTML><HEAD><TITLE>Ejemplo 2</TITLE></HEAD><BODY></BODY></HTML>'
        # Action
        reader = Reader()
        reader.feed(html)
        metrics = reader.get_metrics()
        # Assert
        self.assertEqual(metrics['total_elements'], 4)

        # Assume
        html2 = '<HTML><HEAD><IMG /><TITLE>Ejemplo 2</TITLE></HEAD><BODY></BODY></HTML>'
        # Action
        reader2 = Reader()
        reader2.feed(html2)
        metrics2 = reader2.get_metrics()
        # Assert
        self.assertEqual(metrics2['total_elements'], 5)

        # Assume
        html3 = '<HTML><HEAD><BADTAG><TITLE>Ejemplo 2</TITLE></HEAD><BADTAG><BODY></BODY></HTML>'
        # Action
        reader3 = Reader()
        reader3.feed(html3)
        metrics3 = reader3.get_metrics()
        # Assert
        self.assertEqual(metrics3['total_elements'], 4)

if __name__ == '__main__':
    unittest.main()
