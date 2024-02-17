class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        rows, columns = len(matrix), len(matrix[0])
        sums = [[0 for _ in range(columns)] for _ in range(rows)]
        self.__fill_sums_matrix(matrix, sums)

        count_target = 0
        for row_index in range(rows):
            for column_index in range(columns):
                full_sum = sums[row_index][column_index]
                if full_sum == target:
                    count_target += 1
                for sub_row_index in range(row_index + 1):
                    for sub_column_index in range(column_index + 1):
                        if row_index == sub_row_index and column_index == sub_column_index:
                            break
                        if self.__calc_difference(sums, row_index, column_index, sub_row_index, sub_column_index) == target:
                            count_target += 1
        return count_target

    def __fill_sums_matrix(self, matrix: list[list[int]], sums: list[list[int]]) -> None:
        rows, columns = len(matrix), len(matrix[0])
        for column_index in range(columns):
            sums[0][column_index] = sums[0][column_index - 1] + matrix[0][column_index]

        for row_index in range(rows):
            sums[row_index][0] = sums[row_index - 1][0] + matrix[row_index][0]

        for row_index in range(1, rows):
            for column_index in range(1, columns):
                sums[row_index][column_index] = (
                    sums[row_index - 1][column_index] + sums[row_index][column_index - 1] - sums[row_index - 1][column_index - 1]
                ) + matrix[row_index][column_index]
        return

    def __calc_difference(self, sums: list[list[int]], row: int, column: int, sub_row: int, sub_column: int) -> int:
        full_sum = sums[row][column]
        difference = sums[row][sub_column] + sums[sub_row][column] - sums[sub_row][sub_column]
        return full_sum - difference


print(Solution().numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
