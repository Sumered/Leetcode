class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return len(points)

        linear_equations: dict[tuple[float, float], set] = {}
        for index_a in range(len(points)):
            for index_b in range(index_a + 1, len(points)):
                point_a, point_b = points[index_a], points[index_b]
                linear_func = self.get_linear_func(point_a, point_b)
                if linear_func not in linear_equations:
                    linear_equations[linear_func] = set()
                linear_equations[linear_func].add(tuple(point_a))
                linear_equations[linear_func].add(tuple(point_b))

        return max(len(value) for value in linear_equations.values())

    def get_linear_func(self, point_a: list[int], point_b: list[int]) -> tuple[float, float]:
        diff_x = point_a[0] - point_b[0]

        if diff_x == 0:
            lin_func: tuple[float, float] = (point_a[0], 0)
        else:
            ax = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])
            bx = (point_a[0] * point_b[1] - point_a[1] * point_b[0]) / diff_x
            lin_func = (ax, bx)

        return lin_func
