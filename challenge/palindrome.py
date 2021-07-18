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
                if start > previous_start and end <= previous_end:
                    break

                if text[moving_start] == text[moving_end]:
                    moving_start += 1
                    moving_end -= 1
                else:
                    moving_start = start
                    end -= 1
                    moving_end = end

            if not (start > previous_start and end <= previous_end):
                current_palindrome = text[start:end + 1]
                if len(longest_palindrome) < len(current_palindrome):
                    longest_palindrome = current_palindrome
                previous_start = start
                previous_end = end

            start += 1
            end = text_length - 1

        return longest_palindrome

    def get_min_splits_on_string(self, text):
        """
        Splits a string in the least possible number of splits
        so that its substrings are all palindromes.

        Returns the splitted string representation and the total number of splits done.
        """
        text = self.validate_input(text)
        splitted = self._split_string_to_palindromic_substrings(text)
        representation = "|".join(splitted)
        return representation, len(splitted) - 1

    def _split_string_to_palindromic_substrings(self, text):
        palindromes = self._extract_palindromes(text)

        splits = []

        for palindrome in palindromes:
            # if overlapping palindromes, let's decide by checking which
            # overlap remainder needs the least count of splits
            if type(palindrome) == OverlappingPalindromes:
                right_remainder_splitted = self._split_string_to_palindromic_substrings(
                    palindrome.right_remainder,
                )
                left_remainder_splitted = self._split_string_to_palindromic_substrings(
                    palindrome.left_remainder,
                )

                if len(right_remainder_splitted) <= len(left_remainder_splitted):
                    splits.append(palindrome.left_palindrome)
                    splits.extend(right_remainder_splitted)
                else:
                    splits.extend(left_remainder_splitted)
                    splits.append(palindrome.right_palindrome)
            else:
                splits.append(palindrome)

        return splits

    def _extract_palindromes(self, text):
        """
        Extracts all palindromes from a string. Overlapping palindromes are grouped.
        """
        text_length = len(text)

        start = 0
        end = text_length - 1
        previous_start = -1
        previous_end = -1

        palindromes = []

        while start <= end:
            moving_start = start
            moving_end = end

            while moving_end >= moving_start:
                # we're probably navigating inside the previously added palindrome
                if start > previous_start and end <= previous_end:
                    break

                if text[moving_start] == text[moving_end]:
                    moving_start += 1
                    moving_end -= 1
                else:
                    moving_start = start
                    end -= 1
                    moving_end = end

            if not (start > previous_start and end <= previous_end):
                current_palindrome = text[start:end + 1]

                # group overlapping palindromes
                if (previous_start < start <= previous_end or
                    previous_start < end < previous_end):
                    left_remainder_string = text[
                        previous_start:start
                    ]
                    right_remainder_string = text[
                        previous_end + 1:end + 1
                    ]
                    previous_palindrome = palindromes.pop()

                    # more than two overlapping palindromes
                    if type(previous_palindrome) == OverlappingPalindromes:
                        right_remainder_splitted = self._split_string_to_palindromic_substrings(
                            previous_palindrome.right_remainder,
                        )
                        left_remainder_splitted = self._split_string_to_palindromic_substrings(
                            previous_palindrome.left_remainder,
                        )

                        if len(right_remainder_splitted) <= len(left_remainder_splitted):
                            palindromes.append(previous_palindrome.left_palindrome)
                            middle_remainder_string = text[
                                previous_start + 1:start
                            ]
                            if middle_remainder_string:
                                palindromes.append(middle_remainder_string)
                        else:
                            palindromes.extend(left_remainder_splitted)
                            palindromes.append(previous_palindrome.right_palindrome)

                        palindromes.append(current_palindrome)

                    else:
                        palindromes.append(OverlappingPalindromes(
                            left_palindrome=previous_palindrome,
                            right_palindrome=current_palindrome,
                            left_remainder=left_remainder_string,
                            right_remainder=right_remainder_string,
                        ))
                else:
                    palindromes.append(current_palindrome)

                previous_start = start
                previous_end = end

            start += 1
            end = text_length - 1

        return palindromes

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

class OverlappingPalindromes:
    def __init__(
        self,
        left_palindrome,
        right_palindrome,
        left_remainder,
        right_remainder,
    ):
        self.left_palindrome = left_palindrome
        self.right_palindrome = right_palindrome
        self.left_remainder = left_remainder
        self.right_remainder = right_remainder
