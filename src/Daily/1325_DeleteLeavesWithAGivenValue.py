# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: "TreeNode | None", target: int) -> "TreeNode | None":
        if root is None:
            return root

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.left is None and root.right is None:
            if root.val == target:
                return None

        return root
