class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            medium = (left + right) // 2
            if medium * medium > x:
                right = medium
            else:
                left = medium + 1

        return left - 1
