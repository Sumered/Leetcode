# type: ignore


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        digits = []
        passed_val = 0

        while l1 is not None and l2 is not None:
            sum_of_digits = l1.val + l2.val + passed_val
            digits.append(sum_of_digits % 10)
            passed_val = sum_of_digits // 10
            l1 = l1.next
            l2 = l2.next

        passed_val = self.__finalize(digits, l1, passed_val)
        passed_val = self.__finalize(digits, l2, passed_val)

        if passed_val != 0:
            digits.append(1)

        answer = self.__create_answer(digits, 0)

        return answer

    def __create_answer(self, digits: list[int], iterator: int) -> ListNode:
        if iterator >= len(digits):
            return None
        new_node = ListNode()
        new_node.val = digits[iterator]
        new_node.next = self.__create_answer(digits, iterator + 1)
        return new_node

    def __finalize(self, digits: list[int], node: ListNode, passed_val: int):
        while node is not None:
            sum_of_digits = node.val + passed_val
            digits.append(sum_of_digits % 10)
            passed_val = sum_of_digits // 10
            node = node.next
        return passed_val


algos = Solution()
l1 = ListNode(9, ListNode(9, ListNode(1)))
l2 = ListNode(
    1,
)
result = algos.addTwoNumbers(l1, l2)

while result is not None:
    print(result.val)
    result = result.next
