import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # --------------------------------------------------
        # Approach 1: Brute force using regular expressions
        # --------------------------------------------------

        # cleaned_string = re.sub(r'[^\w\s]', '', s)
        # cleaned_string = (
        #     cleaned_string
        #     .replace(' ', '')
        #     .replace('_', '')
        #     .lower()
        # )

        # characters = list(cleaned_string)

        # current_index = len(characters)
        # reversed_characters = []

        # for _ in range(len(characters)):
        #     current_index -= 1
        #     reversed_characters.append(characters[current_index])

        # reversed_string = ''.join(reversed_characters)

        # return cleaned_string == reversed_string


        # --------------------------------------------------
        # Approach 2: Brute force using isalnum()
        # --------------------------------------------------

        # cleaned_string = ""

        # for character in s:
        #     if character.isalnum():
        #         cleaned_string += character.lower()

        # return cleaned_string == cleaned_string[::-1]


        # --------------------------------------------------
        # Approach 3: Optimized two-pointer approach
        # --------------------------------------------------

        def is_alphanumeric(character: str) -> bool:
            return (
                ord('A') <= ord(character) <= ord('Z')
                or ord('a') <= ord(character) <= ord('z')
                or ord('0') <= ord(character) <= ord('9')
            )

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:

            # Skip non-alphanumeric characters from the left.
            while (
                left_pointer < right_pointer
                and not is_alphanumeric(s[left_pointer])
            ):
                left_pointer += 1

            # Skip non-alphanumeric characters from the right.
            while (
                left_pointer < right_pointer
                and not is_alphanumeric(s[right_pointer])
            ):
                right_pointer -= 1

            # Compare both characters without considering case.
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False

            left_pointer += 1
            right_pointer -= 1

        return True