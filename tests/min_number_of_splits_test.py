import unittest
from challenge.palindrome import Palindrome

input_strings = [
    ('noonabbadd', 'noon|abba|dd', 2),
    ('abaxyzzyxf', 'aba|xyzzyx|f', 2),
    ('nolemonnomelon aaaaaaaaaaaaabaaaaaaaaaaaa', 'nolemonnomelon|a|aaaaaaaaaaaabaaaaaaaaaaaa', 2),
    ('asd xxx nurses run xx', 'a|s|d|x|xxnursesrunxx', 4),
    ('racecar mom mom racecar racecar', 'racecarmommomracecar|racecar', 1),
    ('racecara', 'racecar|a', 1),
    ('aracecar', 'a|racecar', 1),
    ('caracecar', 'c|a|racecar', 2),
    ('abaaracecar', 'aba|a|racecar', 2),
]

failing_inputs = [
    ('aabaracecar', 'aba|a|racecar', 2)
]

class MinNumberOfSplitsTest(unittest.TestCase):
    def setUp(self):
        self.palindrome = Palindrome()

    def test_get_min_splits_on_string_palindromic_substrings(self):
        for input, expected_split, expected_count in input_strings:
            with self.subTest():
                input = self.palindrome.validate_input(input)
                splitted, count = self.palindrome.get_min_splits_on_string(input)
                self.assertEqual(count, expected_count)
                self.assertEqual(splitted, expected_split)
