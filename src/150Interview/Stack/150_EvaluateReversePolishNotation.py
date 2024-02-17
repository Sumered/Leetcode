from operator import add, mul, sub, truediv


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        operators = {"*": mul, "+": add, "-": sub, "/": truediv}

        for token in tokens:
            if token in operators:
                left, right = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(operators[token](left, right)))
            else:
                stack.append(int(token))

        return stack[0]
