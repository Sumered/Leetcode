from queue import PriorityQueue


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score_queue = PriorityQueue()
        new_scores = ["" for _ in range(len(score))]

        for index, scr in enumerate(score):
            score_queue.put((-scr, index))

        pop_index = 0

        while not score_queue.empty():
            scr, index = score_queue.get()
            if pop_index == 0:
                new_scores[index] = "Gold Medal"
            elif pop_index == 1:
                new_scores[index] = "Silver Medal"
            elif pop_index == 2:
                new_scores[index] = "Bronze Medal"
            else:
                new_scores[index] = str(pop_index + 1)

            pop_index += 1

        return new_scores
