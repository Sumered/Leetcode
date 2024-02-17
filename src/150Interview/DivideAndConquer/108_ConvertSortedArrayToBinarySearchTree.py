# type: ignore
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(val=nums[0])
        if len(nums) == 0:
            return None
        middle_index = len(nums) // 2
        head = TreeNode(val=nums[middle_index])
        head.left = self.sortedArrayToBST(nums[:middle_index])
        head.right = self.sortedArrayToBST(nums[middle_index + 1 :])

        return head


print(Solution().sortedArrayToBST([1, 3]))
