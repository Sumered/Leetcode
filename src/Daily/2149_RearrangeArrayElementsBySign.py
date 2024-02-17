class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = []
        minus_pointer, plus_pointer = 0, 0
        append_plus = True
        while minus_pointer < len(nums) or plus_pointer < len(nums):
            if plus_pointer < len(nums) and nums[plus_pointer] > 0:
                if append_plus:
                    result.append(nums[plus_pointer])
                    plus_pointer += 1
                    append_plus = False
            else:
                plus_pointer += 1

            if minus_pointer < len(nums) and nums[minus_pointer] < 0:
                if not append_plus:
                    result.append(nums[minus_pointer])
                    minus_pointer += 1
                    append_plus = True
            else:
                minus_pointer += 1
        return result
