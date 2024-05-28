# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        fake_head = ListNode(100000000, head)

        a = self.__remove_nodes(head, fake_head)  # type: ignore

        return fake_head.next

    def __remove_nodes(self, head: ListNode, previous: ListNode) -> int:
        if head.next == None:
            return head.val

        max_on_right = self.__remove_nodes(head.next, head)

        if head.val < max_on_right:
            previous.next = head.next

        return max(max_on_right, head.val)
