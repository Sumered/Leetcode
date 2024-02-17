class Solution:
    def countNicePairs(self, numbers: list[int]) -> int:
        numbers_reversed, sums_count = self.__parse_numbers(numbers)
        nice_pairs_count = 0
        modulo = int(1e9) + 7

        for index, number in enumerate(numbers):
            number_reversed = numbers_reversed[index]
            nice_pairs_count = (nice_pairs_count + sums_count[number - number_reversed] - 1) % modulo
            sums_count[number - number_reversed] -= 1

        return nice_pairs_count

    def __parse_numbers(self, numbers: list[int]) -> tuple[list[int], dict[int, int]]:
        numbers_reversed = [0 for _ in numbers]
        sums_count: dict[int, int] = {}
        for index, number in enumerate(numbers):
            reversed_number = self.__reverse_number(number)
            numbers_reversed[index] = reversed_number
            sums_count[number - reversed_number] = sums_count.get(number - reversed_number, 0) + 1
        return numbers_reversed, sums_count

    def __reverse_number(self, number: int) -> int:
        reversed_number = 0
        while number > 0:
            reversed_number *= 10
            reversed_number += number % 10
            number = number // 10
        return reversed_number


algos = Solution()
print(algos.countNicePairs([1, 1, 1, 1, 1]))
