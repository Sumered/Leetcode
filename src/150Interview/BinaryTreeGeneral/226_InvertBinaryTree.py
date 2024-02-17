# type: ignore
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" | None = None, right: "TreeNode" | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root == None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)  # type: ignore

        return root
