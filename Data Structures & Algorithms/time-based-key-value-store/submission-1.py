class TimeMap:

    def __init__(self):
        # Maps each key to a list of:
        # (timestamp, value)
        #
        # Example:
        # {
        #     "alice": [(1, "happy"), (3, "sad")]
        # }
        self.key_history = {}

    def set(
        self,
        key: str,
        value: str,
        timestamp: int
    ) -> None:

        # Create an empty history when the key
        # is being stored for the first time.
        if key not in self.key_history:
            self.key_history[key] = []

        # Timestamps are guaranteed to arrive in
        # strictly increasing order, so appending
        # keeps the history sorted by timestamp.
        self.key_history[key].append(
            (timestamp, value)
        )

    def get(self, key: str, timestamp: int) -> str:

        # Return an empty string when no valid
        # timestamp exists.
        result_value = ""

        # Get the complete timestamp history for this key.
        # If the key does not exist, use an empty list.
        timestamped_values = self.key_history.get(key, [])

        left_index = 0
        right_index = len(timestamped_values) - 1

        # Find the largest stored timestamp that is
        # less than or equal to the requested timestamp.
        while left_index <= right_index:

            middle_index = (
                left_index + right_index
            ) // 2

            stored_timestamp, stored_value = (
                timestamped_values[middle_index]
            )

            # This timestamp is valid.
            # Save its value and search toward the right
            # for a later timestamp that may also be valid.
            if stored_timestamp <= timestamp:
                result_value = stored_value
                left_index = middle_index + 1

            # This timestamp is too large, so search
            # among earlier timestamps.
            else:
                right_index = middle_index - 1

        return result_value