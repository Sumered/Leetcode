# type: ignore
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node: TreeNode, lower=-int(1e18 + 7), higher=int(1e18 + 7)) -> bool:
            if node is None:
                return True

            if not lower < node.val < higher:
                return False

            return check(node.left, lower, node.val) and check(node.right, node.val, higher)

        return check(root)
