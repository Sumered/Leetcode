# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left, right = root, root
        left_count, right_count = 0, 0

        while left is not None:
            left_count += 1
            left = left.left
        while right is not None:
            right_count += 1
            right = right.right

        if left_count == right_count:
            return 2**left_count - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
