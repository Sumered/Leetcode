# type: ignore


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(val=-200, next=head)
        self.__delete_duplicates(head, dummy_node)
        return dummy_node.next

    def __delete_duplicates(self, head: Optional[ListNode], previous: Optional[ListNode]) -> None:
        if head == None:
            return head

        if head.next != None and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head.next = head.next.next
            previous.next = head.next
            head.next = None

            self.__delete_duplicates(previous.next, previous)
        else:
            self.__delete_duplicates(head.next, head)
