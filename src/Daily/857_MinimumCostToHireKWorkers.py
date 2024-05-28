import heapq


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers_count = len(quality)
        quality_heap = []
        wage_to_quality = [(worker_wage / worker_quality, worker_quality) for worker_wage, worker_quality in zip(wage, quality)]
        wage_to_quality.sort()

        current_qualities_sum = 0

        for index in range(k):
            current_qualities_sum += wage_to_quality[index][1]
            heapq.heappush(quality_heap, -wage_to_quality[index][1])

        result = current_qualities_sum * wage_to_quality[k - 1][0]

        for index in range(k, workers_count):
            current_qualities_sum += heapq.heappop(quality_heap)
            current_qualities_sum += wage_to_quality[index][1]
            heapq.heappush(quality_heap, -wage_to_quality[index][1])
            result = min(result, current_qualities_sum * wage_to_quality[index][0])

        return result
