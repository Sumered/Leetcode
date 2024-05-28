from functools import reduce


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        array_xor = reduce(lambda a, b: a ^ b, nums)

        return int.bit_count(k ^ array_xor)

Solution().minOperations([4], 7)
