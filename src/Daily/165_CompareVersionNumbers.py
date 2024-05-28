class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splitted_v1 = version1.split(".")
        splitted_v2 = version2.split(".")

        while len(splitted_v1) < len(splitted_v2):
            splitted_v1.append("0")
        while len(splitted_v2) < len(splitted_v1):
            splitted_v2.append("0")

        for split_v1, split_v2 in zip(splitted_v1, splitted_v2):
            number_v1 = int(split_v1)
            number_v2 = int(split_v2)
            if number_v1 < number_v2:
                return -1
            elif number_v1 > number_v2:
                return 1

        return 0
