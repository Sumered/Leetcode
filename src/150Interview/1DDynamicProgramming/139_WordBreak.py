class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for index in range(len(s)):
            for word in wordDict:
                if dp[index] == True and s[index : index + len(word)] == word:
                    dp[index + len(word)] = True

        return dp[len(s)]


print(Solution().wordBreak("leetcode", ["leet", "code"]))
