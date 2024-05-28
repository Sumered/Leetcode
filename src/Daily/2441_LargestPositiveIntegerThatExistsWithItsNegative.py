class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        numbers: set[int] = set()
        max_number = -1

        for number in nums:
            if -number in numbers:
                max_number = max(max_number, abs(number))
            numbers.add(number)

        return max_number
