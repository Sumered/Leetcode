from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts: defaultdict = defaultdict(int)
        s2_counts: defaultdict = defaultdict(int)

        for character in s1:
            s1_counts[character] += 1

        left, right = 0, 0
        while right < len(s2):
            s2_counts[s2[right]] += 1

            if right - left + 1 == len(s1):
                if self.__counts_equal(s1_counts, s2_counts):
                    return True
                s2_counts[s2[left]] -= 1
                left += 1

            right += 1

        return False

    def __counts_equal(self, s1_counts: dict[str, int], s2_counts: dict[str, int]) -> bool:
        for letter, count in s1_counts.items():
            if letter not in s2_counts:
                return False
            if count != s2_counts[letter]:
                return False
        return True
