class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Stores values from the previous k indices
        window_values = set()

        # Left boundary of the current window
        left_index = 0

        for right_index in range(len(nums)):

            current_value = nums[right_index]

            # If the current value already exists in the window,
            # the same value appeared within the previous k positions
            if current_value in window_values:
                return True

            # Add the current value to the window
            window_values.add(current_value)

            # Keep at most k previous values in the set
            if right_index - left_index >= k:

                # Remove the value that is now too far away
                window_values.remove(nums[left_index])

                # Move the left boundary forward
                left_index += 1

        # No nearby duplicate was found
        return False