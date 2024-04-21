class Solution:
    def __init__(self) -> None:
        self.__directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter, rows, columns = 0, len(grid), len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:
                    continue
                for direction in self.__directions:
                    new_row = row + direction[0]
                    new_column = column + direction[1]

                    if new_row < 0 or new_row >= rows or new_column < 0 or new_column >= columns:
                        perimeter += 1
                        continue

                    perimeter += 1 if grid[new_row][new_column] == 0 else 0

        return perimeter
