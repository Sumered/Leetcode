class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        job_data = sorted(zip(endTime, startTime, profit))
        number_of_jobs = len(profit)
        dp = [0 for _ in range(number_of_jobs + 1)]

        for index, (end, start, value) in enumerate(job_data):
            previous_index = self.__bin_search(job_data[:index], start)
            dp[index + 1] = max(dp[index], dp[previous_index] + value)

        return dp[number_of_jobs]

    def __bin_search(self, job_data: list[tuple[int, int, int]], start: int) -> int:
        left, right = 0, len(job_data)

        while left < right:
            medium = (left + right) // 2
            if job_data[medium][0] <= start:
                left = medium + 1
            else:
                right = medium
        return left


print(Solution().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]))
