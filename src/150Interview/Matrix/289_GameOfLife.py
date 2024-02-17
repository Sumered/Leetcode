class Solution:
    def __init__(self) -> None:
        self.__directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

    def gameOfLife(self, board: list[list[int]]) -> None:
        new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        rows_count, columns_count = len(board), len(board[0])

        for row_index in range(rows_count):
            for column_index in range(columns_count):
                alive = board[row_index][column_index]

                if self.__parse_cell(board, row_index, column_index, alive):
                    new_board[row_index][column_index] = 1
                else:
                    new_board[row_index][column_index] = 0

        for row_index in range(rows_count):
            for column_index in range(columns_count):
                board[row_index][column_index] = new_board[row_index][column_index]

    def __parse_cell(self, board: list[list[int]], row: int, column: int, alive: int) -> bool:
        live_neighbors = 0
        for direction_row, direction_column in self.__directions:
            new_row, new_column = row + direction_row, column + direction_column

            if 0 <= new_row < len(board) and 0 <= new_column < len(board[0]):
                live_neighbors += board[new_row][new_column]

        return self.__parse_rules(alive, live_neighbors)

    def __parse_rules(self, alive: int, live_neighbors: int) -> bool:
        return live_neighbors == 3 or (alive == 1 and live_neighbors == 2)
