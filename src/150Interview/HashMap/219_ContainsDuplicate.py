class Solution:
    def containsNearbyDuplicate(self, numbers: list[int], k: int) -> bool:
        numbers_indexes: dict[int, int] = {}
        for index, number in enumerate(numbers):
            if number in numbers_indexes.keys():
                if index - numbers_indexes[number] <= k:
                    return True
            numbers_indexes[number] = index
        return False
