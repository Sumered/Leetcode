class Node:
    def __init__(self, index: str):
        self.index = index
        self.neighbors: list[tuple["Node", float]] = []


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        nodes: dict[str, Node] = {}

        self.__construct_graph(equations, values, nodes)

        answers = []
        for query_start, query_end in queries:
            if query_start not in nodes or query_end not in nodes:
                answers.append(-1.0)
                continue
            visited: set[str] = set()
            answers.append(self.__find_solution(nodes[query_start], query_end, visited, 1.0))

        return answers

    def __find_solution(self, node: Node, end_index: str, visited: set[str], current_val: float) -> float:
        if node.index == end_index:
            return current_val

        visited.add(node.index)

        for neighbor, weight in node.neighbors:
            if neighbor.index not in visited:
                returned_val = self.__find_solution(neighbor, end_index, visited, current_val * weight)
                if returned_val != -1:
                    return returned_val
        return -1

    def __construct_graph(self, equations: list[list[str]], values: list[float], nodes: dict[str, Node]) -> None:
        for (node_a, node_b), value in zip(equations, values):
            if node_a not in nodes:
                nodes[node_a] = Node(node_a)
            if node_b not in nodes:
                nodes[node_b] = Node(node_b)

            nodes[node_a].neighbors.append((nodes[node_b], value))
            nodes[node_b].neighbors.append((nodes[node_a], 1 / value))
