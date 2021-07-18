class Palindrome:
    def is_palindrome(self, text):
        """Check if a string is a palindrome."""
        text = self.validate_input(text)
        text_length = len(text)

        start = 0
        end = text_length - 1
        middle = self._get_string_middle_index(text)

        while not start > middle:
            if text[start] != text[end]:
                return False
            start += 1
            end -= 1

        return True

    def get_longest_palindromic_string(self, text):
        """Get the longest palindromic string in a string"""
        text = self.validate_input(text)
        text_length = len(text)

        start = 0
        end = text_length - 1
        previous_start = -1
        previous_end = -1

        longest_palindrome = ""

        while start <= end:
            moving_start = start
            moving_end = end

            while moving_end >= moving_start:
                # we're probably navigating inside the previously added palindrome
                if start > previous_start and end < previous_end:
                    break

                if text[moving_start] == text[moving_end]:
                    moving_start += 1
                    moving_end -= 1
                else:
                    moving_start = start
                    end -= 1
                    moving_end = end

            if not (start > previous_start and end < previous_end):
                current_palindrome = text[start:end + 1]
                if len(longest_palindrome) < len(current_palindrome):
                    longest_palindrome = current_palindrome
                previous_start = start
                previous_end = end

            start += 1
            end = text_length - 1

        return longest_palindrome

    def validate_input(self, input):
        """Validate input for palindrome actions."""
        if not (type(input) == str):
            raise ValueError("Input must be a string")

        input = input.replace(" ", "")

        if not input:
            raise ValueError("Input must contain at least 1 character")

        return input.lower()

    def _get_string_middle_index(self, text):
        """Compute the middle index of a string."""
        middle = len(text) // 2
        if len(text) % 2 == 0:
            return middle - 1
        return middle
