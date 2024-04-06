class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        splits = []
        left, right = 0, 0
        current_product = 1

        while right < len(nums):
            if current_product * nums[right] < k:
                current_product *= nums[right]
            else:
                splits.append((left, right))
                current_product *= nums[right]

                while left <= right and current_product >= k:
                    current_product //= nums[left]
                    left += 1
            right += 1

        if current_product < k:
            splits.append((left, right))

        result = self.__count_subarrays(splits)
        return result

    def __count_subarrays(self, splits: list[tuple[int, int]]) -> int:
        result = 0
        previous_split = (0, 0)

        for left, right in splits:
            result += self.__count_subarray(left, right)
            common_part = (max(left, previous_split[0]), min(right, previous_split[1]))
            result -= self.__count_subarray(common_part[0], common_part[1])
            previous_split = (left, right)

        return result

    def __count_subarray(self, left: int, right: int) -> int:
        length = right - left

        return ((length**2) + length) // 2 if length > 0 else 0
