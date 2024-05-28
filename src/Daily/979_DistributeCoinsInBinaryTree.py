class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.__total_cost = 0

    def distributeCoins(self, root: TreeNode | None) -> int:
        self.__move_coins_up(root, None)
        self.__move_coins_down(root)

        return self.__total_cost

    def __move_coins_up(self, root: TreeNode | None, parent: TreeNode | None) -> tuple[int, int]:
        if root is None:
            return 0, 0

        left_subtree_size, left_subtree_coins = self.__move_coins_up(root.left, root)
        right_subtree_size, right_subtree_coins = self.__move_coins_up(root.right, root)

        my_size = left_subtree_size + right_subtree_size + 1
        my_coins = left_subtree_coins + right_subtree_coins + root.val

        if my_coins > my_size:
            if parent is not None:
                my_diff = my_coins - my_size
                parent.val += my_diff
                self.__total_cost += my_diff
                root.val -= my_diff

        return my_size, min(my_size, my_coins)

    def __move_coins_down(self, root: TreeNode | None) -> None:
        if root is None:
            return

        left_subtree_size, left_subtree_coins = self.__get_size_and_coins(root.left)
        right_subtree_size, right_subtree_coins = self.__get_size_and_coins(root.right)

        if left_subtree_size > left_subtree_coins and root.left is not None:
            left_diff = left_subtree_size - left_subtree_coins
            root.left.val += left_diff
            root.val -= left_diff
            self.__total_cost += left_diff

        if right_subtree_size > right_subtree_coins and root.right is not None:
            right_diff = right_subtree_size - right_subtree_coins
            root.right.val += right_diff
            root.val -= right_diff
            self.__total_cost += right_diff

        self.__move_coins_down(root.left)
        self.__move_coins_down(root.right)

    def __get_size_and_coins(self, root: TreeNode | None) -> tuple[int, int]:
        if root is None:
            return 0, 0

        left_subtree_size, left_subtree_coins = self.__get_size_and_coins(root.left)
        right_subtree_size, right_subtree_coins = self.__get_size_and_coins(root.right)

        return left_subtree_size + right_subtree_size + 1, left_subtree_coins + right_subtree_coins + root.val
