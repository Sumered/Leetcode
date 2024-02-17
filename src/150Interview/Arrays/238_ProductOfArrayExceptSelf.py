class Solution:
    def productExceptSelf(self, numbers: list[int]) -> list[int]:
        numbers_length = len(numbers)

        answer = [1 for _ in range(numbers_length + 1)]

        for index in range(numbers_length - 1, 0, -1):
            answer[index] = numbers[index] * answer[index + 1]

        prefix = 1
        for index in range(numbers_length):
            answer[index] = answer[index + 1] * prefix
            prefix *= numbers[index]

        return answer[:-1]
