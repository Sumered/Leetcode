# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None or head.next.next is None:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow.next

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        slow.next = None

        left, right = head, prev
        while left is not None and right is not None:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
