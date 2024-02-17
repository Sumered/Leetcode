# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.__sum(root, targetSum, 0)

    def __sum(self, root: Optional[TreeNode], targetSum: int, current_sum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return current_sum + root.val == targetSum
        else:
            return self.__sum(root.left, targetSum, current_sum + root.val) or self.__sum(root.right, targetSum, current_sum + root.val)
