class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        lengths = sorted(nums)
        all_lengths = sum(lengths)
        for index in range(len(lengths) - 1, 1, -1):
            if all_lengths - lengths[index] > lengths[index]:
                return all_lengths
            else:
                all_lengths -= lengths[index]

        return -1
