class Solution:
    SUDOKU_SIZE = 9
    SQUARE_SIZE = 3

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.__check_rows(board) and self.__check_columns(board) and self.__check_squares(board)

    def __check_rows(self, board: list[list[str]]) -> bool:
        for row_index in range(self.SUDOKU_SIZE):
            unique_numbers: set[str] = set()

            for column_index in range(self.SUDOKU_SIZE):
                number = board[row_index][column_index]
                if number == ".":
                    continue
                if number in unique_numbers:
                    return False
                unique_numbers.update(number)

        return True

    def __check_columns(self, board: list[list[str]]) -> bool:
        for column_index in range(self.SUDOKU_SIZE):
            unique_numbers: set[str] = set()

            for row_index in range(self.SUDOKU_SIZE):
                number = board[row_index][column_index]
                if number == ".":
                    continue
                if number in unique_numbers:
                    return False
                unique_numbers.update(number)

        return True

    def __check_squares(self, board: list[list[str]]) -> bool:
        for row_index in range(0, self.SUDOKU_SIZE, self.SQUARE_SIZE):
            for column_index in range(0, self.SUDOKU_SIZE, self.SQUARE_SIZE):
                if not self.__check_square(board, row_index, column_index):
                    return False
        return True

    def __check_square(self, board: list[list[str]], row_index: int, column_index: int) -> bool:
        unique_numbers: set[str] = set()

        for row_offset in range(self.SQUARE_SIZE):
            for column_offset in range(self.SQUARE_SIZE):
                number = board[row_index + row_offset][column_index + column_offset]
                if number == ".":
                    continue
                if number in unique_numbers:
                    return False
                unique_numbers.update(number)
        return True
