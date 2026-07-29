import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # # Brute force approach

        # eating_speed = 1

        # while True:

        #     # Calculate the total number of hours required
        #     # for the current eating speed
        #     total_hours = 0

        #     for pile_size in piles:
        #         total_hours += math.ceil(pile_size / eating_speed)

        #     # If Koko can finish within the allowed hours,
        #     # this is the minimum valid speed because we started from 1
        #     if total_hours <= h:
        #         return eating_speed

        #     # Current speed is too slow, so try the next speed
        #     eating_speed += 1

        # return eating_speed

        # Optimized approach

        import math

        # Minimum possible eating speed
        minimum_speed = 1

        # Maximum useful eating speed is the largest pile
        maximum_speed = max(piles)

        # Start with the maximum speed as a guaranteed valid answer
        minimum_valid_speed = maximum_speed

        while minimum_speed <= maximum_speed:

            # Try the middle eating speed
            middle_speed = (minimum_speed + maximum_speed) // 2

            # Calculate how many hours Koko needs
            # if she eats at middle_speed bananas per hour
            total_hours = 0

            for pile_size in piles:
                total_hours += math.ceil(pile_size / middle_speed)

            # If this speed allows Koko to finish on time,
            # remember it and search for a smaller valid speed
            if total_hours <= h:

                minimum_valid_speed = middle_speed
                maximum_speed = middle_speed - 1

            # Otherwise, this speed is too slow,
            # so search for a larger eating speed
            else:

                minimum_speed = middle_speed + 1

        return minimum_valid_speed
        