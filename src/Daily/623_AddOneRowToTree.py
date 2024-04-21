# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode | None, val: int, depth: int) -> TreeNode | None:
        if root is None:
            return
        if depth == 1:
            new_root = TreeNode(val, root, None)
            return new_root
        elif depth == 2:
            new_left = TreeNode(val, root.left, None)
            new_right = TreeNode(val, None, root.right)
            root.left = new_left
            root.right = new_right
            return root

        root.left = self.addOneRow(root.left, val, depth - 1)
        root.right = self.addOneRow(root.right, val, depth - 1)

        return root
