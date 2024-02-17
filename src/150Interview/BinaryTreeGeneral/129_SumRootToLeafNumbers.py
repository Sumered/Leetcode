# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.__traverse(root, 0)
        return self.sum

    def __traverse(self, root: Optional[TreeNode], current: int) -> None:
        if root is None:
            return
        current *= 10
        current += root.val

        if root.left is None and root.right is None:
            self.sum += current
            return

        self.__traverse(root.left, current)
        self.__traverse(root.right, current)

        return
