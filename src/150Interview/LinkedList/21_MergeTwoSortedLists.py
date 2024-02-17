# type: ignore
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        current = head = ListNode()

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1, current = list1.next, current.next
            else:
                current.next = ListNode(list2.val)
                list2, current = list2.next, current.next

        if list1 != None or list2 != None:
            current.next = list1 if list1 else list2

        return head.next
