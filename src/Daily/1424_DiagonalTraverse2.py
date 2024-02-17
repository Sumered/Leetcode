class Solution:
    def findDiagonalOrder(self, numbers: list[list[int]]) -> list[int]:
        diagonals: list[list[int]] = [[] for _ in range(self.__get_max_length(numbers) * 2 + 1)]

        for row_index, numbers_row in enumerate(numbers):
            for number_index, number in enumerate(numbers_row):
                diagonals[row_index + number_index].append(number)

        result: list[int] = []
        for diagonal in diagonals:
            result += reversed(diagonal)
        return result

    def __get_max_length(self, numbers: list[list[int]]) -> int:
        maximal_length = len(numbers)
        for sub_numbers in numbers:
            maximal_length = max(maximal_length, len(sub_numbers))
        return maximal_length


algos = Solution()
print(algos.findDiagonalOrder([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]))
# [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
# print(algos.findDiagonalOrder([[1, 2, 3, 4, 5, 6]]))
# [1, 2, 3, 4, 5, 6]
