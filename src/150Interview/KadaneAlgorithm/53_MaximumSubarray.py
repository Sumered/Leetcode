from dataclasses import dataclass


@dataclass
class NodeResult:
    left_max: int
    right_max: int
    best_result: int
    elements_sum: int

    @staticmethod
    def create(left_node: "NodeResult", right_node: "NodeResult") -> "NodeResult":
        left_max = max(left_node.left_max, left_node.elements_sum + right_node.left_max)
        right_max = max(right_node.right_max, right_node.elements_sum + left_node.right_max)
        best_result = max(left_node.best_result, right_node.best_result, left_node.right_max + right_node.left_max)
        elements_sum = left_node.elements_sum + right_node.elements_sum

        return NodeResult(left_max, right_max, best_result, elements_sum)


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        left_index, right_index = 0, len(numbers) - 1

        return self.__divide_and_conquer(numbers, left_index, right_index).best_result

    def __divide_and_conquer(self, numbers: list[int], left_index: int, right_index: int) -> NodeResult:
        if right_index - left_index == 0:
            resulting_value = numbers[left_index]
            return NodeResult(resulting_value, resulting_value, resulting_value, resulting_value)

        middle_point = (left_index + right_index) // 2

        left_result = self.__divide_and_conquer(numbers, left_index, middle_point)
        right_result = self.__divide_and_conquer(numbers, middle_point + 1, right_index)

        return NodeResult.create(left_result, right_result)

    def maxSubArray_kadane(self, numbers: list[int]) -> int:
        maximal_sum, current_sum = -10001, -10001

        for number in numbers:
            current_sum = max(current_sum + number, number)
            maximal_sum = max(maximal_sum, current_sum)

        return maximal_sum


algos = Solution()
print(algos.maxSubArray([1]))
