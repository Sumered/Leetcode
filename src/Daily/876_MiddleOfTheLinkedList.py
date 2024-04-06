# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        list_length = self.__get_list_len(head, 0)
        middle_point = list_length // 2
        middle_node = self.__get_middle_node(head, middle_point, 0)

        return middle_node

    def __get_middle_node(self, node: ListNode | None, middle_point: int, depth: int) -> ListNode:
        if depth == middle_point:
            return node

        return self.__get_middle_node(node.next, middle_point, depth + 1)

    def __get_list_len(self, node: ListNode | None, depth: int) -> int:
        if node is None:
            return depth

        return self.__get_list_len(node.next, depth + 1)
