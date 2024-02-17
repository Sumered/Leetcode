# type: ignore
class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" | None = None, right: "TreeNode" | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
