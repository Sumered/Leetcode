class Solution:
    def trap(self, heights: list[int]) -> int:
        left_maxes = [0 for _ in heights]
        right_maxes = [0 for _ in heights]
        result, current_maximum = 0, 0

        for index, height in enumerate(heights):
            current_maximum = max(current_maximum, height)
            left_maxes[index] = current_maximum

        current_maximum = 0
        for index in range(len(heights) - 1, -1, -1):
            current_maximum = max(current_maximum, heights[index])
            right_maxes[index] = current_maximum

        for index, height in enumerate(heights):
            result += max(0, min(left_maxes[index], right_maxes[index]) - height)

        return result


algos = Solution()
print(algos.trap([9, 6, 8, 8, 5, 6, 3]))
