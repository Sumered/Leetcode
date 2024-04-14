# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None, is_left: bool = False) -> int:
        result = 0
        if root is None:
            return result

        if root.left is None and root.right is None:
            if is_left:
                result += root.val
        else:
            result += self.sumOfLeftLeaves(root.left, True)
            result += self.sumOfLeftLeaves(root.right, False)

        return result
