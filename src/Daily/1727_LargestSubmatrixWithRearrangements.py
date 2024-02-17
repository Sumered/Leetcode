class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        rows_count, columns_count = len(matrix), len(matrix[0])
        maximal_count_down = [[-1 for _ in range(columns_count)] for _ in range(rows_count)]
        self.__fill_maximal_count_down(maximal_count_down, matrix, rows_count, columns_count)
        self.__prepare_countdown_matrix(maximal_count_down, rows_count)

        result = 0
        for row_index in range(rows_count):
            result = max(result, self.__check_row(maximal_count_down[row_index], columns_count))
        return result

    def __prepare_countdown_matrix(self, maximal_count_down: list[list[int]], rows_count: int) -> None:
        for row_index in range(rows_count):
            maximal_count_down[row_index].sort(reverse=True)

    def __check_row(self, maximal_count_down: list[int], columns_count: int) -> int:
        result = 0
        for index in range(columns_count):
            result = max(result, maximal_count_down[index] * (index + 1))
        return result

    def __fill_maximal_count_down(
        self, maximal_count_down: list[list[int]], matrix: list[list[int]], rows_count: int, columns_count: int
    ) -> None:
        for row_index in range(rows_count):
            for column_index in range(columns_count):
                if maximal_count_down[row_index][column_index] != -1:
                    continue
                offset = 0
                while row_index + offset < rows_count:
                    if matrix[row_index + offset][column_index] == 0:
                        break
                    else:
                        offset += 1

                for row_index_offseted in range(row_index, row_index + offset):
                    maximal_count_down[row_index_offseted][column_index] = (row_index + offset) - row_index_offseted


algos = Solution()
print(algos.largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(algos.largestSubmatrix([[1, 0, 1, 0, 1]]))
print(algos.largestSubmatrix([[1, 1, 0], [1, 0, 1]]))
print(algos.largestSubmatrix([[1, 0, 0], [1, 1, 1], [0, 1, 1]]))
