class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions_count = self.__generate_solutions(n, [])

        return solutions_count

    def __generate_solutions(self, n: int, current: list[int]) -> int:
        if len(current) == n:
            return 1

        result = 0

        for index in range(n):
            if self.__check(len(current), index, current):
                current.append(index)
                result += self.__generate_solutions(n, current)
                current.pop()

        return result

    def __check(self, x: int, y: int, current: list[int]) -> bool:
        for index, pos in enumerate(current):
            check_row = pos != y
            check_diag = abs(pos - y) != abs(index - x)
            if not check_row or not check_diag:
                return False

        return True
