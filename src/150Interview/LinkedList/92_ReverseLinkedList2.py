# type: ignore
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.__rightmost = None
        self.__last_rightmost = None

    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy_node = ListNode(next=head)
        self.__reverseBetween(dummy_node, left, right, None, 0)
        return dummy_node.next

    def __reverseBetween(self, head: ListNode | None, left: int, right: int, previous_node: ListNode | None, index: int) -> None:
        if head is None:
            return

        self.__reverseBetween(head.next, left, right, head, index + 1)

        if left < index <= right:
            head.next = previous_node
        if index == right:
            self.__last_rightmost = head
        if index == right + 1:
            self.__rightmost = head
            return
        if index == left:
            head.next = self.__rightmost
        if index == left - 1:
            head.next = self.__last_rightmost
