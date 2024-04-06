# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True

        slow, fast = head, head
        previous = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next

            temporary = slow.next
            slow.next = previous
            previous = slow
            slow = temporary

        if fast is not None:
            slow = slow.next

        while previous is not None and slow is not None:
            if previous.val != slow.val:
                return False
            previous = previous.next
            slow = slow.next

        return True
