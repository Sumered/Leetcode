from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams: dict[str, list[str]] = defaultdict(list)

        for word in strs:
            word_letters = "".join(sorted(word))
            anagrams[word_letters].append(word)

        return list(anagrams.values())
