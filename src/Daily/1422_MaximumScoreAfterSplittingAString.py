class Solution:
    def maxScore(self, s: str) -> int:
        score, left_zeros, right_ones = 0, 0, s.count("1")

        for character in s[:-1]:
            if character == "0":
                left_zeros += 1
            else:
                right_ones -= 1

            score = max(score, left_zeros + right_ones)

        return score
