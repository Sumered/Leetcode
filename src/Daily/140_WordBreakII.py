class Solution:
    def __init__(self) -> None:
        self.__solution: list[str] = []

    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        self.__solve(0, 1, [], s, wordDict)
        return self.__solution

    def __solve(self, start_index: int, end_index: int, current_solution: list[str], s: str, wordDict: list[str]) -> None:
        if start_index == len(s):
            self.__solution.append(" ".join(current_solution.copy()))
            return

        if end_index == len(s) + 1:
            return

        if s[start_index:end_index] in wordDict:
            current_solution.append(s[start_index:end_index])
            self.__solve(end_index, end_index + 1, current_solution, s, wordDict)
            current_solution.pop()

        self.__solve(start_index, end_index + 1, current_solution, s, wordDict)
