class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [[0, 0] for _ in range(len(s))]
        combo_digits = ["1", "2"]
        no_combo_digits = ["0", "3", "4", "5", "6", "7", "8", "9"]
        off_limit_digits = ["7", "8", "9"]

        dp[0][0] = 1

        for index, char in enumerate(s[1:]):
            previous_char = s[index]
            if char == "0":
                if previous_char in combo_digits:
                    dp[index + 1][0] = 0
                    dp[index + 1][1] = dp[index][0]
                else:
                    return 0
                continue
            if previous_char in combo_digits:
                if previous_char == "2" and char in off_limit_digits:
                    dp[index + 1][0] = dp[index][0] + dp[index][1]
                else:
                    dp[index + 1][0] = dp[index][0] + dp[index][1]
                    dp[index + 1][1] = dp[index][0]
            elif previous_char in no_combo_digits:
                dp[index + 1][0] = dp[index][0] + dp[index][1]

        return dp[len(s) - 1][0] + dp[len(s) - 1][1]


# 777 -> 1
# 222 -> 2|2|2, 22|2, 2|22 -> 2, 1
# 2222 -> 2|2|2|2, 22|2|2, 22|22, 2|2|22, 2|22|2 -> 3 + 2
# 2227 -> 2|2|2|7, 22|2|7, 22|27, 2|2|27, 2|22|7 -> 3 + 2
# 2277 -> 2|2|7|7, 22|7|7, 2|27|7 -> 3 0
# 227 -> 2|2|7, 22|7, 2|27 -> 2 1
# 22 -> 2|2, 22 -> 1, 1
# 20 -> 20 -> 0, 1
# 2220 -> 2|2|20, 22|20 -> 0, 2

print(Solution().numDecodings("227"))
