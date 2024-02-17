class Solution:
    def reductionOperations(self, numbers: list[int]) -> int:
        numbers.sort()
        numbers.reverse()

        answer = 0
        for index in range(len(numbers) - 1):
            if numbers[index] > numbers[index + 1]:
                answer += index + 1  # there is lower one next, so we need to convert all previous ones

        return answer

    def reductionOperations_counting(self, numbers: list[int]) -> int:
        # Due to limits on numbers[i] being small, we can do it in O(n)
        number_value_limit = int(1e5) + 1
        occurrences = [0 for _ in range(number_value_limit)]

        for number in numbers:
            occurrences[number] += 1

        answer, cumulative_operations = 0, 0

        for index in range(number_value_limit - 1, 0, -1):
            if occurrences[index] > 0:
                cumulative_operations += occurrences[index]
                answer += cumulative_operations - occurrences[index]

        return answer

    def reductionOperations_nlogn(self, numbers: list[int]) -> int:
        numbers_count: dict[int, int] = {}

        for number in numbers:
            numbers_count[number] = numbers_count.get(number, 0) + 1

        counts = sorted(list(numbers_count.items()))

        answer = 0

        for index, (_, count) in enumerate(counts[1:]):
            answer += (index + 1) * count

        return answer
