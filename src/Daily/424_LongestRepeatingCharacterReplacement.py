from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: defaultdict = defaultdict(int)
        left, right, current_max, best = 0, 0, 0, 0

        while right < len(s):
            counts[s[right]] += 1
            current_max = max(counts[s[right]], current_max)

            while right - left + 1 - current_max > k:
                counts[s[left]] -= 1
                left += 1
                current_max = max(counts.values())

            best = max(best, right - left)
            right += 1

        return best
