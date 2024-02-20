class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_sum = sum(nums)
        expected_sum = (len(nums) + 1) * len(nums) / 2
        return int(expected_sum - nums_sum)
