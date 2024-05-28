class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        minimal_value, second_minimal_value = (0, -1), (0, -1)

        for row in range(rows):
            new_minimal_value, new_second_minimal_value = (int(1e9), -1), (int(1e9), -1)
            for column in range(columns):
                value = grid[row][column]
                if minimal_value[1] != column:
                    new_minimal_value, new_second_minimal_value = self.__update_minimal_values(
                        value, column, minimal_value, new_minimal_value, new_second_minimal_value
                    )
                else:
                    new_minimal_value, new_second_minimal_value = self.__update_minimal_values(
                        value, column, second_minimal_value, new_minimal_value, new_second_minimal_value
                    )
            minimal_value, second_minimal_value = new_minimal_value, new_second_minimal_value

        return minimal_value[0]

    def __update_minimal_values(
        self,
        value: int,
        index: int,
        previous_minimal_value: tuple[int, int],
        minimal_value: tuple[int, int],
        second_minimal_value: tuple[int, int],
    ) -> tuple[tuple[int, int], tuple[int, int]]:
        if previous_minimal_value[0] + value < minimal_value[0]:
            second_minimal_value = minimal_value
            minimal_value = (previous_minimal_value[0] + value, index)
        elif previous_minimal_value[0] + value < second_minimal_value[0]:
            second_minimal_value = (previous_minimal_value[0] + value, index)

        return minimal_value, second_minimal_value
