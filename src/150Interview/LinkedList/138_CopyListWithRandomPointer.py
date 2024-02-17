# type: ignore


class Node:
    def __init__(self, x: int, next: "Node" | None = None, random: "Node" | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        self.__copy_head(head)
        self.__fill_random(head)
        head, new_head = self.__separate(head)

        return new_head

    def __copy_head(self, head: "Node") -> None:
        if head == None:
            return
        new_head = Node(head.val, head.next)
        head.next = new_head

        self.__copy_head(head.next.next)

    def __fill_random(self, head: "Node") -> None:
        if head == None:
            return
        if head.random:
            head.next.random = head.random.next
        self.__fill_random(head.next.next)

    def __separate(self, head: "Node") -> tuple["Node", "Node"]:
        if head == None:
            return None, None
        new_head = head.next
        head.next = head.next.next
        new_head.next = new_head.next.next if new_head.next else None
        self.__separate(head.next)

        return head, new_head
