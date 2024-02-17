class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left_index, right_index = 0, len(numbers) - 1
        while left_index <= right_index:
            numbers_sum = numbers[left_index] + numbers[right_index]
            if numbers_sum < target:
                left_index += 1
            elif numbers_sum == target:
                return [left_index + 1, right_index + 1]
            else:
                right_index -= 1
        return []

    def constant_dict_twoSum(self, numbers: list[int], target: int) -> list[int]:
        # This solution also uses constant extra space -> target is bounded from -1000 to 1000 so maxsize of dict is 2000.
        # It could also be an array.
        # But I guess that it is not what was meant by constant extra space.
        found_diffs: dict[int, int] = {}

        for index, number in enumerate(numbers):
            if number in found_diffs:
                return [found_diffs[number], index + 1]
            found_diffs[target - number] = index + 1
        return []
