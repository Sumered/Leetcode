class Solution:
    def __init__(self) -> None:
        self.__directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.__highest_gold = 0

    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        for row in range(rows):
            for column in range(columns):
                if not visited[row][column] and grid[row][column] != 0:
                    self.__travel(row, column, grid, visited, 0)

        return self.__highest_gold

    def __travel(self, row: int, column: int, grid: list[list[int]], visited: list[list[bool]], gain: int) -> None:
        visited[row][column] = True
        gain += grid[row][column]
        self.__highest_gold = max(self.__highest_gold, gain)

        for direction in self.__directions:
            new_row = row + direction[0]
            new_column = column + direction[1]
            if new_row >= 0 and new_row < len(grid) and new_column >= 0 and new_column < len(grid[0]):
                if not visited[new_row][new_column] and grid[new_row][new_column] != 0:
                    self.__travel(new_row, new_column, grid, visited, gain)

        visited[row][column] = False
