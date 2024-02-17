class Solution:
    def removeDuplicates(self, numbers: list[int]) -> int:
        current_index = 0
        current_number = -101
        unique_elements_count = 0

        for index, number in enumerate(numbers):
            if number != current_number:
                numbers[current_index] = number
                current_index += 1
                current_number = number
                unique_elements_count += 1

        return unique_elements_count
