class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        result = 0

        left_index, right_index = 0, len(piles) - 1
        while left_index < right_index:
            result += piles[right_index - 1]
            left_index += 1
            right_index -= 2

        return result
