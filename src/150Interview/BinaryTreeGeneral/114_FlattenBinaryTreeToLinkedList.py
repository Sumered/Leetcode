# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.flatten(root.left)
        leftmost = root.left
        if leftmost is None:
            self.flatten(root.right)
        else:
            while leftmost.right is not None:
                leftmost = leftmost.right
            right_node = root.right
            leftmost.right = right_node
            root.right = root.left
            root.left = None
            self.flatten(right_node)
        return
