class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maximum, second_maximum = 0, 0
        for number in nums:
            second_maximum = maximum if number - 1 >= maximum else max(second_maximum, number - 1)
            maximum = max(maximum, number - 1)

        return maximum * second_maximum
