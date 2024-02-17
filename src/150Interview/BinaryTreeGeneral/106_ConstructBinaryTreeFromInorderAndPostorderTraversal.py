# type: ignore
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.__inorder_mapping = {}

    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        self.__inorder_mapping = {value: index for index, value in enumerate(inorder)}
        return self.__construct(postorder, 0, len(postorder) - 1)

    def __construct(self, preorder: list[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        node = TreeNode(preorder.pop())
        index = self.__inorder_mapping[node.val]
        node.right = self.__construct(preorder, index + 1, right)
        node.left = self.__construct(preorder, left, index - 1)
        return node
