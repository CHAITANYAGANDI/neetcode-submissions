class Solution:
    def trap(self, height: List[int]) -> int:

        # Brute Force approach  -- by iterating through whole array
        # n = len(height)
        # res = 0

        # for i in range(n):
        #     left_max = right_max = height[i]
            
        #     for j in range(i):
        #         left_max = max(left_max, height[j])
                
        #     for j in range(i+1, n):
                
        #         right_max = max(right_max, height[j])
                
        #     res+= min(left_max, right_max) - height[i]
            
        # return res


        #Optimal approach using 

        left_pointer = 0

        right_pointer = len(height)-1

        left_max = height[left_pointer]
            
        right_max = height[right_pointer]

        res = 0

        while left_pointer < right_pointer:
            
            if left_max < right_max:
                
                left_pointer+=1
                left_max = max(left_max, height[left_pointer])
                res += left_max - height[left_pointer]
                
            else:
                
                right_pointer-=1
                right_max = max(right_max, height[right_pointer])
                res += right_max - height[right_pointer]
                
        return res
        