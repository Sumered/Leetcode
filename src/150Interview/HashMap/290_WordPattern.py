class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False

        letter_mapping: dict[str, str] = {}
        reverted_mapping: dict[str, str] = {}

        for index in range(len(pattern)):
            if pattern[index] in letter_mapping:
                if letter_mapping[pattern[index]] != words[index]:
                    return False
            else:
                if words[index] in letter_mapping.values():
                    return False
                letter_mapping[pattern[index]] = words[index]

        return True


algos = Solution()
algos.wordPattern("abba", "dog dog dog dog")
