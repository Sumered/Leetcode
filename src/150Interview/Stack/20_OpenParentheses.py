class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = []
        matching = {")": "(", "}": "{", "]": "["}
        opening = matching.values()
        closing = matching.keys()

        for character in s:
            if character in opening:
                open_parentheses.append(character)
            else:
                if len(open_parentheses) != 0 and open_parentheses[-1] == matching[character]:
                    open_parentheses.pop()
                else:
                    return False
        return not open_parentheses
