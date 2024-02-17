class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        stations_count = len(gas)
        travel_cost = 0
        last_positive_index = int(1e6)
        negative_costs_till_now = 0

        for index in range(stations_count):
            travel_cost += gas[index] - cost[index]

            if travel_cost < 0:
                negative_costs_till_now += travel_cost
                travel_cost = 0
                last_positive_index = int(1e6)
            else:
                last_positive_index = min(last_positive_index, index)

        if last_positive_index == int(1e6):
            return -1

        if negative_costs_till_now + travel_cost < 0:
            return -1

        return last_positive_index


algos = Solution()
print(algos.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
