class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows_count, columns_count = len(grid), len(grid[0])
        dp = [[10001 for _ in range(columns_count + 1)] for _ in range(rows_count + 1)]
        dp[0][1] = 0
        for row_index in range(1, rows_count + 1):
            for column_index in range(1, columns_count + 1):
                up_value = dp[row_index - 1][column_index]
                left_value = dp[row_index][column_index - 1]
                dp[row_index][column_index] = min(left_value, up_value) + grid[row_index - 1][column_index - 1]

        return dp[rows_count][columns_count]
