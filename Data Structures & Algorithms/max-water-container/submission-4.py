class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # # Brute Force approach
        # res = 0

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area = (j-i) * min(heights[i], heights[j])
        #         res = max(res,area)
            
    

        # optimal approach

        left_pointer = 0
        right_pointer = len(heights) - 1
        result = 0

        while left_pointer < right_pointer:
            
            area =  (right_pointer-left_pointer) * min(heights[left_pointer],
            heights[right_pointer])
            
            result = max(result,area)
            
            # moving pointer to the right if the height of left bar is less 
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer+=1
            # moving the pointer to the left if the height of right bar is less
            elif heights[left_pointer] > heights[right_pointer]:
                right_pointer-=1
            # moving the right pointer to the left if both heights are same
            else:
                right_pointer-=1
                
        return result