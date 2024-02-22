class Solution:
    def findJudge(self, n: int, trust_list: list[list[int]]) -> int:
        in_level = [0 for _ in range(n + 1)]
        out_level = [0 for _ in range(n + 1)]

        for trust in trust_list:
            trust_a, trust_b = trust[0], trust[1]
            out_level[trust_a] += 1
            in_level[trust_b] += 1

        for person in range(1, n + 1):
            if in_level[person] == n - 1 and out_level[person] == 0:
                return person

        return -1
