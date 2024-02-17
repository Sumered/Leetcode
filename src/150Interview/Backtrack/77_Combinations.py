class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        answer: list[list[int]] = []
        self.__backtrack(list(range(1, n + 1)), 0, k, answer, [])
        return answer

    def __backtrack(self, numbers: list[int], index: int, k: int, answer: list[list[int]], current_answer: list[int]) -> None:
        if index == len(numbers):
            if k == len(current_answer):
                answer.append(current_answer.copy())

            return

        current_answer.append(numbers[index])
        self.__backtrack(numbers, index + 1, k, answer, current_answer)
        current_answer.pop()
        self.__backtrack(numbers, index + 1, k, answer, current_answer)
