class Solution:
    def climbStairs(self, n: int) -> int:
        solution = [0 for _ in range(n + 1)]
        solution[0] = solution[1] = 1
        for i in range(2, n + 1):
            solution[i] = solution[i - 1] + solution[i - 2]

        return solution[n]
