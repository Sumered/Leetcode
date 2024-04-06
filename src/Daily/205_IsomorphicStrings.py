class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = self.__create_string_dict(s)
        t_dict = self.__create_string_dict(t)
        mapping: dict[str, str] = {}

        for character, count in s_dict.items():
            found, character_in_t = self.__get_key_for_value(t_dict, count)
            if not found:
                return False
            t_dict[character_in_t] = 0
            mapping[character_in_t] = character

        mapped_t = list(map(lambda c: mapping[c], t))
        return all(mapped_t[index] == s[index] for index in range(len(s)))

    def __get_key_for_value(self, chars_count: dict[str, int], count_to_find: int) -> tuple[bool, str]:
        for character, count in chars_count.items():
            if count == count_to_find:
                return True, character
        return False, ""

    def __create_string_dict(self, word: str) -> dict[str, int]:
        word_dict: dict[str, int] = {}
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
        return word_dict
