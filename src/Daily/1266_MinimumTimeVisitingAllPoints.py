class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total_cost = 0
        current_point = points[0]

        for point in points[1:]:
            travel_vector = [abs(point[0] - current_point[0]), abs(point[1] - current_point[1])]
            total_cost += max(travel_vector)
            current_point = point

        return total_cost


algos = Solution()
print(algos.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
