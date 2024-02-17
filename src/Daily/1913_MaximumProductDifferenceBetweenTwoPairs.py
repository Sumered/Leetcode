class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        first_max, second_max, first_min, second_min = 0, 0, 10001, 10001

        for number in nums:
            second_max = first_max if number >= first_max else max(second_max, number)
            first_max = max(first_max, number)

            second_min = first_min if number <= first_min else min(second_min, number)
            first_min = min(first_min, number)

        return (first_max * second_max) - (first_min * second_min)
