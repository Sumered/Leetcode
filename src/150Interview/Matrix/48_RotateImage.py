class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n, loops_left, offset = len(matrix) - 1, len(matrix) - 1, 0

        while loops_left > 0:
            for i in range(loops_left):
                (
                    matrix[offset][i + offset],
                    matrix[offset + i][n - offset],
                    matrix[n - offset][n - i - offset],
                    matrix[n - i - offset][offset],
                ) = (
                    matrix[n - i - offset][offset],
                    matrix[offset][i + offset],
                    matrix[offset + i][n - offset],
                    matrix[n - offset][n - i - offset],
                )

            offset += 1
            loops_left -= 2
