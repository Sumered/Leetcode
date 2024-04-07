from functools import cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_parentheses, wildcards = [], []

        for index in range(len(s)):
            character = s[index]
            if character == "(":
                open_parentheses.append(index)
            elif character == ")":
                if open_parentheses:
                    open_parentheses.pop()
                elif wildcards:
                    wildcards.pop()
                else:
                    return False
            else:
                wildcards.append(index)

        while open_parentheses and wildcards:
            open_index = open_parentheses.pop()
            wildcard_index = wildcards.pop()
            if wildcard_index < open_index:
                return False

        return True and not open_parentheses

    def checkValidString_3dDP(self, s: str) -> bool:
        dp = [[[False for _ in range(len(s) + 1)] for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        dp[0][0][0] = True

        for index in range(len(s)):
            character = s[index]
            dp_index = index + 1
            if character == "(":
                for left_index in range(len(s)):
                    for right_index in range(len(s)):
                        if dp[dp_index - 1][left_index][right_index]:
                            dp[dp_index][left_index + 1][right_index] = True
            elif character == ")":
                for left_index in range(len(s)):
                    for right_index in range(len(s)):
                        if dp[dp_index - 1][left_index][right_index] and left_index > right_index:
                            dp[dp_index][left_index][right_index + 1] = True
            else:
                for left_index in range(len(s)):
                    for right_index in range(len(s)):
                        if dp[dp_index - 1][left_index][right_index]:
                            dp[dp_index][left_index][right_index] = True
                            dp[dp_index][left_index + 1][right_index] = True
                            if left_index > right_index:
                                dp[dp_index][left_index][right_index + 1] = True

        for equal_index in range(len(s)):
            if dp[len(s)][equal_index][equal_index]:
                return True
        return False

    def checkValidString_recurrent(self, s: str) -> bool:
        return self.__check_recurrent(s, 0, 0, 0)

    @cache
    def __check_recurrent(self, s: str, index: int, left: int, right: int) -> bool:
        if index == len(s):
            if left == right:
                return True
            else:
                return False

        character = s[index]
        if character == "(":
            return self.__check_recurrent(s, index + 1, left + 1, right)
        elif character == ")":
            if left > right:
                return self.__check_recurrent(s, index + 1, left, right + 1)
        else:
            as_left = self.__check_recurrent(s, index + 1, left + 1, right)
            as_right = False
            if left > right:
                as_right = self.__check_recurrent(s, index + 1, left, right + 1)
            as_none = self.__check_recurrent(s, index + 1, left, right)
            return as_left or as_right or as_none

        return False
