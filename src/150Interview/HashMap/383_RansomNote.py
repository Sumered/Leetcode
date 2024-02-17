class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters_in_ransom: dict[str, int] = {}
        letters_in_magazine: dict[str, int] = {}

        self.__fill_letters(ransomNote, letters_in_ransom)
        self.__fill_letters(magazine, letters_in_magazine)

        return self.__check_containment(letters_in_ransom, letters_in_magazine)

    def __fill_letters(self, word: str, letters_dict: dict[str, int]) -> None:
        for character in word:
            letters_dict[character] = letters_dict.get(character, 0) + 1

    def __check_containment(self, letters_contained: dict[str, int], all_letters: dict[str, int]) -> bool:
        for character, character_count in letters_contained.items():
            if character not in all_letters:
                return False
            if character_count > all_letters[character]:
                return False
        return True
