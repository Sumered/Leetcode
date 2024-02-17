class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts: dict[int, int] = {}
        for number in arr:
            counts[number] = counts.get(number, 0) + 1

        unique = set()
        for value in counts.values():
            if value in unique:
                return False
            unique.add(value)

        return True
