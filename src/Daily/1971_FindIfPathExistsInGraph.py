class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph: list[list[int]] = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = [False for _ in range(n)]

        self.__travel(source, graph, visited)

        return visited[destination]

    def __travel(self, node: int, graph: list[list[int]], visited: list[bool]) -> None:
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.__travel(neighbor, graph, visited)

        return
