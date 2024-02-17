class Solution:
    def __init__(self) -> None:
        self.__directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: list[int] = []
        self.__rows_count, self.__columns_count = len(matrix), len(matrix[0])
        current_row, current_column, current_direction = 0, 0, 0
        fields_traveled = [0, 0, 0, 0]
        field_to_travel = self.__calculate_offset(current_direction, 0, current_row, current_column)

        self.__fill_solution(matrix, result, current_row, current_column, current_direction, field_to_travel, fields_traveled)

        return result

    def __fill_solution(
        self,
        matrix: list[list[int]],
        result: list[int],
        current_row: int,
        current_column: int,
        current_direction: int,
        fields_remaining: int,
        fields_traveled: list[int],
    ) -> None:
        result.append(matrix[current_row][current_column])

        if fields_remaining == 0:
            fields_traveled[(current_direction - 1) % 4] += 1
            current_direction = (current_direction + 1) % 4
            fields_remaining = self.__calculate_offset(current_direction, fields_traveled[current_direction], current_row, current_column)
            if fields_remaining == 0:
                return

        new_row = current_row + self.__directions[current_direction][0]
        new_column = current_column + self.__directions[current_direction][1]
        self.__fill_solution(matrix, result, new_row, new_column, current_direction, fields_remaining - 1, fields_traveled)

    def __calculate_offset(self, current_direction: int, fields_traveled: int, current_row: int, current_column: int) -> int:
        match current_direction:
            case 0:
                return self.__columns_count - current_column - fields_traveled - 1
            case 1:
                return self.__rows_count - current_row - fields_traveled - 1
            case 2:
                return current_column - fields_traveled
            case 3:
                return current_row - fields_traveled
            case _:
                return 0


algos = Solution()
print(algos.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
