class Solution:
    def totalMoney(self, n: int) -> int:
        weeks_passed = n // 7
        bonus = 7 * weeks_passed * (weeks_passed - 1) / 2
        rest_of_days = (((weeks_passed + 1) * 2 + (n % 7) - 1) * (n % 7)) / 2
        return int(weeks_passed * 28 + bonus + rest_of_days)

    def iterative_totalMoney(self, n: int) -> int:
        result = 0
        actual_n = 1

        while n >= 7:
            result += int((actual_n * 2 + 6) * 3.5)
            actual_n += 1
            n -= 7
        result += int((actual_n * 2 + (n % 7) - 1) * (n % 7) / 2)
        return int(result)


print(Solution().totalMoney(20))
print(Solution().iterative_totalMoney(20))
