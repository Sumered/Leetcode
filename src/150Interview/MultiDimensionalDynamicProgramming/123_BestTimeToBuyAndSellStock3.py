from enum import IntEnum


class Index(IntEnum):
    BOUGHT_ONE = 0
    SOLD_ONE = 1
    BOUGHT_TWO = 2
    SOLD_TWO = 3


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit_table = [int(1e6), 0, int(-1e6), 0]

        for price in prices:
            profit_table[Index.SOLD_ONE] = max(price - profit_table[Index.BOUGHT_ONE], profit_table[Index.SOLD_ONE])
            profit_table[Index.SOLD_TWO] = max(profit_table[Index.BOUGHT_TWO] + price, profit_table[Index.SOLD_TWO])
            profit_table[Index.BOUGHT_ONE] = min(profit_table[Index.BOUGHT_ONE], price)
            profit_table[Index.BOUGHT_TWO] = max(profit_table[Index.SOLD_ONE] - price, profit_table[Index.BOUGHT_TWO])

        return profit_table[Index.SOLD_TWO]
