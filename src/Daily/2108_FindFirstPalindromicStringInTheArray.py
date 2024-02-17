class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.__palindromic(word):
                return word

        return ""

    def __palindromic(self, word: str) -> bool:
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1

        return True
