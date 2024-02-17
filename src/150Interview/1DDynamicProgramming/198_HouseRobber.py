class Solution:
    def rob(self, numbers: list[int]) -> int:
        if len(numbers) <= 1:
            return numbers[0]

        maximum = max(numbers[1], numbers[0])

        current_maximum = numbers[1]
        previous_maximum = numbers[0]

        for number in numbers[2:]:
            maximum = max(previous_maximum + number, maximum)

            helper = current_maximum
            current_maximum = previous_maximum + number
            previous_maximum = max(helper, previous_maximum)

        return maximum
