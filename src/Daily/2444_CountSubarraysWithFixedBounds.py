class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        start_index, index, min_index, max_index = 0, 0, -1, -1
        result = 0

        while index < len(nums):
            number = nums[index]

            if number > maxK or number < minK:
                start_index = index + 1
                min_index = -1
                max_index = -1

            if number == maxK:
                max_index = index
            if number == minK:
                min_index = index

            result += max(0, min(max_index, min_index) - start_index + 1)
            index += 1

        return result
