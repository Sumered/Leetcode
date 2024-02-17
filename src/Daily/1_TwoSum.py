class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_indices = sorted(range(len(nums)), key=lambda k: nums[k])
        left_index, right_index = 0, len(nums) - 1
        while left_index < right_index:
            actual_sum = nums[sorted_indices[left_index]] + nums[sorted_indices[right_index]]
            if actual_sum > target:
                right_index -= 1
            elif actual_sum < target:
                left_index += 1
            else:
                return [sorted_indices[left_index], sorted_indices[right_index]]
        return []

    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        differences = set()
        indexes: dict[int, int] = {}
        for index, number in enumerate(nums):
            if number in differences:
                return [indexes[number], index]
            differences.add(target - number)
            indexes[target - number] = index
        return []
