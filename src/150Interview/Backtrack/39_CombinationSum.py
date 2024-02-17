class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result: list[list[int]] = []
        visited: set[int] = set()

        self.__generate_permutation(candidates, [], 0, target, result, 0)

        return result

    def __generate_permutation(
        self, nums: list[int], current_solution: list[int], candidates_sum: int, target: int, result: list[list[int]], min_index: int
    ) -> None:
        if candidates_sum > target:
            return
        if candidates_sum == target:
            result.append(current_solution.copy())
            return

        for index, number in enumerate(nums[min_index:]):
            current_solution.append(number)
            self.__generate_permutation(nums, current_solution, candidates_sum + number, target, result, index + min_index)
            current_solution.pop()

        return
