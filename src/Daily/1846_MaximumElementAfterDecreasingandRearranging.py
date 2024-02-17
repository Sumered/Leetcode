class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        current_maximum = 1

        duplicates_count = 0
        current_value = arr[0]
        previous_value = 1

        for number in arr[1:]:
            if number == current_value:
                duplicates_count += 1

            if number != current_value:
                current_maximum += min(duplicates_count, current_value - previous_value)
                duplicates_count = 1
                previous_value = current_value
                current_value = number

        current_maximum += min(duplicates_count, current_value - previous_value)
        return current_maximum


algos = Solution()
print(algos.maximumElementAfterDecrementingAndRearranging([1, 2, 3]))
