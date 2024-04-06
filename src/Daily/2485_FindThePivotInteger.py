class Solution:
    def pivotInteger(self, n: int) -> int:
        full_sum = ((n + 1) * n) // 2
        current_sum = 0

        for i in range(1, n + 1):
            current_sum += i
            if current_sum == full_sum - current_sum + i:
                return i

        return -1
