class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        points.sort()
        max_area, previous_point = 0, points[0]

        for point in points[1:]:
            max_area = max(max_area, point[0] - previous_point[0])
            previous_point = point

        return max_area
