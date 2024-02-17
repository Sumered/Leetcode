class Solution:
    def arrayStringsAreEqual(self, first_words: list[str], second_words: list[str]) -> bool:
        first_word = "".join(first_words)
        second_word = "".join(second_words)
        return first_word == second_word
