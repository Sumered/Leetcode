from functools import cache


class Solution:
    def __init__(self) -> None:
        self.__modulo = 10**9 + 7

    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n == 0:
            return self.__sanity_check(n, target)

        result = 0
        for roll_result in range(1, k + 1):
            result += self.numRollsToTarget(n - 1, k, target - roll_result)
            result = result % self.__modulo
        return result

    def __sanity_check(self, n: int, target: int) -> int:
        if target == 0:
            return 1
        else:
            return 0
