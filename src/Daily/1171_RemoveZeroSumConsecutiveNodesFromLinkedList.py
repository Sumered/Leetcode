# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        helping_node = ListNode(val=0, next=head)
        prefix_sums = {0: helping_node}
        current_sum, current = 0, head

        while current:
            current_sum += current.val

            if current_sum in prefix_sums:
                next_node = prefix_sums[current_sum].next
                temporary_sum = current_sum + next_node.val

                while next_node != current:
                    del prefix_sums[temporary_sum]
                    next_node = next_node.next
                    temporary_sum += next_node.val
                prefix_sums[current_sum].next = current.next
            else:
                prefix_sums[current_sum] = current
            current = current.next

        return helping_node.next
