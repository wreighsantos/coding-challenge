from typing import Text


class Palindrome:
    def is_palindrome(self, text):
        """Check if a string is a palindrome."""
        text = self._validate_input(text)
        text_length = len(text)

        start = 0
        end = text_length - 1
        middle = text_length // 2

        if text_length % 2 == 0:
            middle -= 1

        while not start > middle:
            if text[start] != text[end]:
                return False
            start += 1
            end -= 1

        return True

    def _validate_input(self, input):
        if not (type(input) == str):
            raise ValueError("Input must be a string")

        input = input.replace(" ", "")

        if not input:
            raise ValueError("Input must contain at least 1 character")

        return input.lower()
