class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        counts: dict[int, int] = {}

        left, right = 0, 0
        result = 0

        while right < len(nums):
            number = nums[right]
            counts[number] = counts.get(number, 0) + 1

            while left <= right and counts[number] > k:
                counts[nums[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
            right += 1

        return result
