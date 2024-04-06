class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, columns = len(dungeon), len(dungeon[0])
        healths = [[int(1e9) for _ in range(columns + 1)] for _ in range(rows + 1)]
        healths[rows][columns - 1] = 1
        healths[rows - 1][columns] = 1

        for row in range(rows - 1, -1, -1):
            for column in range(columns - 1, -1, -1):
                healths[row][column] = min(healths[row + 1][column], healths[row][column + 1]) - dungeon[row][column]
                healths[row][column] = 1 if healths[row][column] <= 0 else healths[row][column]

        return healths[0][0]
