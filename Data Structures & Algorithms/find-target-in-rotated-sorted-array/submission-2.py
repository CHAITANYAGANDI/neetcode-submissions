class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Brute Force approach

        # for i in nums:

        #     if i == target:

        #         return i

        # return -1


        # Optimized approach


        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:

            middle_index = (left_index + right_index) // 2

            # Target found
            if nums[middle_index] == target:
                return middle_index

            # ------------------------------------------------
            # Case 1: Left half is sorted
            # ------------------------------------------------
            if nums[left_index] <= nums[middle_index]:

                # Check whether target lies inside
                # the sorted left half
                if (
                    nums[left_index] <= target
                    and target < nums[middle_index]
                ):
                    # Target must be on the left
                    right_index = middle_index - 1

                else:
                    # Target must be on the right
                    left_index = middle_index + 1

            # ------------------------------------------------
            # Case 2: Right half is sorted
            # ------------------------------------------------
            else:

                # Check whether target lies inside
                # the sorted right half
                if (
                    nums[middle_index] < target
                    and target <= nums[right_index]
                ):
                    # Target must be on the right
                    left_index = middle_index + 1

                else:
                    # Target must be on the left
                    right_index = middle_index - 1

        # Target does not exist in the array
        return -1