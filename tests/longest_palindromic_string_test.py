import unittest
from challenge.palindrome import Palindrome

long_input_strings = [
    ('abaxyzzyxf', 'xyzzyx'),
    ('abaholaholaabaracecarholaabaaba', 'racecar'),
    ('nolemonnomelon aaaaaaaaaaaaabaaaaaaaaaaaa', 'aaaaaaaaaaaabaaaaaaaaaaaa'),
    ('njsnjj asd xxx nurses run xx aa nolemon no melon aaa xxx zz', 'aanolemonnomelonaa'),
    ('racecar mom maskd jammaj nxczb askmeemksa', 'askmeemksa'),
]

full_palindrome_inputs = [
    ('nomelon no lemon', 'nomelonnolemon'),
    ('race car', 'racecar'),
    ('aaabbbcccbbbaaa', 'aaabbbcccbbbaaa'),
    ('hannah', 'hannah'),
    ('bbb', 'bbb'),
]

class LongestPalindromicStringTest(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()

    def test_get_longest_palindromic_string(self):
        for input, expected in long_input_strings:
            with self.subTest():
                result = self.palindrome.get_longest_palindromic_string(input)
                self.assertEqual(result, expected)

    def test_get_longest_palindromic_string_on_palindromic_two_characters(self):
        input = "aa"
        expected = "aa"
        result = self.palindrome.get_longest_palindromic_string(input)
        self.assertEqual(result, expected)

    def test_get_longest_palindromic_string_on_full_palindromes(self):
        for input, expected in full_palindrome_inputs:
            with self.subTest():
                result = self.palindrome.get_longest_palindromic_string(input)
                self.assertEqual(result, expected)

    def test_get_longest_palindromic_string_on_one_character(self):
        input = "a"
        expected = "a"
        result = self.palindrome.get_longest_palindromic_string(input)
        self.assertEqual(result, expected)

    def test_get_longest_palindromic_string_on_non_palindromic_two_characters(self):
        input = "ab"
        expected = ""
        result = self.palindrome.get_longest_palindromic_string(input)
        self.assertEqual(result, expected)
