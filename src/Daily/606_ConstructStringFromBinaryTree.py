# type: ignore
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode | None) -> str:
        result = str(root.val)  # type: ignore
        result = self.__solve(root, result)
        return result

    def __solve(self, root: TreeNode | None, result: str) -> str:
        if root.left is not None:
            result += "(" + str(root.left.val)
            result = self.__solve(root.left, result)
            result += ")"
        if root.right is not None:
            if root.left is None:
                result += "()"
            result += "(" + str(root.right.val)
            result = self.__solve(root.right, result)
            result += ")"
        return result
