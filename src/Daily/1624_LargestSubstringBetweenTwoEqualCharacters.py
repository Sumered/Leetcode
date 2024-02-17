class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longest = -1

        for index in range(len(s)):
            end_index = s[index + 1 :].rfind(s[index])
            if end_index != -1 and end_index > longest:
                longest = end_index

        return longest
