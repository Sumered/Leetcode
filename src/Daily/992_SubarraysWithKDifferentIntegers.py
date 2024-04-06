class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.__count_less_than_k(nums, k) - self.__count_less_than_k(nums, k - 1)

    def __count_less_than_k(self, nums: list[int], k: int) -> int:
        counts: dict[int, int] = {}
        left, right = 0, 0
        result = 0

        while right < len(nums):
            number = nums[right]
            counts[number] = counts.get(number, 0) + 1

            while len(counts) > k:
                counts[nums[left]] -= 1

                if counts[nums[left]] == 0:
                    del counts[nums[left]]

                left += 1

            if len(counts) <= k:
                result += (right - left) + 1

            right += 1

        return result
