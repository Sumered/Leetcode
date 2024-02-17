class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = "".join(map(str, digits))
        number = str(int(number) + 1)
        return [int(c) for c in number]

    def iterative_plusOne(self, digits: list[int]) -> list[int]:
        addition = 1
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] + addition == 10:
                digits[index] = 0
            else:
                digits[index] += addition
                addition = 0
                break
        if addition == 1:
            digits.insert(0, 1)
        return digits
