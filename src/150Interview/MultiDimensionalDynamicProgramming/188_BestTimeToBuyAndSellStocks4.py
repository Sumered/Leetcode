from enum import IntEnum


class Options(IntEnum):
    NOTHING = 0
    BUY = 1
    SELL = 2


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        days = len(prices)
        result = 0
        dp = [[[-100001, -100001, -100001] for _ in range(k + 1)] for _ in range(days)]
        dp[0][0][Options.NOTHING] = 0
        dp[0][1][Options.BUY] = -prices[0]

        for day in range(1, days):
            for operation_number in range(k, -1, -1):
                dp[day][operation_number][Options.NOTHING] = self.__calculate_nothing_value(prices, dp, day, operation_number)
                dp[day][operation_number][Options.BUY] = self.__calculate_buy_value(prices, dp, day, operation_number)
                dp[day][operation_number][Options.SELL] = self.__calculate_sell_value(prices, dp, day, operation_number)
                result = max(result, max(dp[day][operation_number]))
        return result

    def __calculate_nothing_value(self, prices: list[int], dp: list[list[list[int]]], day: int, operation: int) -> int:
        previous_day_nothing = dp[day - 1][operation][Options.NOTHING]
        previous_day_buy = dp[day - 1][operation][Options.BUY]
        previous_day_sell = dp[day - 1][operation][Options.SELL]
        return max(previous_day_nothing, previous_day_buy, previous_day_sell)

    def __calculate_buy_value(self, prices: list[int], dp: list[list[list[int]]], day: int, operation: int) -> int:
        previous_day_nothing = dp[day - 1][operation - 1][Options.NOTHING] if operation >= 1 else -100001
        previous_day_buy = dp[day - 1][operation][Options.BUY]
        previous_day_sell = dp[day - 1][operation - 1][Options.SELL] if operation >= 1 else -100001

        return max(previous_day_nothing - prices[day], previous_day_buy, previous_day_sell - prices[day])

    def __calculate_sell_value(self, prices: list[int], dp: list[list[list[int]]], day: int, operation: int) -> int:
        previous_day_buy = dp[day - 1][operation][Options.BUY]

        return previous_day_buy + prices[day]
