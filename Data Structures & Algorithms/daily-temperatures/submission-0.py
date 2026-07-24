class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ## Brute Force Approach


        # Stores the number of days we need to wait
        # for a warmer temperature for each day
        # output = []

        # # Take each day as the current day
        # for i in range(len(temperatures)):

        #     # Start checking from the next day
        #     j = i + 1

        #     # Search all future days for the first warmer temperature
        #     while j < len(temperatures):

        #         # If a future day is warmer than the current day
        #         if temperatures[j] > temperatures[i]:

        #             # Difference between indexes gives
        #             # the number of days we had to wait
        #             output.append(j - i)

        #             # Stop searching because we only need
        #             # the first warmer future day
        #             break

        #         else:
        #             # Current future day is not warmer,
        #             # so check the next future day
        #             j += 1

        #     # This runs only if the while loop finishes
        #     # without finding a warmer day (without hitting break)
        #     else:
        #         output.append(0)

        # return output
        
    
        ## Optimized approach

        # Stack stores indexes of days that are still
        # waiting for a warmer temperature
        stack = []

        # Initialize result with 0 because if no warmer day
        # is found, the answer should remain 0
        output = [0] * len(temperatures)

        # Traverse through each day's temperature
        for i in range(len(temperatures)):

            # Check whether the current temperature is warmer
            # than the temperature of the day at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Remove the previous day that has now
                # found its next warmer temperature
                previous_day_index = stack.pop()

                # Difference between indexes gives the number
                # of days we had to wait for a warmer temperature
                output[previous_day_index] = i - previous_day_index

            # Current day has not found a future warmer day yet,
            # so store its index in the stack
            stack.append(i)

        return output