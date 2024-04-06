class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions: list[list[str]] = []

        self.__generate_solutions(n, solutions, [])

        return solutions

    def __generate_solutions(self, n: int, solutions: list[list[str]], current: list[int]) -> None:
        if len(current) == n:
            solution = self.__parse_solution(n, current)
            solutions.append(solution)
            return

        for index in range(n):
            if self.__check(len(current), index, current):
                current.append(index)
                self.__generate_solutions(n, solutions, current)
                current.pop()

    def __parse_solution(self, n: int, current: list[int]) -> list[str]:
        board = []

        for pos in current:
            board.append("." * pos + "Q" + "." * (n - pos - 1))

        return board

    def __check(self, x: int, y: int, current: list[int]) -> bool:
        for index, pos in enumerate(current):
            check_row = pos != y
            check_diag = abs(pos - y) != abs(index - x)
            if not check_row or not check_diag:
                return False

        return True
