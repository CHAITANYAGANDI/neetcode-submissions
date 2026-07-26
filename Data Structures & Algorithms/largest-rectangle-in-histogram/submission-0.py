class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # Brute Force Approach

        # max_area = 0

        # # Choose the starting index of the rectangle
        # for start_index in range(len(heights)):

        #     # At first, the minimum height is the starting bar itself
        #     minimum_height = heights[start_index]

        #     # Expand the rectangle toward the right
        #     for end_index in range(start_index, len(heights)):

        #         # Update the shortest bar seen in the current range
        #         minimum_height = min(
        #             minimum_height,
        #             heights[end_index]
        #         )

        #         # Number of bars between start and end, inclusive
        #         width = end_index - start_index + 1

        #         # Rectangle height is limited by the shortest bar
        #         current_area = minimum_height * width

        #         # Keep track of the largest area found
        #         max_area = max(max_area, current_area)

        # return max_area

        ## Optimal approach

        max_area = 0

        # Stack stores:
        # (starting_index, bar_height)
        #
        # starting_index tells us how far left this height
        # can extend while still forming a valid rectangle.
        monotonic_stack = []

        for current_index in range(len(heights)):

            current_height = heights[current_index]

            # Initially, the current bar can start
            # from its own index.
            start_index = current_index

            # If the current bar is shorter than the bar
            # at the top of the stack, the taller bar
            # cannot extend any farther to the right.
            while (
                monotonic_stack
                and monotonic_stack[-1][1] > current_height
            ):

                previous_start_index, previous_height = (
                    monotonic_stack.pop()
                )

                # The previous rectangle extends from
                # previous_start_index up to current_index - 1.
                rectangle_width = (
                    current_index - previous_start_index
                )

                current_area = (
                    previous_height * rectangle_width
                )

                max_area = max(
                    max_area,
                    current_area
                )

                # The current shorter bar can extend left
                # to where the taller popped bar started.
                start_index = previous_start_index

            # Store the current height along with the earliest
            # position from which it can form a rectangle.
            monotonic_stack.append(
                (start_index, current_height)
            )


        # Bars still in the stack never encountered
        # a shorter bar on their right.
        #
        # Therefore, their rectangles can extend
        # all the way to the end of the histogram.
        for start_index, height in monotonic_stack:

            rectangle_width = (
                len(heights) - start_index
            )

            current_area = (
                height * rectangle_width
            )

            max_area = max(
                max_area,
                current_area
            )

        return max_area