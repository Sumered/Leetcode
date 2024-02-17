# type: ignore
from collections import defaultdict


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        depths = defaultdict(list)
        self.__traverse_connecting(root, depths, 0)
        for depth in depths.keys():
            for index in range(len(depths[depth]) - 1):
                depths[depth][index].next = depths[depth][index + 1]
        return root

    def __traverse_connecting(self, node: Node, depths: defaultdict[int, list], depth: int) -> None:
        if node is None:
            return
        depths[depth].append(node)
        self.__traverse_connecting(node.left, depths, depth + 1)
        self.__traverse_connecting(node.right, depths, depth + 1)
