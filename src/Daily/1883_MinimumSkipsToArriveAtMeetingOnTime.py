import math


class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        correction = 0.00000001 # because with a lot of floating point operations we get some rounding error

        if sum(dist) / speed > hoursBefore:
            return -1

        n = len(dist)
        skips = [[1e11 for _ in range(n + 1)] for _ in range(n)]
        skips[0][0] = math.ceil(dist[0] / speed)
        skips[0][1] = dist[0] / speed

        for index in range(1, n):
            distance = dist[index]
            skips[index][0] = math.ceil(skips[index - 1][0] + (distance / speed) - correction)

            for skip_count in range(1, n + 1):
                without_skip = math.ceil(skips[index - 1][skip_count] + (distance / speed) - correction)
                with_skip = skips[index - 1][skip_count - 1] + (distance / speed)
                skips[index][skip_count] = min(without_skip, with_skip)

        for skip_count in range(0, n + 1):
            if skips[n - 1][skip_count] <= hoursBefore:
                return skip_count

        return -1