class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 and n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        obstacleGrid[0][0] = 1

        for row_index in range(m):
            for column_index in range(n):
                if obstacleGrid[row_index][column_index] != 1:
                    from_top = dp[row_index - 1][column_index] if row_index - 1 >= 0 else 0
                    from_left = dp[row_index][column_index - 1] if column_index - 1 >= 0 else 0
                    dp[row_index][column_index] = from_top + from_left

        return dp[m - 1][n - 1]


algos = Solution()
print(algos.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
