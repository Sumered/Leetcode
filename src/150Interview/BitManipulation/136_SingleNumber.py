from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

    def sumVersion_singleNumber(self, nums: list[int]) -> int:
        numbers_sum = 0
        numbers_occurred = set()

        for number in nums:
            if number in numbers_occurred:
                numbers_sum -= number
            else:
                numbers_sum += number
                numbers_occurred.add(number)

        return numbers_sum
