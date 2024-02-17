class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows_sum, columns_sum = [], []
        rows_count, columns_count = len(grid), len(grid[0])
        diff_grid = [[0 for _ in range(columns_count)] for _ in range(rows_count)]

        for row in grid:
            rows_sum.append(sum(row))

        for column_index in range(columns_count):
            column_sum = 0
            for row_index in range(rows_count):
                column_sum += grid[row_index][column_index]
            columns_sum.append(column_sum)

        for row_index in range(rows_count):
            for column_index in range(columns_count):
                ones_sum = rows_sum[row_index] + columns_sum[column_index]
                zeros_sum = rows_count + columns_count - ones_sum
                diff_grid[row_index][column_index] = ones_sum - zeros_sum

        return diff_grid
