class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        best_score, current_score = 0, 0
        while left <= right:
            if power < tokens[left]:
                if current_score >= 1:
                    power += tokens[right]
                    current_score -= 1
                    right -= 1
                else:
                    return best_score
            else:
                power -= tokens[left]
                current_score += 1
                best_score = max(best_score, current_score)
                left += 1
        return best_score
