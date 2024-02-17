class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        visited = [False for _ in range(len(nums))]
        result, current_row, used_numbers = [], set(), 0

        while used_numbers != len(nums):
            for index in range(len(nums)):
                if not visited[index] and nums[index] not in current_row:
                    visited[index] = True
                    current_row.add(nums[index])
                    used_numbers += 1

            result.append(list(current_row))
            current_row = set()

        return result
