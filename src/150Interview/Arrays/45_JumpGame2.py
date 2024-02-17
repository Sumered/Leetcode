class Solution:
    def jump_linear(self, numbers: list[int]) -> int:
        answer = 0
        farthest_now = 0
        farthest_future = 0

        for index in range(len(numbers) - 1):
            farthest_future = min(len(numbers), max(farthest_future, index + numbers[index]))

            if index == farthest_now:
                answer += 1
                farthest_now = farthest_future

        return answer

    def jump_nlogn(self, numbers: list[int]) -> int:
        if len(numbers) == 1:
            return 0

        numbers_length = len(numbers)
        minimal_tree = MinTree(numbers_length)
        minimal_tree.update(0, minimal_tree.offset_index(numbers_length - 1))

        for index, number in reversed(list(enumerate(numbers[: numbers_length - 1]))):
            minimal_jumps = (
                minimal_tree.get_value(1, 0, minimal_tree.lowest_size // 2 - 1, index, min(index + number, numbers_length - 1)) + 1
            )
            minimal_tree.update(minimal_jumps, minimal_tree.offset_index(index))
        return minimal_tree.tree[minimal_tree.offset_index(0)]

    def jump_brute(self, numbers: list[int]) -> int:
        minimal_jumps_required = [10001 for _ in numbers]
        minimal_jumps_required[0] = 0

        for index, number in enumerate(numbers):
            for jump_length in range(number):
                further_index = index + jump_length + 1
                if further_index >= len(numbers):
                    break
                minimal_jumps_required[further_index] = min(minimal_jumps_required[further_index], minimal_jumps_required[index] + 1)

        return minimal_jumps_required[len(numbers) - 1]


class MinTree:
    def __init__(self, size: int):
        self.lowest_size = self.__get_lowest_power(size)
        self.tree = [10001 for _ in range(self.lowest_size)]

    def __get_lowest_power(self, size: int) -> int:
        power = 1
        while power < size:
            power *= 2
        return power * 2

    def offset_index(self, index: int) -> int:
        return (self.lowest_size // 2) + index

    def update(self, value: int, index: int) -> None:
        if index == 0:
            return
        self.tree[index] = min(value, self.tree[index])
        self.update(self.tree[index], index // 2)

    def get_value(self, current_index: int, left_end: int, right_end: int, left_index: int, right_index: int) -> int:
        if left_index == left_end and right_index == right_end:
            return self.tree[current_index]
        middle_point = (left_end + right_end) // 2

        if left_index <= middle_point and right_index <= middle_point:
            return self.get_value(current_index * 2, left_end, middle_point, left_index, right_index)

        if left_index <= middle_point and right_index > middle_point:
            left_min = self.get_value(current_index * 2, left_end, middle_point, left_index, middle_point)
            right_min = self.get_value(current_index * 2 + 1, middle_point + 1, right_end, middle_point + 1, right_index)
            return min(left_min, right_min)

        return self.get_value(current_index * 2 + 1, middle_point + 1, right_end, left_index, right_index)
