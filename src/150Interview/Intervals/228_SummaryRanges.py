class Solution:
    def summaryRanges(self, numbers: list[int]) -> list[str]:
        answer: list[str] = []
        if len(numbers) == 0:
            return answer
        left_index, right_index = 0, 1
        numbers.append(numbers[len(numbers) - 1] + 2)
        while right_index != len(numbers):
            if numbers[right_index] - numbers[left_index] != right_index - left_index:
                if right_index - left_index - 1 == 0:
                    answer.append(f"{numbers[left_index]}")
                else:
                    answer.append(f"{numbers[left_index]}->{numbers[right_index - 1]}")
                left_index = right_index
            right_index += 1
        return answer
