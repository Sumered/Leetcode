class Solution:
    def __init__(self) -> None:
        self.keyboard = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits: str) -> list[str]:
        answer: list[str] = []
        if digits:
            self.__backtrack(digits, 0, [], answer)
        return answer

    def __backtrack(self, digits: str, index: int, current_word: list[str], combinations: list[str]) -> None:
        if index == len(digits):
            combinations.append("".join(current_word))
            return

        key = digits[index]

        for char in self.keyboard[key]:
            current_word.append(char)
            self.__backtrack(digits, index + 1, current_word, combinations)
            current_word.pop()
