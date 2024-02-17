from collections import defaultdict


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counts: defaultdict = defaultdict(int)
        for number in arr:
            counts[number] += 1

        result = len(counts)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1])

        for number, count in sorted_counts:
            if k >= count:
                result -= 1
                k -= count
            else:
                break

        return result
