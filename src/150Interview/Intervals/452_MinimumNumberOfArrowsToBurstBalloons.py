class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()

        arrows_needed, current_point = 0, points[0]
        for point in points[1:]:
            if self.__is_intersecting(current_point, point):
                current_point = [max(current_point[0], point[0]), min(current_point[1], point[1])]
            else:
                arrows_needed += 1
                current_point = point

        return arrows_needed + 1

    def __is_intersecting(self, interval: list[int], second_interval: list[int]) -> bool:
        inside_second = second_interval[0] < interval[0] and interval[1] < second_interval[1]
        intersects = interval[0] <= second_interval[0] <= interval[1] or interval[0] <= second_interval[1] <= interval[1]

        return inside_second or intersects
