class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth, max_depth = 0, 0
        for char in s:
            if char == "(":
                current_depth += 1
            elif char == ")":
                current_depth -= 1
            max_depth = max(max_depth, current_depth)

        return max_depth
