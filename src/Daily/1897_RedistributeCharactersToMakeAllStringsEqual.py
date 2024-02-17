class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        letters_count = {}

        for word in words:
            for char in word:
                if char not in letters_count:
                    letters_count[char] = 1
                else:
                    letters_count[char] += 1

        for key, value in letters_count.items():
            if value % len(words) != 0:
                return False
        return True
