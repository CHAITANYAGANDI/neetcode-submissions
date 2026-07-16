class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen_elements= {}

        for key, value in enumerate(nums):
            difference = target - value

            if difference in already_seen_elements:
                return [already_seen_elements[difference], key]
            else:
                already_seen_elements[value] = key
        
        return []