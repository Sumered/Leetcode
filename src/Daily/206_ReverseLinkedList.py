# type: ignore
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        new_head = self.__reverse(head, None)

        return new_head

    def __reverse(self, head: ListNode | None, previous: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        if head.next is None:
            head.next = previous
            return head

        new_head = self.__reverse(head.next, head)
        head.next = previous
        return new_head
