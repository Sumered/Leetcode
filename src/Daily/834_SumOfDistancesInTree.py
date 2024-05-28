class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        distances: list[tuple[int, int]] = [(0, 0) for _ in range(n)]
        visited = [False for _ in range(n)]
        self.__calculate_distances(0, graph, distances, visited)

        total_distances = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        self.__calculate_total_distances(0, 0, 0, graph, distances, visited, total_distances)

        return total_distances

    def __calculate_distances(
        self, node: int, graph: list[list[int]], distances: list[tuple[int, int]], visited: list[bool]
    ) -> tuple[int, int]:
        visited[node] = True
        total_distances, nodes = 0, 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                child_distances, child_nodes = self.__calculate_distances(neighbor, graph, distances, visited)
                total_distances += child_distances + child_nodes
                nodes += child_nodes

        distances[node] = (total_distances, nodes)
        return total_distances, nodes

    def __calculate_total_distances(
        self,
        node: int,
        parent_nodes: int,
        cumulative_distance: int,
        graph: list[list[int]],
        distances: list[tuple[int, int]],
        visited: list[bool],
        total_distances: list[int],
    ) -> None:
        visited[node] = True
        total_distances[node] = cumulative_distance + distances[node][0]

        for neighbor in graph[node]:
            if not visited[neighbor]:
                new_parent_nodes = parent_nodes + (distances[node][1] - distances[neighbor][1])

                new_cumulative_distance = (
                    cumulative_distance + new_parent_nodes + (distances[node][0] - distances[neighbor][0] - distances[neighbor][1])
                )

                self.__calculate_total_distances(
                    neighbor, new_parent_nodes, new_cumulative_distance, graph, distances, visited, total_distances
                )

        return
