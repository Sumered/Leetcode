class Solution:
    def maxArea(self, height: list[int]) -> int:
        result, left_index, right_index = 0, 0, len(height) - 1

        while left_index < right_index:
            result = max(result, min(height[left_index], height[right_index]) * (right_index - left_index))
            if height[left_index] < height[right_index]:
                left_index += 1
            elif height[left_index] == height[right_index]:
                left_index += 1
                right_index -= 1
            else:
                right_index -= 1
        return result
