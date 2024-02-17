class Solution:
    def calculate(self, s: str) -> int:
        return self.__eval(s, 0)[0]

    def __eval(self, expression: str, index: int) -> tuple[int, int]:
        result, number, sign = 0, 0, 1

        while index < len(expression):
            token = expression[index]
            if token.isdigit():
                number = number * 10 + int(token)
            elif token == "(":
                right_result, index = self.__eval(expression, index + 1)
                result += right_result * sign
            elif token == ")":
                result += number * sign
                return result, index
            elif token in "-+":
                result += number * sign
                number = 0
                sign = -1 if token == "-" else 1
            index += 1
        return result + number * sign, index
