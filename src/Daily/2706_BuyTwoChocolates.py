class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        min_first, min_second = 107, 107
        for price in prices:
            min_second = min_first if price <= min_first else min(min_second, price)
            min_first = min(price, min_first)

        change = money - (min_first + min_second)
        return change if change >= 0 else money
