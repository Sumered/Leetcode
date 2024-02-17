# type: ignore
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.__count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.__solve(root, k)

    def __solve(self, root: TreeNode, k: int) -> int:
        if root.left is not None:
            res_left = self.__solve(root.left, k)
            if res_left != -1:
                return res_left

        self.__count += 1

        if self.__count == k:
            return root.val

        if root.right is not None:
            res_right = self.__solve(root.right, k)
            if res_right != -1:
                return res_right

        return -1
