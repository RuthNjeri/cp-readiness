import unittest
from application import even_numbers

class TestEvenNumbers(unittest.TestCase):

    def test_even(self):
        self.assertTrue(even_numbers.number(2))

    def test_not_even(self):
        self.assertFalse(even_numbers.number(3))    

    def test_if_number_is_integer(self):
        with self.assertRaises(ValueError):
            even_numbers.number("one")  

    def test_if_number_is_positive(self):
        with self.assertRaises(ValueError):
            even_numbers.number(-1)          


if __name__ == '__main__':
    unittest.main()        