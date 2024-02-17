class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows_count, columns_count = len(matrix), len(matrix[0])
        new_matrix = [[0 for _ in range(rows_count)] for _ in range(columns_count)]

        for row in range(rows_count):
            for column in range(columns_count):
                new_matrix[column][row] = matrix[row][column]

        return new_matrix
