import random


class RandomizedSet:
    def __init__(self) -> None:
        self.__values: list[int] = []
        self.__value_to_index: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val not in self.__value_to_index:
            self.__values.append(val)
            self.__value_to_index[val] = len(self.__values) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.__value_to_index:
            self.__value_to_index[self.__values[len(self.__values) - 1]] = self.__value_to_index[val]
            self.__values[self.__value_to_index[val]], self.__values[len(self.__values) - 1] = (
                self.__values[len(self.__values) - 1],
                self.__values[self.__value_to_index[val]],
            )

            self.__values.pop()
            del self.__value_to_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.__values)


obj = RandomizedSet()
obj.insert(0)
obj.insert(1)
obj.remove(0)
obj.insert(2)
obj.remove(1)
print(obj.getRandom())
