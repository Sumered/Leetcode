class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = [[]]
        self.__backtrack(nums, 0, result, [])
        return result

    def __backtrack(self, nums: list[int], index: int, result: list[list[int]], current: list[int]) -> None:
        for iterator in range(index, len(nums)):
            current.append(nums[iterator])
            result.append(current.copy())
            self.__backtrack(nums, iterator + 1, result, current)
            current.pop()
