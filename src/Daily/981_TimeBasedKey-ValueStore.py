from collections import defaultdict


class TimeMap:

    def __init__(self) -> None:
        self.__dict: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.__dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.__dict:
            return ""
        left, right = 0, len(self.__dict[key]) - 1

        while left < right:
            medium = (left + right) // 2
            if self.__dict[key][medium][0] >= timestamp:
                right = medium
            else:
                left = medium + 1
        if self.__dict[key][left][0] > timestamp:
            if left > 0:
                return self.__dict[key][left - 1][1]
            return ""
        return self.__dict[key][left][1]
