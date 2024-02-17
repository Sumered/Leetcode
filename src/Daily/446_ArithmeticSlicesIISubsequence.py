class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        dp: list[dict[int, int]] = [{} for _ in range(len(nums))]
        combinations = 0

        for index in range(len(nums)):
            for second_index in range(index):
                diff = nums[second_index] - nums[index]
                dp[index][diff] = dp[index].get(diff, 0) + dp[second_index].get(diff, 0) + 1

        for combos in dp:
            combinations += sum(combos.values())
        return combinations - (len(nums) * ((len(nums)) - 1)) // 2
