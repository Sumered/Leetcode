class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left_index, right_index = 0, len(nums) - 1

        while left_index <= right_index:
            medium = (left_index + right_index) // 2
            if nums[medium] < target:
                left_index = medium + 1
            elif nums[medium] > target:
                right_index = medium - 1
            else:
                return medium

        return left_index
