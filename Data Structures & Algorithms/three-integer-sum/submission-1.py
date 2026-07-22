class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # ## Brute force approach

        # nums.sort()
        # result = set()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 triplet = [nums[i],nums[j],nums[k]]
        #                 result.add(tuple(triplet))
                    
        # return [list(distinct_triplets) for distinct_triplets in result]

        ## optimal approach

        result = []

        nums.sort()

        for i in range(len(nums)):

            # breaking the loop because the smallest possible number can't be 
            # determined beyond 0 as in [1,2,3,4]
            if nums[i] > 0:
                break # no future is possible (0)

            # skip the duplicate repeated after every index and index before that
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1

            while l < r:

                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum > 0:
                    
                    r-=1

                elif current_sum < 0:

                    l+=1

                else:

                    result.append([nums[i], nums[l], nums[r]])

                    # moving the left pointer to the right
                    l+=1
                    # moving the right pointer to the left
                    r-=1

                    # skipping the duplicates on the left side
                    while l < r and nums[l] == nums[l-1]:
                        
                        l+=1

                    # skipping the right side duplicates
                    while l < r and nums[r] == nums[r+1]:
                        
                        r-=1
        return result
        