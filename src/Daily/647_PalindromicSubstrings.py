from functools import cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        count, n = 0, len(s)

        for index in range(n):
            even = self.__count_palindrome(s, index, index + 1)
            odd = self.__count_palindrome(s, index, index)
            count += even + odd

        return count

    def __count_palindrome(self, s: str, left: int, right: int) -> int:
        count = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

        return count

    def brute_countSubstrings(self, s: str) -> int:
        count = 0

        for start in range(len(s)):
            for end in range(start, len(s)):
                if self.__palindromic(s, start, end):
                    count += 1
        return count

    @cache
    def __palindromic(self, s: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        if s[start] != s[end]:
            return False

        return True and self.__palindromic(s, start + 1, end - 1)
