class Solution:
    def __init__(self) -> None:
        self.__directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        rows, columns = len(land), len(land[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]
        answer = []

        for row in range(rows):
            for column in range(columns):
                if visited[row][column] == False and land[row][column] == 1:
                    output_cords = [307, 307, -1, -1]
                    self.__travel(row, column, land, visited, output_cords)
                    answer.append(output_cords)

        return answer

    def __travel(self, row: int, column: int, land: list[list[int]], visited: list[list[bool]], output_cords: list[int]) -> None:
        visited[row][column] = True
        self.__update_cords(row, column, output_cords)

        for direction in self.__directions:
            new_row, new_column = row + direction[0], column + direction[1]

            if self.__check_travel_requirements(new_row, new_column, land, visited):
                self.__travel(new_row, new_column, land, visited, output_cords)

    def __update_cords(self, row: int, column: int, output_cords: list[int]) -> None:
        output_cords[0] = min(output_cords[0], row)
        output_cords[1] = min(output_cords[1], column)
        output_cords[2] = max(output_cords[2], row)
        output_cords[3] = max(output_cords[3], column)

    def __check_travel_requirements(self, new_row: int, new_column: int, land: list[list[int]], visited: list[list[bool]]) -> bool:
        inside_rows = new_row >= 0 and new_row < len(land)
        inside_columns = new_column >= 0 and new_column < len(land[0])

        if inside_rows and inside_columns:
            is_farm = land[new_row][new_column] == 1
            not_visited = visited[new_row][new_column] == False
            return is_farm and not_visited

        return False
