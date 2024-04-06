class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []
        for character in s:
            if stack and abs(ord(character) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(character)

        return "".join(stack)
