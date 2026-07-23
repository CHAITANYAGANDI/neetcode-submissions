class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ## Brute force approach

        # for row_index in range(9):

        #     seen_values = set()

        #     for column_index in range(9):

        #         current_value = board[row_index][column_index]

        #         if current_value == ".":
        #             continue

        #         if current_value in seen_values:
        #             return False

        #         seen_values.add(current_value)


        # for column_index in range(9):

        #     seen_values = set()

        #     for row_index in range(9):

        #         current_value = board[row_index][column_index]

        #         if current_value == ".":
        #             continue

        #         if current_value in seen_values:
        #             return False

        #         seen_values.add(current_value)


        # for box_index in range(9):

        #     seen_values = set()

        #     for row_offset in range(3):

        #         for column_offset in range(3):

        #             # // 3 → which row of squares?

        #             # % 3  → which column of squares?

        #             # * 3  → where does that square start?

        #             # +i   → move through rows inside the square

        #             # +j   → move through columns inside the square

        #             row_index = (box_index // 3) * 3 + row_offset
        #             column_index = (box_index % 3) * 3 + column_offset

        #             current_value = board[row_index][column_index]

        #             if current_value == ".":
        #                 continue

        #             if current_value in seen_values:
        #                 return False

        #             seen_values.add(current_value)

        # return True



    

    ## Optimal approach

        row_values = defaultdict(set)
        column_values = defaultdict(set)
        box_values = defaultdict(set)

        for row_index in range(9):

            for column_index in range(9):

                current_value = board[row_index][column_index]

                if current_value == ".":
                    continue

                # Convert the current row and column into a 3x3 box position
                # Example: row 4, col 7 -> box (1, 2)

                box_position = (
                    row_index // 3,
                    column_index // 3
                )

                if (
                    current_value in row_values[row_index]
                    or current_value in column_values[column_index]
                    or current_value in box_values[box_position]
                ):
                    return False

                row_values[row_index].add(current_value)
                column_values[column_index].add(current_value)
                box_values[box_position].add(current_value)

        return True

                    



            
        