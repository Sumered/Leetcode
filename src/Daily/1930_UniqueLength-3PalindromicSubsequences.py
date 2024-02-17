class Solution:
    letters_in_alphabet = 26
    letters_indexes = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25,
    }

    def countPalindromicSubsequence(self, word: str) -> int:
        palindromes_count = 0

        occurred = [[False for _ in range(self.letters_in_alphabet)] for _ in range(self.letters_in_alphabet)]

        last_occurrence = [int(1e6) for _ in range(self.letters_in_alphabet)]
        self.__find_last_occurrences(word, last_occurrence)

        already_found_letters: list[str] = []

        for current_index, letter in enumerate(word):
            palindromes_count += self.__add_found_palindromes(letter, current_index, already_found_letters, occurred, last_occurrence)
            if letter not in already_found_letters:
                already_found_letters.append(letter)

        return palindromes_count

    def __find_last_occurrences(self, word: str, last_occurrence: list[int]) -> None:
        found_count = 0

        for i in range(len(word) - 1, 0, -1):
            index = self.letters_indexes[word[i]]
            if last_occurrence[index] == 1e6:
                last_occurrence[index] = i
                found_count += 1

            if found_count == self.letters_in_alphabet:
                break

        return

    def __add_found_palindromes(
        self,
        letter: str,
        current_index: int,
        already_found_letters: list[str],
        occurred: list[list[bool]],
        last_occurence: list[int],
    ) -> int:
        new_palindromes_found = 0

        for found_letter in already_found_letters:
            current_letter_index = self.letters_indexes[letter]
            found_letter_index = self.letters_indexes[found_letter]

            if occurred[found_letter_index][current_letter_index]:
                continue
            else:
                if last_occurence[found_letter_index] > current_index and last_occurence[found_letter_index] != int(1e6):
                    occurred[found_letter_index][current_letter_index] = True
                    new_palindromes_found += 1
        return new_palindromes_found


solution = Solution()
print(solution.countPalindromicSubsequence("bbcbaba"))
