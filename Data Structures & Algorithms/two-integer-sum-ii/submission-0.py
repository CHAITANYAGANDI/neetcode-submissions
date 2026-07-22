class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # ## Brute Force approach

        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1, j+1]

        # return []

        ## optimized approach
        left, right = 0, len(numbers)-1

        while left < right:
            
            if numbers[left]+numbers[right] > target :
                right-=1
                
            elif numbers[left]+numbers[right] < target :
                left+=1
                
            else:
                return [left+1, right+1]
                
        return[]