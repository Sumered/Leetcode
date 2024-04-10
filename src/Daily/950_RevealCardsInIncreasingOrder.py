from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        number_to_original_pos = {number: index for index, number in enumerate(deck)}
        original_position_end = {}
        simulation_deck = deque(deck)
        end_index = 0

        while simulation_deck:
            first_item = simulation_deck.popleft()
            if simulation_deck:
                second_item = simulation_deck.popleft()
                simulation_deck.append(second_item)
            original_pos = number_to_original_pos[first_item]
            original_position_end[end_index] = original_pos
            end_index += 1

        deck_sorted = sorted(deck)
        result = [-1 for _ in range(len(deck))]
        for index, number in enumerate(deck_sorted):
            result[original_position_end[index]] = number

        return result
