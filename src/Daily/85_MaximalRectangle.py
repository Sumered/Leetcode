from collections import deque

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        result = 0

        rows, columns = len(matrix), len(matrix[0])
        histogram = [0 for _ in range(columns)]

        for row in range(rows):
            for column in range(columns):
                histogram[column] = (histogram[column] + 1) if matrix[row][column] == '1' else 0
            
            result = max(result, self.__calculate_area(histogram))
        
        return result

    def __calculate_area(self, histogram: list[int]) -> int:
        stack = deque()
        biggest_area = 0

        for index in range(len(histogram) + 1):
            while stack and (index == len(histogram) or histogram[stack[-1]] > histogram[index]):
                height = histogram[stack.pop()]
                width = index if not stack else index - stack[-1] - 1
                biggest_area = max(biggest_area, height * width)
            stack.append(index)
        
        return biggest_area