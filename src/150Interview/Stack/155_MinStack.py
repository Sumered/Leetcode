# type: ignore
class MinStack:
    def __init__(self) -> None:
        self.val = int(1e9 + 7) * 3
        self.min = int(1e9 + 7) * 3
        self.previous: None | MinStack = None

    def push(self, val: int) -> None:
        new_head = MinStack()
        new_head.val = self.val
        new_head.min = self.min
        new_head.previous = self.previous

        self.val = val
        self.min = min(self.val, new_head.min)
        self.previous = new_head

    def pop(self) -> None:
        self.val = self.previous.val
        self.min = self.previous.min
        self.previous = self.previous.previous

    def top(self) -> int:
        return self.val

    def getMin(self) -> int:
        return self.min
