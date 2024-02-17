class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        numbers_dict = self.__fill_dict(nums)

        for first_index in range(len(nums)):
            if first_index - 1 >= 0 and nums[first_index] == nums[first_index - 1]:
                continue
            for second_index in range(first_index + 1, len(nums)):
                if second_index - 1 != first_index and nums[second_index] == nums[second_index - 1]:
                    continue
                matching_number = -1 * (nums[first_index] + nums[second_index])
                if matching_number in numbers_dict and numbers_dict[matching_number] > second_index:
                    result.append([nums[first_index], nums[second_index], matching_number])

        return result

    def __fill_dict(self, nums: list[int]) -> dict[int, int]:
        numbers_dict: dict[int, int] = {}
        for index, number in enumerate(nums):
            numbers_dict[number] = max(numbers_dict.get(number, 0), index)
        return numbers_dict
