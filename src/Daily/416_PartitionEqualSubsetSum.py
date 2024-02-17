class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        required_change = self.__sanity_checks(nums)
        if required_change == -1:
            return False

        dp = [False for _ in range(required_change + 1)]
        for number in nums:
            for index in range(len(dp) - 1, -1, -1):
                if dp[index] and index + number <= required_change:
                    dp[index + number] = True
            dp[number] = True
            if dp[required_change]:
                return True
        return False

    def __sanity_checks(self, nums: list[int]) -> int:
        summed = sum(nums)
        if summed % 2 == 1:
            return -1

        required_change = summed // 2

        if max(nums) > required_change:
            return -1

        return required_change
