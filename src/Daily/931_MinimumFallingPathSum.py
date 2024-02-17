class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        dp = [[-100000000 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dp[0] = [matrix[0][i] for i in range(len(matrix[0]))]

        for row in range(1, len(matrix)):
            for column in range(len(matrix)):
                minimal_parent = dp[row - 1][column]
                minimal_parent = min(minimal_parent, dp[row - 1][column + 1]) if column + 1 < len(matrix[0]) else minimal_parent
                minimal_parent = min(minimal_parent, dp[row - 1][column - 1]) if column - 1 >= 0 else minimal_parent
                dp[row][column] = minimal_parent + matrix[row][column]

        return min(dp[len(matrix) - 1])


Solution().minFallingPathSum([[17, 82], [1, -44]])
