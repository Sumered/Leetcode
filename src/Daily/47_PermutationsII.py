class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        used_prefixes: set[tuple] = set()
        result: list[list[int]] = []

        max_counts: dict[int, int] = {}
        for number in nums:
            max_counts[number] = max_counts.get(number, 0) + 1

        self.__generate(nums, [], used_prefixes, result, {}, max_counts)

        return result

    def __generate(
        self,
        nums: list[int],
        current_solution: list[int],
        used_prefixes: set[tuple],
        result: list[list[int]],
        counts: dict[int, int],
        max_counts: dict[int, int],
    ) -> None:
        if len(current_solution) == len(nums):
            result.append(current_solution.copy())
            return

        for number in nums:
            current_solution.append(number)
            counts[number] = counts.get(number, 0) + 1
            if counts[number] <= max_counts[number] and tuple(current_solution) not in used_prefixes:
                used_prefixes.add(tuple(current_solution))
                self.__generate(nums, current_solution, used_prefixes, result, counts, max_counts)

            current_solution.pop()
            counts[number] -= 1
