class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zeroed = [False for _ in range(len(matrix))]
        column_zeroed = [False for _ in range(len(matrix[0]))]

        self.__check_zeroing(matrix, row_zeroed, column_zeroed)
        self.__zero_matrix(matrix, row_zeroed, column_zeroed)

    def __check_zeroing(self, matrix: list[list[int]], row_zeroed: list[bool], column_zeroed: list[bool]) -> None:
        for row_index in range(len(matrix)):
            for column_index in range(len(matrix[0])):
                if matrix[row_index][column_index] == 0:
                    row_zeroed[row_index] = True
                    column_zeroed[column_index] = True

    def __zero_matrix(self, matrix: list[list[int]], row_zeroed: list[bool], column_zeroed: list[bool]) -> None:
        for row_index in range(len(matrix)):
            for column_index in range(len(matrix[0])):
                if row_zeroed[row_index] or column_zeroed[column_index]:
                    matrix[row_index][column_index] = 0
