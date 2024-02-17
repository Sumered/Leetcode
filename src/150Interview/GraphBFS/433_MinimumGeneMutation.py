from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        visited: set[str] = set()
        current_queue: deque[str] = deque()
        next_queue: deque[str] = deque()

        distance = 0
        current_queue.append(startGene)

        while len(next_queue) != 0 or len(current_queue) != 0:
            while len(current_queue) != 0:
                current_gene = current_queue.pop()

                if current_gene == endGene:
                    return distance

                if current_gene in visited:
                    continue

                visited.add(current_gene)

                for bank_gene in bank:
                    if not bank_gene in visited and self.__can_mutate(current_gene, bank_gene):
                        next_queue.append(bank_gene)

            distance += 1
            current_queue, next_queue = next_queue, current_queue
        return -1

    def __can_mutate(self, gene: str, new_gene: str) -> bool:
        diff_count = 0

        for g, ng in zip(gene, new_gene):
            if g != ng:
                diff_count += 1

        return diff_count == 1
