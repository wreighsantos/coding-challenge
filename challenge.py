import sys
from challenge.palindrome import Palindrome

def main():
    input_action = sys.argv[1]
    input_string = sys.argv[2]

    if input_string is None or input_action is None:
        raise ValueError("Missing inputs")

    palindrome = Palindrome()

    if input_action == "-level1":
        print(
            "Is palindrome? {}".format(palindrome.is_palindrome(input_string))
        )
    elif input_action == "-level2":
        print(
            "Longest palindrome: {}".format(
                palindrome.get_longest_palindromic_string(input_string)
            )
        )
    elif input_action == "-level3":
        splitted, count = palindrome.get_min_splits_on_string(input_string)
        print(splitted)
        print(count)
    else:
        raise NotImplementedError

if __name__ == "__main__":
    main()
