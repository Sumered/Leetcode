class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []

        for interval_left, interval_right in intervals:
            if newInterval[1] < interval_left:
                result.append(newInterval)
                newInterval = [interval_left, interval_right]
            elif newInterval[0] > interval_right:
                result.append([interval_left, interval_right])
            else:
                newInterval[0] = min(interval_left, newInterval[0])
                newInterval[1] = max(interval_right, newInterval[1])

        result.append(newInterval)
        return result
