class Solution:
    def __init__(self) -> None:
        self.__directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def solve(self, grid: list[list[str]]) -> None:
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        self.__handle_horizontal_border(rows, columns, visited, grid)
        self.__handle_vertical_border(rows, columns, visited, grid)

        self.__fill_not_visited(rows, columns, visited, grid)

    def __fill_not_visited(self, rows: int, columns: int, visited: list[list[bool]], grid: list[list[str]]) -> None:
        for row_index in range(rows):
            for column_index in range(columns):
                if visited[row_index][column_index] != True:
                    grid[row_index][column_index] = "X"

    def __handle_horizontal_border(self, rows: int, columns: int, visited: list[list[bool]], grid: list[list[str]]) -> None:
        for row_index in range(rows):
            if visited[row_index][0] != True and grid[row_index][0] == "O":
                self.__visit_island(row_index, 0, visited, grid)
            if visited[row_index][columns - 1] != True and grid[row_index][columns - 1] == "O":
                self.__visit_island(row_index, columns - 1, visited, grid)

    def __handle_vertical_border(self, rows: int, columns: int, visited: list[list[bool]], grid: list[list[str]]) -> None:
        for column_index in range(columns):
            if visited[0][column_index] != True and grid[0][column_index] == "O":
                self.__visit_island(0, column_index, visited, grid)
            if visited[rows - 1][column_index] != True and grid[rows - 1][column_index] == "O":
                self.__visit_island(rows - 1, column_index, visited, grid)

    def __visit_island(self, row_index: int, column_index: int, visited: list[list[bool]], grid: list[list[str]]) -> None:
        visited[row_index][column_index] = True
        rows, columns = len(grid), len(grid[0])

        for direction_row, direction_column in self.__directions:
            new_row_index = self.__cap_cords(row_index + direction_row, rows)
            new_column_index = self.__cap_cords(column_index + direction_column, columns)
            if visited[new_row_index][new_column_index] == False and grid[new_row_index][new_column_index] == "O":
                self.__visit_island(new_row_index, new_column_index, visited, grid)

    def __cap_cords(self, cord: int, limit: int) -> int:
        return min(limit - 1, max(0, cord))
