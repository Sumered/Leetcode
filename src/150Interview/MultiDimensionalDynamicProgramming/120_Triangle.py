class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        results: list[list[int]] = [[int(1e6) for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        results[0][0] = triangle[0][0]

        for row in range(1, len(triangle)):
            for position in range(len(triangle[row])):
                left_position = position - 1 if position >= 1 else 0
                right_position = position if position <= row - 1 else position - 1
                best_previous_row = min(results[row - 1][left_position], results[row - 1][right_position])
                results[row][position] = best_previous_row + triangle[row][position]

        best_result = int(1e6)
        last_row_index = len(triangle)
        for i in range(len(triangle[last_row_index])):
            best_result = min(best_result, results[last_row_index][i])

        return best_result
