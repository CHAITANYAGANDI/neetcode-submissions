class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ## Iterative approach

        # cars = []

        # # Calculate how long each car would take to reach
        # # the target if it were driving by itself.
        # for index in range(len(position)):

        #     arrival_time = (
        #         target - position[index]
        #     ) / speed[index]

        #     # Keep the car's position together with
        #     # its arrival time.
        #     cars.append(
        #         (position[index], arrival_time)
        #     )

        # # Process cars from closest to the target
        # # to farthest from the target.
        # cars.sort(reverse=True)

        # # The closest car always forms the first fleet.
        # fleet_count = 1

        # # Arrival time of the fleet directly ahead
        # # of the cars we are currently processing.
        # fleet_arrival_time = cars[0][1]

        # # Start from index 1 because the first car
        # # already created the first fleet.
        # for index in range(1, len(cars)):

        #     current_arrival_time = cars[index][1]

        #     # If the current car takes longer to reach the
        #     # target than the fleet ahead, it cannot catch
        #     # that fleet and therefore creates a new fleet.
        #     if current_arrival_time > fleet_arrival_time:

        #         fleet_count += 1

        #         # This new fleet is now the closest fleet
        #         # ahead for the remaining cars.
        #         fleet_arrival_time = current_arrival_time

        #     # Otherwise:
        #     # current_arrival_time <= fleet_arrival_time
        #     #
        #     # The current car catches the fleet ahead,
        #     # so they become one fleet.
        #     # No update is required.

        # return fleet_count


        # Stack approach

        cars = []

        # Calculate each car's individual arrival time
        # and store it together with its position.
        for index in range(len(position)):

            arrival_time = (
                target - position[index]
            ) / speed[index]

            cars.append(
                (position[index], arrival_time)
            )

        # Sort from the car closest to the target
        # to the car farthest from the target.
        cars.sort(reverse=True)

        # Stack stores the arrival time of every
        # separate fleet discovered so far.
        fleet_stack = []

        for car_position, arrival_time in cars:

            # If there are no fleets yet, the current car
            # automatically creates the first fleet.
            if not fleet_stack:

                fleet_stack.append(arrival_time)

            # If this car takes longer than the fleet ahead,
            # it cannot catch that fleet, so it becomes
            # a new separate fleet.
            elif arrival_time > fleet_stack[-1]:

                fleet_stack.append(arrival_time)

            # Otherwise:
            # arrival_time <= fleet_stack[-1]
            #
            # The current car catches the fleet ahead,
            # so we do not add another fleet to the stack.

        # Each value remaining in the stack
        # represents one separate fleet.
        return len(fleet_stack)
        