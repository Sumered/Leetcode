class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts: dict[str, list[int]] = {}
        for index, character in enumerate(s):
            if character in counts:
                counts[character][1] += 1
            else:
                counts[character] = [index, 1]

        indexes = [value[0] for value in counts.values() if value[1] == 1]
        return min(indexes) if indexes else -1
