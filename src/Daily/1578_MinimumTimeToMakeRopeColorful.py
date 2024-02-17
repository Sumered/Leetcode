class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        left_index, right_index = 0, 1
        total_cost = 0

        while right_index < len(colors):
            if colors[left_index] != colors[right_index]:
                total_cost += sum(neededTime[left_index:right_index]) - max(neededTime[left_index:right_index])
                left_index = right_index
            right_index += 1

        total_cost += sum(neededTime[left_index:right_index]) - max(neededTime[left_index:right_index])

        return total_cost
