class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int, int] = {}
        for number in nums:
            counts[number] = counts.get(number, 0) + 1

        frequencies: list[list[int]] = [[] for _ in range(len(nums) + 1)]
        for number, frequency in counts.items():
            frequencies[frequency].append(number)

        result, top_k = [], 0
        for index in range(len(nums), -1, -1):
            for element in frequencies[index]:
                result.append(element)
                top_k += 1
                if top_k == k:
                    return result
        return result
