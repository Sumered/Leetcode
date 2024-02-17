class Solution:
    def majorityElement(self, numbers: list[int]) -> int:
        left_index = 0
        right_index = len(numbers) - 1
        count_of_duplicates = 0

        while left_index < right_index:
            if numbers[left_index] == numbers[right_index]:
                numbers[right_index] = 0
                right_index -= 1
                count_of_duplicates += 1
            else:
                if count_of_duplicates > 0:
                    numbers[right_index] = 0
                    right_index -= 1
                    count_of_duplicates -= 1
                else:
                    numbers[left_index] = 0
                    numbers[right_index] = 0
                    left_index += 1
                    right_index -= 1

        for number in numbers:
            if number != 0:
                return number

        return 0
