class Solution:
    def __init__(self) -> None:
        self.__directions: list[list[int]] = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def exist(self, board: list[list[str]], word: str) -> bool:
        visited: set[tuple[int, int]] = set()

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    visited.add((row, column))
                    if self.__check(row, column, board, visited, word, ""):
                        return True
                    visited.remove((row, column))
        return False

    def __check(self, row: int, column: int, board: list[list[str]], visited: set[tuple[int, int]], word: str, current_word: str) -> bool:
        current_word += board[row][column]

        if current_word == word:
            return True

        for direction in self.__directions:
            new_row = row + direction[0]
            new_column = column + direction[1]
            if self.__is_inside(new_row, new_column, board):
                if board[new_row][new_column] == word[len(current_word)] and (new_row, new_column) not in visited:
                    visited.add((new_row, new_column))
                    if self.__check(new_row, new_column, board, visited, word, current_word):
                        return True
                    visited.remove((new_row, new_column))

        current_word = current_word[:-1]

        return False

    def __is_inside(self, x: int, y: int, board: list[list[str]]) -> bool:
        return x < len(board) and y < len(board[0]) and x >= 0 and y >= 0
