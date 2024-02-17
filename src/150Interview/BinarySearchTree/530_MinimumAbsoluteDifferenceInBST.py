# type: ignore
class TreeNode:
    def __init__(self, val=0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.__solve(root, -(10**6), 10**6)

    def __solve(self, node: TreeNode, lower: int, higher: int) -> int:
        if node is None:
            return higher - lower

        left_result = self.__solve(node.left, lower, node.val)
        right_result = self.__solve(node.right, node.val, higher)

        return min(left_result, right_result)
