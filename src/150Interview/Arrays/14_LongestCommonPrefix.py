class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        index = 0
        longest_prefix = ""

        while True:
            if index >= len(strs[0]):
                return longest_prefix
            for word_index in range(1, len(strs)):
                if index >= len(strs[word_index]) or strs[word_index][index] != strs[word_index - 1][index]:
                    return longest_prefix
            longest_prefix += strs[0][index]
            index += 1


algos = Solution()
print(algos.longestCommonPrefix(["ab", "a"]))
