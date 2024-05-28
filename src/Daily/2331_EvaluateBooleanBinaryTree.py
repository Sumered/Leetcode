# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return False

        if root.left == None and root.right == None:
            return bool(root.val)

        left_eval = self.evaluateTree(root.left)
        right_eval = self.evaluateTree(root.right)

        if root.val == 2:
            return left_eval or right_eval
        else:
            return left_eval and right_eval
