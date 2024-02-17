from collections import deque


class Solution:
    def ladderLength(self, startWord: str, endWord: str, bank: list[str]) -> int:
        bank.append(startWord)

        visited: set[str] = set()
        current_queue: deque[str] = deque()
        next_queue: deque[str] = deque()

        distance = 1
        current_queue.append(startWord)

        while len(next_queue) != 0 or len(current_queue) != 0:
            while len(current_queue) != 0:
                current_word = current_queue.pop()

                if current_word == endWord:
                    return distance

                if current_word in visited:
                    continue

                bank.remove(current_word)
                visited.add(current_word)

                for bank_word in bank:
                    if not bank_word in visited and self.__can_mutate(current_word, bank_word):
                        next_queue.append(bank_word)

            distance += 1
            current_queue, next_queue = next_queue, current_queue
        return 0

    def __can_mutate(self, word: str, new_word: str) -> bool:
        diff_count = 0

        for g, ng in zip(word, new_word):
            if g != ng:
                diff_count += 1

        return diff_count == 1
