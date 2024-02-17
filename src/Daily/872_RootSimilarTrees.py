# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first_root_leaves, second_root_leaves = [], []
        self.__get_leaves(root1, first_root_leaves)
        self.__get_leaves(root2, second_root_leaves)

        return first_root_leaves == second_root_leaves

    def __get_leaves(self, root: Optional[TreeNode], leaves: list[int]) -> None:
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)

        self.__get_leaves(root.left, leaves)
        self.__get_leaves(root.right, leaves)
