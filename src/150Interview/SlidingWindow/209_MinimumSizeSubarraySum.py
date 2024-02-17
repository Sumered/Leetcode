class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left_index, right_index, current_sum = 0, 0, 0
        best_answer = int(1e6)

        while right_index < len(nums):
            if current_sum >= target:
                current_sum -= nums[left_index]
                left_index += 1
            else:
                current_sum += nums[right_index]
                right_index += 1

            if current_sum >= target:
                best_answer = min(best_answer, right_index - left_index)

        best_answer = self.__finalize(target, nums, current_sum, left_index, right_index, best_answer)
        if best_answer == int(1e6):
            return 0
        return best_answer

    def __finalize(self, target: int, nums: list[int], current_sum: int, left_index: int, right_index: int, best_answer: int) -> int:
        while left_index < len(nums) and current_sum >= target:
            current_sum -= nums[left_index]
            left_index += 1

            if current_sum >= target:
                best_answer = min(best_answer, right_index - left_index)
            else:
                break

        return best_answer


algos = Solution()
print(algos.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
