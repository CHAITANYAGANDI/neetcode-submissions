class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left_index = 0
        right_index = 0

        character_frequency = {}
        highest_frequency = 0
        maximum_length = 0

        while right_index < len(s):

            current_character = s[right_index]

            # Add the current character to the window
            character_frequency[current_character] = (
                character_frequency.get(current_character, 0) + 1
            )

            # Track the highest character frequency seen
            highest_frequency = max(
                highest_frequency,
                character_frequency[current_character]
            )

            # Shrink the window if more than k replacements are needed
            while (
                right_index - left_index + 1
                - highest_frequency
                > k
            ):

                outgoing_character = s[left_index]
                character_frequency[outgoing_character] -= 1

                left_index += 1

            # Update the longest valid window
            current_window_length = (
                right_index - left_index + 1
            )

            maximum_length = max(
                maximum_length,
                current_window_length
            )

            right_index += 1

        return maximum_length
        