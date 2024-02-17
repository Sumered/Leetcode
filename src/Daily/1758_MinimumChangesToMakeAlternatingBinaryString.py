class Solution:
    def minOperations(self, s: str) -> int:
        previous_char, operations = s[0], [{"0": 0, "1": 0} for _ in range(len(s))]
        opposite_char = {"1": "0", "0": "1"}

        operations[0][s[0]] = 0
        operations[0][opposite_char[s[0]]] = 1

        for index, char in enumerate(s[1:]):
            operations[index + 1][char] = operations[index][opposite_char[char]]
            operations[index + 1][opposite_char[char]] = operations[index][char] + 1

        return min(operations[len(s) - 1].values())
