class Solution:
    def __init__(self) -> None:
        self.__directions = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)],
        }

    def hasValidPath(self, grid: list[list[int]]) -> bool:
        visited: list[list[bool]] = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        return self.__dfs(0, 0, grid, visited)

    def __dfs(self, row: int, column: int, grid: list[list[int]], visited: list[list[bool]]) -> bool:
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return True

        direction = grid[row][column]

        for row_direction, column_direction in self.__directions[direction]:
            new_row, new_column = row + row_direction, column + column_direction

            if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]):
                opposite_direction = (row_direction * -1, column_direction * -1)
                matches = opposite_direction in self.__directions[grid[new_row][new_column]]

                if matches and not visited[new_row][new_column]:
                    visited[new_row][new_column] = True
                    if self.__dfs(new_row, new_column, grid, visited):
                        return True

        return False
