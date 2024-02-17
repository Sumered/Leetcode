class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        output: list[list[str]] = [[] for _ in range(numRows)]
        full_traversal = numRows * 2 - 2

        for index, character in enumerate(s):
            modulo = index % full_traversal
            if modulo >= numRows:
                modulo = full_traversal - modulo
            output[modulo].append(character)

        parsed_output = "".join("".join(x) for x in output)
        return parsed_output


print(Solution().convert("A", 1))
