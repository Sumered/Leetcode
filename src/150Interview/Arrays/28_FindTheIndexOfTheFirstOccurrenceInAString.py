class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


algos = Solution()
print(algos.strStr("mississippi", "issip"))
