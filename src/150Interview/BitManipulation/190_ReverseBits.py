class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result *= 2
            result += n % 2
            n //= 2
        return result
