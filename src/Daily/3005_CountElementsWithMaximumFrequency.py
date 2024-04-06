class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts, max_frequency = self.__count_elements(nums)
        number_count = 0

        for count in counts.values():
            if count == max_frequency:
                number_count += count

        return number_count

    def __count_elements(self, nums: list[int]) -> tuple[dict[int, int], int]:
        counts: dict[int, int] = {}
        max_frequency = 0

        for number in nums:
            counts[number] = counts.get(number, 0) + 1
            max_frequency = max(max_frequency, counts[number])

        return counts, max_frequency
