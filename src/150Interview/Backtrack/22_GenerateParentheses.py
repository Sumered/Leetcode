class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []

        self.__generate(n, n, [], result)

        return result

    def __generate(self, left_parentheses: int, right_parentheses: int, current_result: list[str], result: list[str]) -> None:
        if left_parentheses == 0 and right_parentheses == 0:
            if self.__validate(current_result):
                result.append("".join(current_result))
            return

        if left_parentheses != 0:
            current_result.append("(")
            self.__generate(left_parentheses - 1, right_parentheses, current_result, result)
            current_result.pop()

        if right_parentheses != 0:
            current_result.append(")")
            self.__generate(left_parentheses, right_parentheses - 1, current_result, result)
            current_result.pop()

    def __validate(self, combination: list[str]) -> bool:
        result = 0
        for char in combination:
            if char == "(":
                result += 1
            else:
                result -= 1

            if result < 0:
                return False

        return True
