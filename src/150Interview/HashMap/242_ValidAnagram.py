class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = self.__create_string_dict(s)
        t_dict = self.__create_string_dict(t)

        for character, count in s_dict.items():
            if character not in t_dict or t_dict[character] != count:
                return False

        return True

    def __create_string_dict(self, word: str) -> dict[str, int]:
        word_dict: dict[str, int] = {}
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1
        return word_dict
