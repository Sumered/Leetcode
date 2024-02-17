class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        costs = [[0 for _ in range(len(word2))] for _ in range(len(word1))]

        for index_first, letter_first in enumerate(word1):
            for index_second, letter_second in enumerate(word2):
                possible_cost = 0 if letter_first == letter_second else 1
                costs[index_first][index_second] = possible_cost + abs(index_second - index_first)

        dp = [[0 for _ in range(len(word2))] for _ in range(len(word1))]

        for index_first, letter_first in enumerate(word1):
            for index_second, letter_last in enumerate(word2):
                dp[index_first][index_second] = (
                    min(dp[index_first - 1][index_second - 1], dp[index_first][index_second - 1]) + costs[index_first][index_second]
                )

        return min(dp[len(word1) - 1])


print(Solution().minDistance("horse", "ros"))
