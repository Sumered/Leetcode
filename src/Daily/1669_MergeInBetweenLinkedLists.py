# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start_node, end_node = self.__get_start_end(list1, a, b)
        start_node.next = list2
        while list2.next != None:
            list2 = list2.next
        list2.next = end_node

        return list1

    def __get_start_end(self, list1: ListNode, a: int, b: int) -> tuple[ListNode, ListNode]:
        position = 0
        helper_node = list1
        while position < a - 1:
            helper_node = helper_node.next
            position += 1
        start_node = helper_node
        while position <= b:
            helper_node = helper_node.next
            position += 1
        end_node = helper_node

        return start_node, end_node
