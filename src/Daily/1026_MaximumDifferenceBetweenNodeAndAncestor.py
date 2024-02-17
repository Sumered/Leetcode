# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.__maxDiff = -1

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.__findDiff(root, root.val, root.val)

        return self.__maxDiff

    def __findDiff(self, root: Optional[TreeNode], min_occured: int, max_occured: int) -> None:
        if root is None:
            return 0

        min_occured = min(min_occured, root.val)
        max_occured = max(max_occured, root.val)

        self.__maxDiff = max(self.__maxDiff, max_occured - min_occured)

        self.__findDiff(root.left, min_occured, max_occured)
        self.__findDiff(root.right, min_occured, max_occured)

        return None
