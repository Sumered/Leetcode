class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = int(1e9) + 7
        dp = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for number_len in range(n + 1)]
        dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for number_len in range(2, n + 1):
            dp[number_len][0] = (dp[number_len - 1][4] + dp[number_len - 1][6]) % modulo
            dp[number_len][1] = (dp[number_len - 1][6] + dp[number_len - 1][8]) % modulo
            dp[number_len][2] = (dp[number_len - 1][7] + dp[number_len - 1][9]) % modulo
            dp[number_len][3] = (dp[number_len - 1][4] + dp[number_len - 1][8]) % modulo
            dp[number_len][4] = ((dp[number_len - 1][3] + dp[number_len - 1][9]) % modulo + dp[number_len - 1][0]) % modulo
            dp[number_len][6] = ((dp[number_len - 1][1] + dp[number_len - 1][7]) % modulo + dp[number_len - 1][0]) % modulo
            dp[number_len][7] = (dp[number_len - 1][2] + dp[number_len - 1][6]) % modulo
            dp[number_len][8] = (dp[number_len - 1][1] + dp[number_len - 1][3]) % modulo
            dp[number_len][9] = (dp[number_len - 1][2] + dp[number_len - 1][4]) % modulo

        result = 0
        for i in range(10):
            result = (result + dp[n][i]) % modulo

        return result
