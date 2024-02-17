# type: ignore
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0

        if root is None:
            return result

        result += root.val if low <= root.val <= high else 0
        left = self.rangeSumBST(root.left, low, high) if root.val >= low else 0
        right = self.rangeSumBST(root.right, low, high) if root.val <= high else 0

        return result + left + right
