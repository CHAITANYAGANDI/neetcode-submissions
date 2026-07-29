class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Brute Force approach

        # Traverse through every row in the matrix
        # for row_index in range(len(matrix)):

        #     # Traverse through every column in the current row
        #     for column_index in range(len(matrix[0])):

        #         # If the current value matches the target,
        #         # the target exists in the matrix
        #         if matrix[row_index][column_index] == target:
        #             return True

        # # Target was not found after checking every element
        # return False

        # optimized approach

        total_rows = len(matrix)
        total_columns = len(matrix[0])

        # -------------------------------------------------
        # First binary search:
        # Find the row that could contain the target
        # -------------------------------------------------

        top_row = 0
        bottom_row = total_rows - 1

        while top_row <= bottom_row:

            middle_row = (top_row + bottom_row) // 2

            # Target is greater than the largest value
            # in this row, so search the rows below
            if target > matrix[middle_row][-1]:
                top_row = middle_row + 1

            # Target is smaller than the smallest value
            # in this row, so search the rows above
            elif target < matrix[middle_row][0]:
                bottom_row = middle_row - 1

            # Target lies within the range of this row
            else:
                break

        # If the row pointers crossed, no row can
        # possibly contain the target
        if top_row > bottom_row:
            return False

        # This is the row where the target could exist
        target_row = (top_row + bottom_row) // 2


        # -------------------------------------------------
        # Second binary search:
        # Search for the target inside the selected row
        # -------------------------------------------------

        left_column = 0
        right_column = total_columns - 1

        while left_column <= right_column:

            middle_column = (
                left_column + right_column
            ) // 2

            current_value = matrix[target_row][middle_column]

            # Target is larger, so search the right half
            if target > current_value:
                left_column = middle_column + 1

            # Target is smaller, so search the left half
            elif target < current_value:
                right_column = middle_column - 1

            # Target found
            else:
                return True

        # Target does not exist in the selected row
        return False


        