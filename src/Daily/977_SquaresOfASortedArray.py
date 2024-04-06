class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        output: list[int] = []

        while left <= right:
            left_square, right_square = nums[left] * nums[left], nums[right] * nums[right]
            if left_square >= right_square:
                output.append(left_square)
                left += 1
            else:
                output.append(right_square)
                right -= 1

        output.reverse()
        return output
