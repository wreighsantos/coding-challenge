import unittest
from challenge.palindrome import Palindrome

class PalindromeTest(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()

    def test_input_is_not_a_string(self):
        input = 1
        with self.assertRaises(ValueError):
            self.palindrome.validate_input(input)

    def test_input_string_is_empty(self):
        input = ""
        with self.assertRaises(ValueError):
            self.palindrome.validate_input(input)

    def test_all_space_input_string(self):
        input = "           "
        with self.assertRaises(ValueError):
            self.palindrome.validate_input(input)
