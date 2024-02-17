class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        needed_operations = 0
        actual_sign = 1
        binary_n = self.__transform_into_binary(n)
        for index in range(len(binary_n) - 1, 0, -1):
            if binary_n[index] == 1:
                needed_operations += actual_sign * ((2 ** (index + 1)) - 1)
                actual_sign *= -1

        return needed_operations + (actual_sign * binary_n[0])

    def __transform_into_binary(self, n: int) -> list[int]:
        result = []
        while n > 0:
            result.append(n % 2)
            n //= 2
        return result


algos = Solution()
for i in range(1, 31):
    print(algos.minimumOneBitOperations(i))


# Key observation here is that if you have any number then you need to remove first bit first. And after that you will always
# be left with 1 on the second bit. So essentially solution for 16 is how long it takes to zero the first bit and then how long it takes
# to solve 8. Also it can be seen that all lighten bits in your number only decreases the number of operations needed for first zeroing.
# After first zeroing you are always left with biggest power of 2 smaller than your starting number.
# To approach this kind of task, You need to see that this is kind of dynamic, but not really (it can be done via recurrence in n^2 via manually solving using proper algorithm)
# And to see pattern you need to start writing solutions for all n, one by one till you find this pattern (no easier way).
# 2 = 10 = 11 = 01 = 00 = 3
# 3 = 11 = 01 = 00 = 2
# 4 = 100 = 101 = 111 = 110 = 010 = 011 = 001 = 000 = 7
# 5 = 101 = 6
# 6 = 110 = 4
# 7 = 111 = 5
# 8 = 1000 = 1001 = 1011 = 1010 = 1110 = 1111 = 1101 = 1100 = 0100 = 15 16 - 1
# 9 = 1001 = 14 = 16 - 2
# 10 = 1010 = 12 = 16 - 4
# 11 = 1011 = 13 = 16 - 4 + 1
# 12 = 1100 = 8 = 16 - 8
# 13 = 1101 = 9 = 16 - 8 + 1
# 14 = 1110 = 11 = 16 - 8 + 3
# 15 = 1111 = 10 = 16 - 8 + 3 - 1
# 16 = 10000 = 10001 = 10011 = 10010 = 10110 = 10111 = 10101 = 10100 = 11100 = 11101 = 11111 = 11110 = 11010 = 11011 = 11001 = 11000 = 01000 = 31
# 17 = 10001 = 31 - 1 = 30
# 18 = 10010 = 31 - 3 = 28
# 19 = 10011 = 31 - 3 + 1 = 29
# 20 = 10100 = 31 - 7 = 24
# 21 = 10101 = 31 - 7 + 1 = 25
# 22 = 10110 = 31 - 7 + 3 = 27
# 23 = 10111 = 31 - 7 + 3 - 1 = 26
# 24 = 11000 = 31 - 15 = 16
# 25