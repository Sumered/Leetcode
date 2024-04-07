from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
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
