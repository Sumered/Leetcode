from collections import deque


class Solution:
    def __init__(self) -> None:
        self.__directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.__inf = int(1e9)

    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        safeness = [[self.__inf for _ in range(n)] for _ in range(n)]
        self.__get_safeness(grid, safeness)

        max_safeness = self.__get_max_safeness(safeness)

        return max_safeness

    def __get_safeness(self, grid: list[list[int]], safeness: list[list[int]]) -> None:
        n = len(grid)
        thieves: deque[tuple[int, int]] = deque()

        for row in range(n):
            for column in range(n):
                if grid[row][column] == 1:
                    thieves.append((row, column))
                    safeness[row][column] = 0

        while thieves:
            row, column = thieves.popleft()

            for direction in self.__directions:
                new_row, new_column = row + direction[0], column + direction[1]

                if new_row >= 0 and new_row < n and new_column >= 0 and new_column < n:
                    if safeness[new_row][new_column] == self.__inf:
                        thieves.append((new_row, new_column))
                        safeness[new_row][new_column] = safeness[row][column] + 1

    def __get_max_safeness(self, safeness: list[list[int]]) -> int:
        low, high = 0, 400 * 400 + 1
        best_result = 0

        while low <= high:
            mid = (low + high) // 2
            can_reach = self.__can_reach(safeness, mid)
            if can_reach:
                best_result = mid
                low = mid + 1
            else:
                high = mid - 1

        return best_result

    def __can_reach(self, safeness: list[list[int]], minimal_safeness: int) -> bool:
        n = len(safeness)
        path: deque[tuple[int, int]] = deque()
        visited = [[False for _ in range(n)] for _ in range(n)]

        if safeness[0][0] >= minimal_safeness:
            path.append((0, 0))
            visited[0][0] = True

        while path:
            row, column = path.popleft()

            if row == n - 1 and column == n - 1:
                return True

            for direction in self.__directions:
                new_row, new_column = row + direction[0], column + direction[1]

                if new_row >= 0 and new_row < n and new_column >= 0 and new_column < n:
                    if safeness[new_row][new_column] >= minimal_safeness and not visited[new_row][new_column]:
                        path.append((new_row, new_column))
                        visited[new_row][new_column] = True

        return False
