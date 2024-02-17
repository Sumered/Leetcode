from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        maxes: deque[int] = deque()
        left, right = 0, 0
        output = []

        while right < len(nums):
            if right - left == k:
                output.append(maxes[0])
                if maxes[0] == nums[left]:
                    maxes.popleft()
                left += 1
            while len(maxes) != 0 and nums[right] > maxes[-1]:
                maxes.pop()

            maxes.append(nums[right])
            right += 1

        output.append(maxes[0])
        return output
