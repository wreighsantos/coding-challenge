import unittest
from challenge.palindrome import Palindrome

class PalindromeTest(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()

    def test_even_lengthed_string_is_palindrome(self):
        two_character_input = "bb"
        more_character_input = "hannah"

        res_two_characters = self.palindrome.is_palindrome(two_character_input)
        res_more_characters = self.palindrome.is_palindrome(more_character_input)

        self.assertTrue(res_two_characters)
        self.assertTrue(res_more_characters)

    def test_odd_lengthed_string_is_palindrome(self):
        one_character_input = "a"
        more_character_input = "racecar"

        res_one_character = self.palindrome.is_palindrome(one_character_input)
        res_more_characters = self.palindrome.is_palindrome(more_character_input)

        self.assertTrue(res_one_character)
        self.assertTrue(res_more_characters)

    def test_palindrome_with_whitespace_is_palindrome(self):
        input = "never odd or even"
        result = self.palindrome.is_palindrome(input)
        self.assertTrue(result)

    def test_palindrome_with_different_capitalization_is_palindrome(self):
        input = "AabCBAa"
        result = self.palindrome.is_palindrome(input)
        self.assertTrue(result)

    def test_even_lengthed_string_is_not_palindrome(self):
        two_character_input = "ba"
        more_character_input = "notapalindrome"

        res_two_characters = self.palindrome.is_palindrome(two_character_input)
        res_more_characters = self.palindrome.is_palindrome(more_character_input)

        self.assertFalse(res_two_characters)
        self.assertFalse(res_more_characters)

    def test_odd_lengthed_string_is_not_palindrome(self):
        input = "notpalindrome"
        result = self.palindrome.is_palindrome(input)
        self.assertFalse(result)

    def test_is_palindrome_input_is_not_a_string(self):
        input = 1
        with self.assertRaises(ValueError):
            self.palindrome.is_palindrome(input)

    def test_is_palindrome_input_string_is_empty(self):
        input = ""
        with self.assertRaises(ValueError):
            self.palindrome.is_palindrome(input)

    def test_is_palindrome_all_space_input_string(self):
        input = "           "
        with self.assertRaises(ValueError):
            self.palindrome.is_palindrome(input)
