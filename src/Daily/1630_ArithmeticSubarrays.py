class Solution:
    def checkArithmeticSubarrays(self, numbers: list[int], l: list[int], r: list[int]) -> list[bool]:
        answer = []

        for start, end in zip(l, r):
            answer.append(self.__check_subarray(numbers[start : end + 1]))
        return answer

    def __check_subarray(self, subarray: list[int]) -> bool:
        min_value = min(subarray)
        max_value = max(subarray)
        increment = (max_value - min_value) // (len(subarray) - 1)

        if (max_value - min_value) % (len(subarray) - 1) != 0:
            return False

        if increment == 0:
            return True

        visited = set()
        correct = True
        for number in subarray:
            diff = number - min_value
            if diff % increment != 0 or diff // increment in visited:
                correct = False
                break
            visited.add(diff // increment)
        return correct


algos = Solution()
print(algos.checkArithmeticSubarrays([-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10], [0, 1, 6, 4, 8, 7], [4, 4, 9, 7, 9, 10]))
