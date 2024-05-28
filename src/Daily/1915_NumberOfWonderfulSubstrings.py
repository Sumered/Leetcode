from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        start, end = ord("a"), ord("j")
        self.__count = end - start
        self.__bits = {chr(index): 2 ** (index - start) for index in range(start, end + 1)}

    def wonderfulSubstrings(self, word: str) -> int:
        prefixes: defaultdict[int, int] = defaultdict(int, {0: 1})

        result = 0
        current_bit_mask = 0

        for index, letter in enumerate(word):
            current_bit_mask = current_bit_mask ^ self.__bits[letter]
            result += self.__count_matching(prefixes, current_bit_mask)
            result += prefixes[current_bit_mask]
            prefixes[current_bit_mask] = prefixes.get(current_bit_mask, 0) + 1

        return result

    def __count_matching(self, prefixes: dict[int, int], current_bit_mask: int) -> int:
        result = 0

        for offset in range(self.__count + 1):
            matching_mask = current_bit_mask ^ (1 << offset)
            if matching_mask in prefixes:
                result += prefixes[matching_mask]

        return result
