from heapq import heappop, heappush


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        costs = [[int(1e9) for _ in range(k + 2)] for _ in range(n)]
        graph = self.__load_graph(flights, n)
        order: list[tuple[int, int, int]] = []
        heappush(order, (0, 0, src))

        while order:
            stops, cost, node = heappop(order)

            for neighbor, travel_cost in graph[node]:
                if stops <= k and cost + travel_cost < costs[neighbor][stops + 1]:
                    costs[neighbor][stops + 1] = cost + travel_cost
                    heappush(order, (stops + 1, cost + travel_cost, neighbor))

        answer = min(costs[dst])
        return answer if answer != int(1e9) else -1

    def __load_graph(self, flights: list[list[int]], n: int) -> list[list[tuple[int, int]]]:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for flight_start, flight_end, flight_cost in flights:
            graph[flight_start].append((flight_end, flight_cost))

        return graph
