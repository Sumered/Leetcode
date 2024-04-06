class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)
        output_array = [1 for _ in range(len(nums))]
        current = 1

        for index in range(len(nums) - 1, -1, -1):
            output_array[index] *= current
            current *= nums[index]

        current = 1
        for index in range(len(nums)):
            output_array[index] *= current
            current *= nums[index]

        return output_array
