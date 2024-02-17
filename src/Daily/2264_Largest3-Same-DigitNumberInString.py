class Solution:
    def largestGoodInteger(self, num: str) -> str:
        actual_string = ""
        for index in range(len(num[:-2])):
            if num[index] == num[index + 1] and num[index + 1] == num[index + 2]:
                actual_string = max(actual_string, num[index] * 3)

        return actual_string
