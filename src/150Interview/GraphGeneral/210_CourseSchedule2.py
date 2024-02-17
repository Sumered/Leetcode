from collections import deque


class Node:
    def __init__(self, index: int):
        self.index = index
        self.ingoing: int = 0
        self.neighbors: list["Node"] = []


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        nodes: list[Node] = []
        self.__construct_graph(prerequisites, nodes, numCourses)

        nodes_queue: deque[int] = deque()
        visited: list[bool] = [False for _ in range(numCourses)]
        self.__add_first_nodes(nodes, nodes_queue)

        answer = []
        while len(nodes_queue) != 0:
            node = nodes[nodes_queue.popleft()]
            visited[node.index] = True
            answer.append(node.index)

            for neighbor in node.neighbors:
                neighbor.ingoing -= 1
                if neighbor.ingoing == 0:
                    nodes_queue.append(neighbor.index)

        if all(visited):
            return answer
        return []

    def __add_first_nodes(self, nodes: list[Node], nodes_queue: deque[int]) -> None:
        for node in nodes:
            if node.ingoing == 0:
                nodes_queue.append(node.index)

    def __construct_graph(self, prerequisites: list[list[int]], nodes: list[Node], numCourses: int) -> None:
        for course_index in range(numCourses):
            nodes.append(Node(index=course_index))

        for node_a, node_b in prerequisites:
            nodes[node_b].neighbors.append(nodes[node_a])
            nodes[node_a].ingoing += 1
