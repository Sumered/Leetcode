from functools import cache


class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        @cache
        def max_range(left: int, right: int) -> int:
            return max(jobDifficulty[left : right + 1])

        if len(jobDifficulty) < d:
            return -1

        dp = [[10007 for _ in range(d + 1)] for _ in range(len(jobDifficulty))]
        for i in range(len(jobDifficulty)):
            dp[i][1] = max_range(0, i)

        for index in range(len(jobDifficulty)):
            for previous_job in range(index):
                for day in range(1, d):
                    result = dp[previous_job][day] + max_range(previous_job + 1, index)
                    dp[index][day + 1] = min(dp[index][day + 1], result)

        return dp[len(jobDifficulty) - 1][d]
