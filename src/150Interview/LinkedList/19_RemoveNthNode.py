# type: ignore
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.__from_last = 0

    def removeNthFromEnd(self, head: "ListNode" | None, n: int) -> "ListNode" | None:
        dummy = ListNode(next=head)
        self.__remove_nth(dummy, n)
        return dummy.next

    def __remove_nth(self, head: "ListNode" | None, n: int) -> None:
        if head == None:
            return

        self.__remove_nth(head.next, n)
        self.__from_last += 1

        if self.__from_last == n + 1:
            head.next = head.next.next
