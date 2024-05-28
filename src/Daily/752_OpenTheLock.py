from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        visited = set()

        for deadend in deadends:
            visited.add(deadend)

        node_queue, next_node_queue = deque(), deque()

        node_queue.append("0000")
        depth = 0

        while node_queue:
            while node_queue:
                current_node = node_queue.pop()
                neighbors = self.__get_neighbors(current_node)

                for neighbor in neighbors:
                    if neighbor == target:
                        return depth + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_node_queue.append(neighbor)

            node_queue = next_node_queue
            next_node_queue = deque()
            depth += 1

        return -1

    def __get_neighbors(self, number: str) -> list[str]:
        neighbors = []

        for pos in range(len(number)):
            neighbors.append(self.__one_up(number, pos))
            neighbors.append(self.__one_down(number, pos))

        return neighbors

    def __one_up(self, number: str, pos: int) -> str:
        if number[pos] == "9":
            return f"{number[:pos]}0{number[pos + 1:]}"
        return f"{number[:pos]}{int(number[pos]) + 1}{number[pos + 1:]}"

    def __one_down(self, number: str, pos: int) -> str:
        if number[pos] == "0":
            return f"{number[:pos]}9{number[pos + 1:]}"
        return f"{number[:pos]}{int(number[pos]) - 1}{number[pos + 1:]}"
