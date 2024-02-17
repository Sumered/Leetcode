class Solution:
    def getSumAbsoluteDifferences(self, numbers: list[int]) -> list[int]:
        result = []
        previous_number = numbers[0]
        left_count, right_count = 0, len(numbers)
        left_difference, right_difference = 0, sum(numbers) - right_count * previous_number
        for number in numbers:
            left_difference += (number - previous_number) * left_count
            right_difference -= (number - previous_number) * right_count
            result.append(left_difference + right_difference)
            previous_number = number
            left_count += 1
            right_count -= 1

        return result


algos = Solution()
print(algos.getSumAbsoluteDifferences([2, 3, 5]))
