import unittest

from src.reader import Reader


class TestReader(unittest.TestCase):

    def test_invalid_feed(self):
        # Assume
        value = 5
        # Action
        reader = Reader()
        # Assert
        with self.assertRaises(TypeError):
            reader.feed(value)


if __name__ == '__main__':
    unittest.main()
