class Solution:
    def partition(self, s: str) -> list[list[str]]:
        partitions: list[list[str]] = []

        self.__palindrome_partition(s, 0, [], partitions)

        return partitions

    def __palindrome_partition(self, s: str, start_index: int, current_partition: list[str], partitions: list[list[str]]) -> None:
        if start_index == len(s):
            partitions.append(current_partition.copy())
            return

        for index in range(start_index + 1, len(s) + 1):
            if self.__is_palindrome(s[start_index:index]):
                current_partition.append(s[start_index:index])
                self.__palindrome_partition(s, index, current_partition, partitions)
                current_partition.pop()

    def __is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
