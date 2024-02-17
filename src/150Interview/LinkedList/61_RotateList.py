# type: ignore
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.__from_last = 0
        self.__linked_list_len = 0

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        self.__calculate_len(head)
        k = k % self.__linked_list_len
        if k == 0:
            return head
        new_head = self.__rotate(head, head, None, k)

        return new_head

    def __rotate(
        self, head: Optional[ListNode], first_node: Optional[ListNode], previous: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = self.__rotate(head.next, first_node, head, k)
        if new_head is not None:
            return new_head

        self.__from_last += 1

        if head.next is None:
            head.next = first_node

        if self.__from_last == k:
            previous.next = None
            return head
        return None

    def __calculate_len(self, head: Optional[ListNode]) -> None:
        while head is not None:
            self.__linked_list_len += 1
            head = head.next
