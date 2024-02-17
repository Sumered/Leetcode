class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        threshold = len(arr) / 4
        current_number, current_count = arr[0], 0

        for number in arr:
            if number == current_number:
                current_count += 1
                if current_count > threshold:
                    return current_number
            else:
                current_count = 1
            current_number = number

        return arr[0]
