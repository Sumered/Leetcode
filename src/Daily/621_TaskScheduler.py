from queue import PriorityQueue


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequencies = [0] * 26

        for task in tasks:
            frequencies[ord(task) - ord("A")] += 1
        frequencies.sort()

        count = frequencies[25] - 1
        idle_time = count * n

        for i in range(25):
            idle_time -= min(count, frequencies[i])

        return len(tasks) + max(idle_time, 0)
