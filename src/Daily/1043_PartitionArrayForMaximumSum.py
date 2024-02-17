from functools import cache


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        @cache
        def calculate(index: int) -> int:
            max_sum, current_max = 0, 0
            limit = min(index + k, len(arr))
            for split_point in range(index, limit):
                current_max = max(current_max, arr[split_point])
                my_sum = (split_point - index + 1) * current_max
                other_sum = calculate(split_point + 1)
                max_sum = max(max_sum, my_sum + other_sum)
            return max_sum

        return calculate(0)
