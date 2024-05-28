class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        rows, columns = len(grid), len(grid[0])
        local_max_matrix: list[list[int]] = [[0 for _ in range(columns - 2)] for _ in range(rows - 2)]

        for row in range(rows - 2):
            for column in range(columns - 2):
                local_max_matrix[row][column] = self.__get_max(grid, row, column)

        return local_max_matrix

    def __get_max(self, grid: list[list[int]], row: int, column: int) -> int:
        maximal_value = 0
        rows_count, columns_count = len(grid), len(grid[0])
        limit_row, limit_column = min(row + 3, rows_count), min(column + 3, columns_count)

        for sub_row in range(row, limit_row):
            for sub_column in range(column, limit_column):
                maximal_value = max(maximal_value, grid[sub_row][sub_column])

        return maximal_value
