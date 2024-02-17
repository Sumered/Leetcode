class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        answer = []

        for index in range(0, len(nums), 3):
            if nums[index] + k < nums[index + 2]:
                return []
            answer.append([nums[index], nums[index + 1], nums[index + 2]])

        return answer
