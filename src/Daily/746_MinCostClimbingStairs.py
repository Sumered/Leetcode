class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        cost.append(0)
        dp = [int(1e9) for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for stair in range(2, len(cost)):
            dp[stair] = min(dp[stair - 1], dp[stair - 2]) + cost[stair]

        return min(dp[len(cost) - 2], dp[len(cost) - 1])
