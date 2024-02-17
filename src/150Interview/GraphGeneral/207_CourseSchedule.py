class Node:
    def __init__(self, index: int):
        self.index = index
        self.neighbors: list["Node"] = []


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        nodes: list[Node] = []

        self.__construct_graph(prerequisites, nodes, numCourses)

        visited = [False for _ in range(numCourses)]

        for node in nodes:
            if not visited[node.index]:
                if self.__find_cycle(node, visited, set()):
                    return False

        return True

    def __find_cycle(self, node: Node, visited: list[bool], last_nodes: set[int]) -> bool:
        visited[node.index] = True
        last_nodes.add(node.index)

        for neighbor in node.neighbors:
            if neighbor.index in last_nodes:
                return True
            if not visited[neighbor.index]:
                if self.__find_cycle(neighbor, visited, last_nodes):
                    return True

        last_nodes.remove(node.index)
        return False

    def __construct_graph(self, prerequisites: list[list[int]], nodes: list[Node], numCourses: int) -> None:
        for course_index in range(numCourses):
            nodes.append(Node(index=course_index))

        for node_a, node_b in prerequisites:
            nodes[node_b].neighbors.append(nodes[node_a])
