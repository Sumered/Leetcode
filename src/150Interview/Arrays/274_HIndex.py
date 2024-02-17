class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        maximal_h_index = 0
        all_papers_count = len(citations)

        for index, citations_count in enumerate(citations):
            if citations_count <= all_papers_count - index:
                maximal_h_index = max(citations_count, maximal_h_index)
            else:
                remaining_papers_count = all_papers_count - index
                maximal_h_index = max(maximal_h_index, remaining_papers_count)
        return maximal_h_index


algos = Solution()
print(algos.hIndex([3, 0, 6, 1, 5]))
