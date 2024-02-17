from functools import cache


class Solution:
    def __init__(self) -> None:
        self.__directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.__modulo = int(1e9 + 7)

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.kick_ball(startRow, startColumn, m, n, maxMove)

    @cache
    def kick_ball(self, pos_x: int, pos_y: int, m: int, n: int, remaining_moves: int) -> int:
        if pos_x < 0 or pos_x >= m or pos_y < 0 or pos_y >= n:
            return 1
        if remaining_moves == 0:
            return 0
        result = 0
        for direction in self.__directions:
            result += self.kick_ball(pos_x + direction[0], pos_y + direction[1], m, n, remaining_moves - 1) % self.__modulo

        return result % self.__modulo
