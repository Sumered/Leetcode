class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        games: dict[int, list[int]] = {}

        for match in matches:
            winner, loser = match[0], match[1]
            if winner not in games:
                games[winner] = [0, 0]
            if loser not in games:
                games[loser] = [0, 0]
            games[winner][0] += 1
            games[loser][1] += 1

        winners, near_winners = [], []
        for player, results in games.items():
            if results[1] == 0:
                winners.append(player)
            elif results[1] == 1:
                near_winners.append(player)

        return [sorted(winners), sorted(near_winners)]
