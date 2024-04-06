class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()

        result = 0
        current_point = [-int(8e9), -int(8e9)]

        for point in points:
            if self.__intersects(point, current_point):
                current_point = [max(current_point[0], point[0]), min(current_point[1], point[1])]
            else:
                current_point = point
                result += 1

        return result

    def __intersects(self, point: list[int], current_point: list[int]) -> bool:
        return not (point[1] < current_point[0] or point[0] > current_point[1])
