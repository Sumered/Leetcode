class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot_index = self.__find_pivot(nums)

        left_index = self.__bin_search(nums, 0, pivot_index - 1, target)
        right_index = self.__bin_search(nums, pivot_index, len(nums) - 1, target)

        if left_index == -1:
            if right_index == -1:
                return -1
            return right_index
        return left_index

    def __find_pivot(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            medium = (left + right) // 2
            if nums[medium] > nums[right]:
                left = medium + 1
            else:
                right = medium
        return left

    def __bin_search(self, nums: list[int], left: int, right: int, target: int) -> int:
        while left < right:
            medium = (left + right) // 2
            if nums[medium] > target:
                right = medium
            elif nums[medium] < target:
                left = medium + 1
            else:
                return medium
        return -1 if nums[left] != target else left
