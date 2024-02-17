class Solution:
    def maxLength(self, arr: list[str]) -> int:
        max_length = 0

        def backtrack(index: int, word: str) -> None:
            nonlocal max_length
            if len(word) != len(set(word)):
                return

            max_length = max(max_length, len(word))

            for i in range(index, len(arr)):
                backtrack(i + 1, word + arr[i])

        backtrack(0, "")
        return max_length


Solution().maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"])
