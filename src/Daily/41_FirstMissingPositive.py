class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        biggest_num = len(nums)
        nums.append(biggest_num + 1)

        for index in range(biggest_num):
            if nums[index] < 0:
                nums[index] = biggest_num + 1

        for number in nums:
            index = abs(number)
            if index <= biggest_num:
                if nums[index] > 0:
                    nums[index] *= -1

        for index in range(1, len(nums)):
            if nums[index] > 0:
                return index

        return biggest_num + 1
