class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        maximal_number = max(nums)
        all_subarrays = (len(nums) ** 2 + len(nums)) // 2

        max_count = 0
        left, right = 0, 0

        while right < len(nums):
            if nums[right] == maximal_number:
                max_count += 1

            while max_count == k:
                if nums[left] == maximal_number:
                    max_count -= 1
                left += 1

            all_subarrays -= 1 + (right - left)
            right += 1

        return all_subarrays
