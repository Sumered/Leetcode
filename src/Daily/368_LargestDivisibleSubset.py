class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        result = [[number] for number in nums]

        for index in range(1, len(nums)):
            for index_second in range(index):
                if nums[index] % nums[index_second] == 0 and len(result[index]) < len(result[index_second]) + 1:
                    result[index] = result[index_second] + [nums[index]]

        best = max(result, key=len)
        return best
