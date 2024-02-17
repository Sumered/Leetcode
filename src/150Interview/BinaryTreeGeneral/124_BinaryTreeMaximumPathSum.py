# type: ignore
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.__maxSum = int(-1e9)

    def maxPathSum(self, root: TreeNode | None) -> int:
        self.__traverse(root)
        return self.__maxSum

    def __traverse(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_result = self.__traverse(root.left)
        right_result = self.__traverse(root.right)
        self.__maxSum = max(max(left_result, 0) + max(right_result, 0) + root.val, self.__maxSum)

        return max(max(left_result, 0), max(right_result, 0)) + root.val
