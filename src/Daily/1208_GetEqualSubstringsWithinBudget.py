class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right = 0, 0
        max_substring_length, current_cost = 0, 0

        while right < len(t):
            if s[right] != t[right]:
                cost = abs(ord(t[right]) - ord(s[right]))

                while current_cost + cost > maxCost:
                    current_cost -= abs(ord(t[left]) - ord(s[left]))
                    left += 1

                current_cost += cost

            max_substring_length = max(max_substring_length, right - left + 1)
            right += 1

        return max_substring_length
