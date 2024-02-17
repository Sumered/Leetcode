class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        dp = [[[0 for _ in range(columns)] for _ in range(columns)] for _ in range(rows + 1)]

        for row in range(rows - 1, -1, -1):
            for first_robot_pos in range(columns):
                for second_robot_pos in range(columns):
                    cherries = grid[row][first_robot_pos] + grid[row][second_robot_pos]

                    if first_robot_pos == second_robot_pos:
                        cherries //= 2

                    most_cherries = self.__find_most_cherries(row + 1, first_robot_pos, second_robot_pos, dp, columns)
                    dp[row][first_robot_pos][second_robot_pos] = cherries + most_cherries

        return dp[0][0][columns - 1]

    def __find_most_cherries(self, row: int, first_robot_pos: int, second_robot_pos: int, dp: list[list[list[int]]], limit: int) -> int:
        most_cherries = 0

        for first_offset in range(-1, 2, 1):
            first_offset_pos = first_robot_pos + first_offset

            if first_offset_pos < 0 or first_offset_pos >= limit:
                continue

            for second_offset in range(-1, 2, 1):
                second_offset_pos = second_robot_pos + second_offset

                if second_offset_pos < 0 or second_offset_pos >= limit:
                    continue

                most_cherries = max(most_cherries, dp[row][first_offset_pos][second_offset_pos])

        return most_cherries
