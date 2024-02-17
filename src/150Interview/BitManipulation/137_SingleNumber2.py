class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bits = [0 for _ in range(33)]

        for number in nums:
            self.__to_bits(number, bits)

        result = 0
        bits.reverse()
        for bit in bits[:-1]:
            result *= 2
            if bit % 3 == 1:
                result += 1
        if bits[-1] % 3 == 1:
            return result
        return -result

    def __to_bits(self, number: int, bits: list[int]) -> None:
        bits[0] += 1 if number > 0 else 0
        number = abs(number)
        index = 1
        while number > 0:
            bits[index] += number % 2
            number = number // 2
            index += 1
