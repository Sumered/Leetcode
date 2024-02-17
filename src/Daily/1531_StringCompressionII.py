from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        result = self.__solve(s, 0, k, "", 0)
        return result

    @cache
    def __solve(self, s: str, index: int, k: int, last_char: str, count: int) -> int:
        if k < 0:
            return 107

        if index == len(s):
            return self.__cost(count)

        remove_result = self.__solve(s, index + 1, k - 1, last_char, count)

        if last_char == s[index]:
            no_remove_result = self.__solve(s, index + 1, k, last_char, count + 1)
        else:
            no_remove_result = self.__solve(s, index + 1, k, s[index], 1) + self.__cost(count)

        return min(remove_result, no_remove_result)

    def __cost(self, count: int) -> int:
        if count > 1:
            return len(str(count)) + 1
        return count
