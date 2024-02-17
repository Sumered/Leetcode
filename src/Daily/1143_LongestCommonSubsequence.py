from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.findLCS(text1, text2, 0, 0)

    @cache
    def findLCS(self, text1: str, text2: str, index_first: int, index_second: int) -> int:
        if index_first == len(text1) or index_second == len(text2):
            return 0
        if text1[index_first] == text2[index_second]:
            return 1 + self.findLCS(text1, text2, index_first + 1, index_second + 1)
        else:
            first_score = self.findLCS(text1, text2, index_first + 1, index_second)
            second_score = self.findLCS(text1, text2, index_first, index_second + 1)
            return max(first_score, second_score)
