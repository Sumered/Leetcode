class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.__to_binary(self.__to_decimal(a) + self.__to_decimal(b))

    def __to_decimal(self, a: str) -> int:
        n = 0
        for bit in a:
            n *= 2
            n += int(bit) % 2
        return n

    def __to_binary(self, n: int) -> str:
        binary = ""
        while n > 0:
            binary += str(n % 2)
            n //= 2
        return binary[::-1]


algos = Solution()
print(algos.addBinary("11", "1"))
