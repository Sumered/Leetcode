class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        result = []
        merged_interval = intervals[0]
        for interval_left, interval_right in intervals[1:]:
            if merged_interval[0] <= interval_left <= merged_interval[1]:
                merged_interval[1] = max(merged_interval[1], interval_right)
            else:
                result.append(merged_interval)
                merged_interval = [interval_left, interval_right]

        result.append(merged_interval)
        return result
