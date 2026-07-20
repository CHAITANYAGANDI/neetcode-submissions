class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # brute force approach

        # output = []

        # for i in range(len(nums)):
        #     pr = 1

        #     for j in range(len(nums)):
        #         if i != j:
        #             pr *= nums[j]

        #     output.append(pr)

        # return output
 
        ## Better approach than brute force approach

        # pre = []
        # pos = []    
        
        # pre_product = 1
        # pos_product = 1

        # for i in range(len(nums)):
        #     pre_product*=nums[i]
        #     pre.append(pre_product)

        # for j in range(len(nums)-1,-1,-1):
        #     pos_product*=nums[j]
        #     pos.append(pos_product)
            
        # pos = pos[::-1]

        # output = []

        # for k in range(len(nums)):
        #     dec = k - 1
        #     inc = k + 1
        #     if dec < 0:
        #         # No elements on the left
        #         value = pos[inc]

        #     elif inc > len(nums) - 1:
        #         # No elements on the right
        #         value = pre[dec]

        #     else:
        #         value = pre[dec] * pos[inc]

        #     output.append(value)
                
        # return output

        ## optimal approach

        result = [1] * len(nums)

        prefix = 1

        for index_value in range(len(nums)):
            # assigning prefix values to the result in the respective index positions
            result[index_value] = prefix

            # finding the prefix value by multiplying in a linear order
            prefix*=nums[index_value]
                
        postfix = 1

        for index_value in range(len(nums)-1,-1,-1):
            # product of prefix product values in the result list and each postfix value to get the output result
            result[index_value]*= postfix
            # finding the postfix values by multiplying in a reverse order of the list
            postfix*= nums[index_value]

        return result