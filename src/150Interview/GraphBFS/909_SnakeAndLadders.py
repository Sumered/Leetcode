class Node:
    def __init__(self, index: int):
        self.distance = 10000
        self.index = index
        self.neighbors: list["Node"] = []


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        nodes: list[Node] = [Node(index) for index in range(n**2)]

        self.__construct_graph(board, nodes, n)

        self.__dfs(nodes[0], 0)

        return nodes[n**2 - 1].distance if nodes[n**2 - 1].distance != 10000 else -1

    def __dfs(self, node: Node, distance: int) -> None:
        node.distance = min(node.distance, distance)
        for neighbor in node.neighbors:
            if neighbor.distance > node.distance + 1:
                self.__dfs(neighbor, distance + 1)

    def __construct_graph(self, board: list[list[int]], nodes: list[Node], n: int) -> None:
        node_index = 0

        for _ in range(n):
            for _ in range(n):
                self.__add_neighbors(board, nodes, node_index)
                node_index += 1

    def __add_neighbors(self, board: list[list[int]], nodes: list[Node], node_index: int) -> None:
        n = len(board)

        for offset in range(1, 7):
            offset_node_index = node_index + offset
            if offset_node_index >= n**2:
                break
            offset_row = n - (offset_node_index // n) - 1
            offset_column = offset_node_index % n if (offset_node_index // n) % 2 == 0 else n - (offset_node_index % n) - 1

            if board[offset_row][offset_column] == -1:
                nodes[node_index].neighbors.append(nodes[node_index + offset])
            else:
                nodes[node_index].neighbors.append(nodes[board[offset_row][offset_column] - 1])


print(Solution().snakesAndLadders([[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]))
