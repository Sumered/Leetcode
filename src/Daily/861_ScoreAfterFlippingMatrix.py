class Solution:
    def __init__(self) -> None:
        self.__best_score = 0

    def matrixScore(self, grid: list[list[int]]) -> int:
        self.__flip_or_not_to_flip(grid, 0)
        return self.__best_score

    def __flip_or_not_to_flip(self, grid: list[list[int]], row: int) -> None:
        if row == len(grid):
            self.__best_score = max(self.__best_score, self.__calculate_results(grid))
            return

        if grid[row][0] == 0:
            self.__flip_row(grid, row)

        self.__flip_or_not_to_flip(grid, row + 1)

    def __flip_row(self, grid: list[list[int]], row: int) -> None:
        for index in range(len(grid[row])):
            grid[row][index] = 0 if grid[row][index] == 1 else 1

    def __calculate_results(self, grid: list[list[int]]) -> int:
        result, power = 0, 1

        for column in range(len(grid[0]) - 1, -1, -1):
            count = 0

            for row in range(len(grid)):
                count += grid[row][column]

            result += power * max(count, len(grid) - count)
            power *= 2

        return result
