class Solution:
    def maxFrequency(self, numbers: list[int], k: int) -> int:
        numbers.sort()
        maximum_frequency = 0
        previous_value = numbers[0]
        left_index, right_index, current_sum = 0, 0, 0

        for number in numbers:
            if number != previous_value:
                current_sum += self.__calculate_update(left_index, right_index, number - previous_value)
                left_index, current_sum = self.__move_left_index_till_lower(numbers, left_index, number, current_sum, k)
                previous_value = number

            right_index += 1
            maximum_frequency = max(maximum_frequency, right_index - left_index)

        return maximum_frequency

    def __calculate_update(self, left_index: int, right_index: int, value_difference: int) -> int:
        return (right_index - left_index) * value_difference

    def __move_left_index_till_lower(
        self, numbers: list[int], left_index: int, number: int, current_sum: int, threshold: int
    ) -> tuple[int, int]:
        while current_sum > threshold:
            current_sum -= number - numbers[left_index]
            left_index += 1

        return left_index, current_sum


algos = Solution()
print(algos.maxFrequency([3, 9, 6], 2))
