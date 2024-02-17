# type: ignore
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        depth_nodes = {}
        self.__traverse(root, depth_nodes, 0)
        return list(depth_nodes.values())

    def __traverse(self, node: TreeNode, depth_nodes: dict[int, int], depth: int) -> None:
        if node is None:
            return
        if depth not in depth_nodes:
            depth_nodes[depth] = node.val

        self.__traverse(node.right, depth_nodes, depth + 1)
        self.__traverse(node.left, depth_nodes, depth + 1)
