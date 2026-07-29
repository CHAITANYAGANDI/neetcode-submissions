class Solution:
    def findMin(self, nums: List[int]) -> int:

        # # Brute Force Approach

        # min = nums[0]

        # for i in nums:

        #     if i <= min:

        #         min = i

        # return min

        # Optimized

        left = 0
        right = len(nums) - 1
        
        # Continue until only one possible position remains
        while left < right:

            mid = (left + right) // 2

            # Minimum must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is either mid or somewhere to its left
            else:
                right = mid

        # left == right, so both pointers are now
        # pointing at the minimum element.
        return nums[left]
                