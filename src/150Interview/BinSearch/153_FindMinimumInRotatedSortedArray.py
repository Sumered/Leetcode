class Solution:
    def findMin(self, nums: list[int]) -> int:
        pivot_index = self.__find_pivot(nums)

        return nums[pivot_index]

    def __find_pivot(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            medium = (left + right) // 2
            if nums[medium] > nums[right]:
                left = medium + 1
            else:
                right = medium
        return left
