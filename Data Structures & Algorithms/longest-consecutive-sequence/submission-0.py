class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Optimal Solution

        # this is to get rid of duplciates
        input_values = set(nums)

        longest = 0

        for each_element in input_values:
            # check if the number is the starting of the sequence by taking
            # the difference of current value and check in the input values if not
            # assign length 1
            if(each_element - 1) not in input_values:

                length = 1

                # loop until there is sequence and keep increasing the length or else
                # move on to the next element
                while(each_element + length) in input_values:
                    
                    length+=1

                longest = max(length, longest)

        return longest
        