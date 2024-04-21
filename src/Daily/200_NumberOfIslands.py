class Solution:
    def __init__(self) -> None:
        self.__directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def numIslands(self, grid: list[list[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        islands_count = 0
        for row_index in range(rows):
            for column_index in range(columns):
                if visited[row_index][column_index] != True and grid[row_index][column_index] == "1":
                    self.__visit_island(row_index, column_index, visited, grid)
                    islands_count += 1

        return islands_count

    def __visit_island(self, row_index: int, column_index: int, visited: list[list[bool]], grid: list[list[str]]) -> None:
        visited[row_index][column_index] = True
        rows, columns = len(grid), len(grid[0])

        for direction_row, direction_column in self.__directions:
            new_row_index = self.__cap_cords(row_index + direction_row, rows)
            new_column_index = self.__cap_cords(column_index + direction_column, columns)
            if visited[new_row_index][new_column_index] == False and grid[new_row_index][new_column_index] == "1":
                self.__visit_island(new_row_index, new_column_index, visited, grid)

    def __cap_cords(self, cord: int, limit: int) -> int:
        return min(limit - 1, max(0, cord))
