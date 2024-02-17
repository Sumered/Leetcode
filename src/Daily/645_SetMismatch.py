class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        expected_sum = (len(nums) ** 2 + len(nums)) // 2
        missing_number = expected_sum - sum(set(nums))
        duplicate_number = sum(nums) - (expected_sum - missing_number)
        return [duplicate_number, missing_number]
