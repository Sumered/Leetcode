class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(list(set(nums)))