class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort()
        max_happiness = 0

        for index in range(k):
            max_happiness += max(0, happiness[-(index + 1)] - index)

        return max_happiness
