class Solution:
    def __init__(self) -> None:
        self.__best_score = 0

    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        letters_count = self.__create_letters_dict(letters)
        words_letters_count = self.__create_words_dict(words)
        self.__check(0, 0, words_letters_count, letters_count, score)

        return self.__best_score

    def __check(
        self, index: int, current_score: int, words: list[dict[str, int]], letters_counts: dict[str, int], scores: list[int]
    ) -> None:
        if index == len(words):
            self.__best_score = max(self.__best_score, current_score)
            return

        can_fit, score = self.__can_fit(words[index], letters_counts, scores)
        if can_fit:
            self.__use_word(words[index], letters_counts, False)
            self.__check(index + 1, current_score + score, words, letters_counts, scores)
            self.__use_word(words[index], letters_counts, True)

        self.__check(index + 1, current_score, words, letters_counts, scores)

    def __use_word(self, word_letter_counts: dict[str, int], letters_count: dict[str, int], revert: bool) -> None:
        multiplier = -1 if not revert else 1
        for letter, count in word_letter_counts.items():
            letters_count[letter] += count * multiplier

    def __can_fit(self, word: dict[str, int], letters_counts: dict[str, int], scores: list[int]) -> tuple[bool, int]:
        score = 0

        for letter, count in word.items():
            if letter not in letters_counts:
                return False, 0
            if letters_counts[letter] < count:
                return False, 0

            score += scores[ord(letter) - ord("a")] * count

        return True, score

    def __create_letters_dict(self, letters: list[str]) -> dict[str, int]:
        letters_count: dict[str, int] = {}

        for letter in letters:
            letters_count[letter] = letters_count.get(letter, 0) + 1

        return letters_count

    def __create_words_dict(self, words: list[str]) -> list[dict[str, int]]:
        words_letters_count: list[dict[str, int]] = []

        for word in words:
            word_letters_count: dict[str, int] = {}

            for letter in word:
                word_letters_count[letter] = word_letters_count.get(letter, 0) + 1

            words_letters_count.append(word_letters_count)

        return words_letters_count


Solution().maxScoreWords(
    words=["dog", "cat", "dad", "good"],
    letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
    score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
)
