class Solution:
    def __init__(self) -> None:
        self.__min_height = int(1e9)
        self.__minimum_height_nodes: list[int] = []

    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        heights = [[0, 0] for _ in range(n)]
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for node_a, node_b in edges:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        self.__calculate_heights(0, graph, heights, visited)

        visited = [False for _ in range(n)]

        self.__find_minimum_height_nodes(0, graph, heights, visited, 0)

        return self.__minimum_height_nodes

    def __find_minimum_height_nodes(
        self, node: int, graph: list[list[int]], heights: list[list[int]], visited: list[bool], depth: int
    ) -> None:
        visited[node] = True
        current_max_height = max(depth, heights[node][0])
        self.__update_solution(current_max_height, node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                new_depth = heights[node][0] + 1 if heights[neighbor][0] + 1 != heights[node][0] else heights[node][1] + 1
                new_depth = max(depth + 1, new_depth)
                self.__find_minimum_height_nodes(neighbor, graph, heights, visited, new_depth)

        return

    def __calculate_heights(self, node: int, graph: list[list[int]], heights: list[list[int]], visited: list[bool]) -> list[int]:
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                son_height = self.__calculate_heights(neighbor, graph, heights, visited)
                self.__update_two_maxes(heights[node], son_height[0] + 1)

        return heights[node]

    def __update_solution(self, current_max_height: int, node: int) -> None:
        if current_max_height < self.__min_height:
            self.__min_height = current_max_height
            self.__minimum_height_nodes.clear()
            self.__minimum_height_nodes.append(node)
        elif current_max_height == self.__min_height:
            self.__minimum_height_nodes.append(node)

    def __update_two_maxes(self, heights: list[int], new_height: int) -> None:
        if new_height > heights[0]:
            heights[1] = heights[0]
            heights[0] = new_height
        elif new_height > heights[1]:
            heights[1] = new_height
