class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        visited: dict[int, "Node"] = {}

        self.__travel_graph(node, visited)

        return visited[1]

    def __travel_graph(self, node: Node, visited: dict[int, Node]) -> None:
        copied_node = Node(val=node.val)
        visited[node.val] = copied_node

        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                self.__travel_graph(neighbor, visited)
            copied_node.neighbors.append(visited[neighbor.val])
