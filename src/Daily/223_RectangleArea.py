class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        first_area = (ax2 - ax1) * (ay2 - ay1)
        second_area = (bx2 - bx1) * (by2 - by1)
        union_width = min(ax2, bx2) - max(ax1, bx1)
        union_height = min(ay2, by2) - max(ay1, by1)
        if union_width < 0 or union_height < 0:
            return first_area + second_area
        else:
            return first_area + second_area - (union_width * union_height)
