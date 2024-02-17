class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            medium = (left + right) // 2
            if nums[medium] < target:
                left = medium + 1
            elif nums[medium] > target:
                right = medium
            else:
                return medium
        return -1
