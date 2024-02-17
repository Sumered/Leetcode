# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.maxDistance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.infect(root, start)
        return self.maxDistance

    def infect(self, root: Optional[TreeNode], start: int) -> int:
        depth = 0
        if root == None:
            return depth

        left_max_distance = self.infect(root.left, start)
        right_max_distance = self.infect(root.right, start)

        if root.val == start:
            self.maxDistance = max(left_max_distance, right_max_distance)
            depth = -1
        elif left_max_distance >= 0 and right_max_distance >= 0:
            depth = max(left_max_distance, right_max_distance) + 1
        else:
            distance = abs(left_max_distance) + abs(right_max_distance)
            self.maxDistance = max(self.maxDistance, distance)
            depth = min(left_max_distance, right_max_distance) - 1
        return depth
