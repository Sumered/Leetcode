class Solution:
    def __init__(self) -> None:
        self.letters = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    def halvesAreAlike(self, s: str) -> bool:
        first_half_counts, second_half_counts = 0, 0

        for index, letter in enumerate(s):
            if letter in self.letters:
                if index < len(s) // 2:
                    first_half_counts += 1
                else:
                    second_half_counts += 1

        return first_half_counts == second_half_counts
