class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        nodes_count, max_value = len(nums), max(nums)
        primes = Primes(max_value)
        graph = UnionFind(nodes_count)

        prime_to_node_mapping: dict[int, int] = {}

        for index, number in enumerate(nums):
            for prime_divider in primes.factors[number]:
                prime_to_node_mapping[prime_divider] = prime_to_node_mapping.get(prime_divider, index)
                graph.union(index, prime_to_node_mapping[prime_divider])

        return graph.get_node_rank(graph.find(0)) == nodes_count


class UnionFind:
    def __init__(self, count: int) -> None:
        self.__rank = [1] * count
        self.__parent = [i for i in range(count)]

    def find(self, index: int) -> int:
        if self.__parent[index] == index:
            return index
        self.__parent[index] = self.find(self.__parent[index])
        return self.__parent[index]

    def union(self, index_f: int, index_s: int) -> None:
        parent_f, parent_s = self.find(index_f), self.find(index_s)

        if parent_f == parent_s:
            return

        if self.__rank[parent_f] < self.__rank[parent_s]:
            parent_f, parent_s = parent_s, parent_f

        self.__parent[parent_s] = parent_f
        self.__rank[parent_f] += self.__rank[parent_s]

    def get_node_rank(self, index: int) -> int:
        return self.__rank[index]


class Primes:
    def __init__(self, limit: int) -> None:
        self.factors = self.__factorize(limit)

    def __factorize(self, limit: int) -> list[list[int]]:
        factors: list[list[int]] = [[] for _ in range(limit + 1)]

        for number in range(2, limit + 1):
            if not factors[number]:
                for complex_number in range(number, limit + 1, number):
                    factors[complex_number].append(number)

        return factors
