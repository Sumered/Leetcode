class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left <= 0 or right <= 0:
            return 0

        highest_in_left = self.__calculate(left)
        highest_in_right = self.__calculate(right)

        if highest_in_left == highest_in_right:
            return highest_in_left + self.rangeBitwiseAnd(left - highest_in_left, right - highest_in_left)
        else:
            return 0

    def __calculate(self, number: int) -> int:
        power = 1
        while number > 0:
            number //= 2
            power *= 2
        return power // 2
