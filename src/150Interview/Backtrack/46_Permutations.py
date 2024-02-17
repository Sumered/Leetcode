class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        visited: set[int] = set()

        self.__generate_permutation(nums, [], visited, result, 0)

        return result

    def __generate_permutation(
        self, nums: list[int], current_solution: list[int], visited: set[int], result: list[list[int]], depth: int
    ) -> None:
        if depth == len(nums):
            result.append(current_solution.copy())
            return

        for number in nums:
            if number not in visited:
                visited.add(number)
                current_solution.append(number)
                self.__generate_permutation(nums, current_solution, visited, result, depth + 1)
                visited.remove(number)
                current_solution.pop()

        return
