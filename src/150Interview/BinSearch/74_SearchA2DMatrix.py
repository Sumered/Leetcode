class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        column_left, column_right = 0, len(matrix)
        row_left, row_right = 0, len(matrix[0])

        while column_left < column_right:
            medium = (column_left + column_right) // 2
            if matrix[medium][0] > target:
                column_right = medium
            else:
                column_left = medium + 1

        column_left -= 1

        while row_left < row_right:
            medium = (row_left + row_right) // 2
            if matrix[column_left][medium] > target:
                row_right = medium
            elif matrix[column_left][medium] < target:
                row_left = medium + 1
            else:
                return True

        return False
