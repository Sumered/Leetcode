class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        letters_count_word1: dict[str, int] = {}
        letters_count_word2: dict[str, int] = {}
        self.__count_letters(word1, letters_count_word1)
        self.__count_letters(word2, letters_count_word2)
        if letters_count_word1.keys() == letters_count_word2.keys():
            if sorted(letters_count_word1.values()) == sorted(letters_count_word2.values()):
                return True
        return False

    def __count_letters(self, word: str, counts: dict[str, int]) -> None:
        for letter in word:
            counts[letter] = counts.get(letter, 0) + 1
