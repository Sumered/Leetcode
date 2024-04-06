class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        to_take = [True for _ in range(len(s))]

        cumulative = 0
        for index in range(len(s)):
            character = s[index]
            if character == "(":
                cumulative += 1
            elif character == ")":
                if cumulative == 0:
                    to_take[index] = False
                else:
                    cumulative -= 1

        cumulative = 0

        for index in range(len(s) - 1, -1, -1):
            character = s[index]
            if character == ")":
                cumulative += 1
            elif character == "(":
                if cumulative == 0:
                    to_take[index] = False
                else:
                    cumulative -= 1

        stack = []
        for index, character in enumerate(s):
            if to_take[index]:
                stack.append(character)

        return "".join(stack)
