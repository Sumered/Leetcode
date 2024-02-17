from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_dict: dict[int, int] = defaultdict(lambda: -1)

        for number in nums:
            nums_dict[number] = 0

        longest_sequence = 0
        for number in nums:
            result = self.__check(number, nums_dict, 0)
            longest_sequence = max(longest_sequence, result)

        return longest_sequence

    def __check(self, number: int, nums_dict: dict[int, int], actual_count: int) -> int:
        if nums_dict[number] == -1:
            return actual_count
        elif nums_dict[number] == 0:
            nums_dict[number] = self.__check(number + 1, nums_dict, actual_count + 1)
            return nums_dict[number]
        else:
            return actual_count + nums_dict[number]


algos = Solution()
print(algos.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
