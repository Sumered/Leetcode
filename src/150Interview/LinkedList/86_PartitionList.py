# type: ignore
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_nodes = ListNode()
        bigger_nodes = ListNode()
        self.__split(head, smaller_nodes, bigger_nodes, x)
        new_head = ListNode()
        self.__attach(new_head, smaller_nodes.next, bigger_nodes.next)
        return new_head.next

    def __attach(self, head: Optional[ListNode], smaller_nodes: Optional[ListNode], bigger_nodes: Optional[ListNode]) -> None:
        if bigger_nodes is None and smaller_nodes is None:
            return None
        elif bigger_nodes is None:
            head.next = smaller_nodes
            self.__attach(head.next, smaller_nodes.next, bigger_nodes)
        elif smaller_nodes is None:
            head.next = bigger_nodes
            self.__attach(head.next, smaller_nodes, bigger_nodes.next)
        else:
            head.next = smaller_nodes
            self.__attach(head.next, smaller_nodes.next, bigger_nodes)

    def __split(self, head: Optional[ListNode], smaller_nodes: Optional[ListNode], bigger_nodes: Optional[ListNode], x) -> None:
        if head is None:
            smaller_nodes.next = None
            bigger_nodes.next = None
            return None

        if head.val < x:
            smaller_nodes.next = head
            self.__split(head.next, smaller_nodes.next, bigger_nodes, x)
        else:
            bigger_nodes.next = head
            self.__split(head.next, smaller_nodes, bigger_nodes.next, x)


print(Solution().partition(ListNode(1, None), 2))
