# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.__final_word = [123 for _ in range(8501)]

    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        self.__solve(root, [])

        return "".join(map(lambda x: chr(x + 97), self.__final_word))

    def __solve(self, root: TreeNode | None, word: list[int]) -> None:
        if root is None:
            return

        word.append(root.val)

        if root.left is None and root.right is None:
            self.__final_word = min(self.__final_word, list(reversed(word)))
            word.pop()
            return

        self.__solve(root.left, word)
        self.__solve(root.right, word)
        word.pop()

        return
