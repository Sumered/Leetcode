# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: ListNode | None) -> ListNode | None:
        result = self.__number_represented(head)

        if result == 1:
            return ListNode(1, head)
        return head

    def __number_represented(self, head: ListNode | None) -> int:
        if head is None:
            return 0

        offset = self.__number_represented(head.next)

        head.val *= 2
        head.val += offset

        if head.val >= 10:
            head.val -= 10
            return 1

        return 0
