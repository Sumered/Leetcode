class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        all_subs = self.__count(nums, goal)
        small_subs = self.__count(nums, goal - 1)
        return all_subs - small_subs

    def __count(self, nums: list[int], goal: int) -> int:
        left, right = 0, 0
        current_sum, result = 0, 0

        while right < len(nums):
            current_sum += nums[right]
            while left <= right and current_sum > goal:
                current_sum -= nums[left]
                left += 1
            result += right - left + 1
            right += 1
        return result
