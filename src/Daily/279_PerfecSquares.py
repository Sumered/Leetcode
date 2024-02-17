from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        unvisited = 100007
        dp = [unvisited for _ in range(n + 1)]
        powers = [i * i for i in range(1, int(sqrt(n) + 1))]

        dp[0] = 0

        for power in powers:
            for number in range(n + 1):
                if number + power > n:
                    break
                if dp[number] != unvisited:
                    dp[number + power] = min(dp[number] + 1, dp[number + power])
        return dp[n]
