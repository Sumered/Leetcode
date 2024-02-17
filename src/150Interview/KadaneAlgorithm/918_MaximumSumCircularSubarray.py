class Solution:
    def maxSubarraySumCircular(self, numbers: list[int]) -> int:
        max_sum, current_max_sum, min_sum, current_min_sum = -10001, -10001, 10001, 10001

        for number in numbers:
            current_max_sum = max(current_max_sum + number, number)
            current_min_sum = min(current_min_sum + number, number)
            max_sum = max(max_sum, current_max_sum)
            min_sum = min(min_sum, current_min_sum)

        if all(number < 0 for number in numbers):
            return max(numbers)
        return max(max_sum, sum(numbers) - min_sum)
