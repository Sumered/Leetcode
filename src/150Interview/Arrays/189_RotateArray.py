class Solution:
    def rotate(self, numbers: list[int], k: int) -> None:
        k = k % len(numbers)
        self.__rotate_array(numbers, 0, len(numbers) - 1)
        self.__rotate_array(numbers, 0, k - 1)
        self.__rotate_array(numbers, k, len(numbers) - 1)

    def __rotate_array(self, numbers: list[int], left_index: int, right_index: int) -> None:
        while left_index < right_index:
            helper = numbers[left_index]
            numbers[left_index] = numbers[right_index]
            numbers[right_index] = helper
            left_index += 1
            right_index -= 1

    def rotate_pythonic(self, numbers: list[int], k: int) -> None:
        """
        Uses extra O(n) space but nice and clean
        """
        break_point = (len(numbers) - k) % len(numbers)
        numbers[:] = numbers[break_point:] + numbers[:break_point]
