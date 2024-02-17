class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if nums == []:
            return [-1, -1]
        left, right = 0, len(nums)

        while left < right:
            medium = (left + right) // 2
            if nums[medium] >= target:
                right = medium
            else:
                left = medium + 1

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        res_left = left
        left, right = 0, len(nums)

        while left < right:
            medium = (left + right) // 2
            if nums[medium] > target:
                right = medium
            else:
                left = medium + 1

        return [res_left, left - 1]


print(Solution().searchRange(nums=[2, 2], target=3))
