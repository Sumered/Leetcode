from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.paths_count = 0

    def pseudoPalindromicPaths(self, root: TreeNode | None) -> int:
        self.__traverse(root, defaultdict(int))
        return self.paths_count

    def __traverse(self, root: TreeNode | None, current: defaultdict[int, int]) -> None:
        if root is None:
            return

        current[root.val] += 1

        if root.left is None and root.right is None:
            if self.__valid(current):
                self.paths_count += 1
            current[root.val] -= 1
            return

        self.__traverse(root.left, current)
        self.__traverse(root.right, current)
        current[root.val] -= 1

    def __valid(self, current: dict[int, int]) -> bool:
        odd_count = 0
        for count in current.values():
            odd_count += 1 if count % 2 == 1 else 0

        return odd_count <= 1
