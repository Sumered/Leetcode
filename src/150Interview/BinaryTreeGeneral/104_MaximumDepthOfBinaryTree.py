class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        return self.__solve(root) if root is not None else 0

    def __solve(self, root: TreeNode) -> int:
        result = 1
        if root.left is not None:
            result = max(result, self.__solve(root.left) + 1)
        if root.right is not None:
            result = max(result, self.__solve(root.right) + 1)
        return result
