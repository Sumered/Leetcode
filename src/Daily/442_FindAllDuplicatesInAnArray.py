class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []

        for number in nums:
            index = abs(number) - 1
            if nums[index] < 0:
                duplicates.append(abs(number))
            else:
                nums[index] *= -1

        return duplicates
