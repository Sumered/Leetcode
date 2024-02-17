class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows_sum = []
        columns_sum = []
        for row in mat:
            rows_sum.append(sum(row))

        for column_index in range(len(mat[0])):
            column_sum = 0
            for row_index in range(len(mat)):
                column_sum += mat[row_index][column_index]
            columns_sum.append(column_sum)

        count = 0
        for row_index in range(len(rows_sum)):
            for column_index in range(len(columns_sum)):
                if rows_sum[row_index] == 1 and columns_sum[column_index] == 1 and mat[row_index][column_index] == 1:
                    count += 1
        return count
