from collections import defaultdict


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_dict: dict[str, int] = defaultdict(int)
        for char in chars:
            char_dict[char] += 1

        result = 0
        for word in words:
            char_dict_copy = char_dict.copy()
            all_in = True
            for character in word:
                char_dict_copy[character] -= 1
                if char_dict_copy[character] < 0:
                    all_in = False
                    break
            if all_in:
                result += len(word)

        return result
