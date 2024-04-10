class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time_taken = 0
        at_most = tickets[k]

        for index in range(len(tickets)):
            if index > k:
                time_taken += min(at_most - 1, tickets[index])
            else:
                time_taken += min(at_most, tickets[index])

        return time_taken
