class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxes_on_the_right = [int(1e6) for _ in range(len(prices))]
        actual_max = -1

        for index in range(len(prices) - 1, -1, -1):
            maxes_on_the_right[index] = actual_max
            actual_max = max(actual_max, prices[index])

        best_sell = 0

        for index in range(len(prices)):
            best_sell = max(best_sell, maxes_on_the_right[index] - prices[index])

        return best_sell
