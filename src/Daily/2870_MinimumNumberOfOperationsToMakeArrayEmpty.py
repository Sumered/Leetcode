class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counts: dict[int, int] = {}
        for number in nums:
            if number not in counts:
                counts[number] = 0
            counts[number] += 1

        operations = 0

        for count in counts.values():
            if count < 2:
                return -1
            elif count == 2 or count == 4:
                operations += count // 2
            else:
                if count % 3 == 1:
                    operations += 2 + (count - 4) // 3
                elif count % 3 == 2:
                    operations += 1 + (count - 2) // 3
                else:
                    operations += count // 3

        return operations
