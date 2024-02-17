class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()

        return self.__find_max_sum(nums)

    def __find_max_sum(self, nums: list[int]) -> int:
        left_index, right_index = 0, len(nums) - 1
        maximal_pair_sum = 0

        while left_index < right_index:
            maximal_pair_sum = max(maximal_pair_sum, nums[left_index] + nums[right_index])
            left_index += 1
            right_index -= 1

        return maximal_pair_sum
