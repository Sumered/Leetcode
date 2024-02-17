class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        answer = [nums[0]]
        for index in range(1, len(nums)):
            if nums[index] > answer[len(answer) - 1]:
                answer.append(nums[index])
            else:
                left, right = 0, len(answer)
                while left < right:
                    medium = (left + right) // 2
                    if answer[medium] > nums[index]:
                        right = medium
                    else:
                        left = medium + 1
                answer[left] = min(nums[index], answer[left])

        return len(answer)

    def square_lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in nums]

        for index in range(len(nums)):
            for second_index in range(index + 1, len(nums)):
                if nums[second_index] > nums[index]:
                    dp[second_index] = max(dp[second_index], dp[index] + 1)

        return max(dp)


print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
