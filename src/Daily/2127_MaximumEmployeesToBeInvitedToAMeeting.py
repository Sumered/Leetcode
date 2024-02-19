class Solution:
    def maximumInvitations(self, favorites: list[int]) -> int:
        visited = [False for _ in range(len(favorites))]
        (neighbors, pairs) = self.__prepare_graph(favorites, visited)

        most_possible_employees = self.__process_cycles(neighbors, visited)

        if len(pairs) != 0:
            non_cyclic_result = self.__process_rest(neighbors, visited, pairs)
            most_possible_employees = max(most_possible_employees, non_cyclic_result + 2 * len(pairs))

        return most_possible_employees

    def __process_rest(self, neighbors: list[int], visited: list[bool], pairs: list[tuple[int, int]]) -> int:
        result = 0
        reversed_neighbors = self.__reverse_neighbors(neighbors)

        for left_node, right_node in pairs:
            current_result = self.__travel(left_node, reversed_neighbors, 0) + self.__travel(right_node, reversed_neighbors, 0)
            result += current_result

        return result

    def __travel(self, node: int, neighbors: list[list[int]], depth: int) -> int:
        res = depth
        for neighbor in neighbors[node]:
            res = max(res, self.__travel(neighbor, neighbors, depth + 1))
        return res

    def __reverse_neighbors(self, neighbors: list[int]) -> list[list[int]]:
        reversed_neighbors: list[list[int]] = [[] for _ in range(len(neighbors))]

        for node in range(len(neighbors)):
            if node != neighbors[neighbors[node]]:
                reversed_neighbors[neighbors[node]].append(node)

        return reversed_neighbors

    def __process_cycles(self, neighbors: list[int], visited: list[bool]) -> int:
        result = 0

        for node in range(len(neighbors)):
            if not visited[node]:
                result = max(result, self.__find_cycle(node, neighbors, visited, {}, 1))

        return result

    def __find_cycle(self, node: int, neighbors: list[int], visited: list[bool], path: dict[int, int], path_length: int) -> int:
        if visited[node]:
            return -1

        visited[node] = True
        path[node] = path_length
        next_node = neighbors[node]
        if next_node in path:
            return path[node] - path[next_node] + 1

        return self.__find_cycle(next_node, neighbors, visited, path, path_length + 1)

    def __prepare_graph(self, favorites: list[int], visited: list[bool]) -> tuple[list[int], list[tuple[int, int]]]:
        employee_count = len(favorites)
        neighbors = [-1 for _ in range(employee_count)]
        pairs = []

        for index, favorite in enumerate(favorites):
            neighbors[index] = favorite
            if neighbors[favorite] == index:
                pairs.append((favorite, index))
                visited[favorite] = True
                visited[index] = True

        return neighbors, pairs
