class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letters_count_s: dict[str, int] = {}
        letters_count_t: dict[str, int] = {}
        self.__count_letters(s, letters_count_s)
        self.__count_letters(t, letters_count_t)

        result = 0
        for letter, count in letters_count_s.items():
            result += max(0, count - letters_count_t.get(letter, 0))

        return result

    def __count_letters(self, word: str, counter: dict[str, int]) -> None:
        for letter in word:
            counter[letter] = counter.get(letter, 0) + 1
