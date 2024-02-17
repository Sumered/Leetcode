class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, s_length, t_index, t_length = 0, len(s), 0, len(t)
        while s_index < s_length and t_index < t_length:
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        return s_index == s_length
