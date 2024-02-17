class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [1000007 for _ in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for change in range(amount + 1):
                if dp[change] == 1000007 or change + coin > amount:
                    continue
                dp[change + coin] = min(dp[change] + 1, dp[change + coin])

        return dp[amount] if dp[amount] != 1000007 else -1


algos = Solution()
print(algos.coinChange([1, 2, 5], 11))
