class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        result = 0
        rows_count, columns_count = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(columns_count)] for _ in range(rows_count)]

        for row_index in range(rows_count):
            for column_index in range(columns_count):
                if matrix[row_index][column_index] == "1":
                    up_value = dp[row_index - 1][column_index] + 1 if row_index >= 1 else 1
                    left_value = dp[row_index][column_index - 1] + 1 if column_index >= 1 else 1
                    diagonal_value = dp[row_index - 1][column_index - 1] + 1 if row_index >= 1 and column_index >= 1 else 1
                    dp[row_index][column_index] = min(up_value, left_value, diagonal_value)
                    result = max(result, dp[row_index][column_index] ** 2)

        return result
