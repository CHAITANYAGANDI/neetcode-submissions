class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # A permutation of s1 cannot exist inside s2
        # when s1 is longer than s2.
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        required_frequency = {}
        window_frequency = {}

        # Build the frequency map for s1
        # and for the first window of s2.
        for index in range(window_size):

            required_character = s1[index]
            required_frequency[required_character] = (
                required_frequency.get(required_character, 0) + 1
            )

            window_character = s2[index]
            window_frequency[window_character] = (
                window_frequency.get(window_character, 0) + 1
            )

        # Check the first window.
        if window_frequency == required_frequency:
            return True

        # Slide the fixed-size window through s2.
        for incoming_index in range(window_size, len(s2)):

            incoming_character = s2[incoming_index]

            outgoing_index = incoming_index - window_size
            outgoing_character = s2[outgoing_index]

            # Add the incoming character to the window.
            window_frequency[incoming_character] = (
                window_frequency.get(incoming_character, 0) + 1
            )

            # Remove the outgoing character from the window.
            window_frequency[outgoing_character] -= 1

            # Remove the key when its count becomes zero
            # so that the two dictionaries can be compared correctly.
            if window_frequency[outgoing_character] == 0:
                window_frequency.pop(outgoing_character)

            # Matching frequency maps mean the current substring
            # is a permutation of s1.
            if window_frequency == required_frequency:
                return True

        return False