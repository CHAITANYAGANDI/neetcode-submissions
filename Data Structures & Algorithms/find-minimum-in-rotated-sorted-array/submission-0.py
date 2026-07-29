class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # Minimum must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is either mid or somewhere to its left
            else:
                right = mid

        return nums[left]
                