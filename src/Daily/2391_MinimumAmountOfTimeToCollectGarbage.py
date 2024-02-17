from dataclasses import dataclass


@dataclass
class Garbage:
    metal: int
    paper: int
    glass: int

    def sum(self) -> int:
        return self.metal + self.paper + self.glass


class Solution:
    def garbageCollection(self, garbage: list[str], travel: list[int]) -> int:
        houses_count = len(travel)
        required_time = 0
        trucks_multiplier = 3
        max_indexes = self.__return_last_indexes(garbage)

        for house_index in range(houses_count):
            garbage_count = self.__parse_garbages(garbage[house_index])
            required_time += garbage_count.sum()
            trucks_multiplier -= self.__check_limit(house_index, max_indexes)
            required_time += travel[house_index] * trucks_multiplier

        required_time += self.__parse_garbages(garbage[houses_count]).sum()
        return required_time

    def __parse_garbages(self, garbage: str) -> Garbage:
        return Garbage(garbage.count("M"), garbage.count("P"), garbage.count("G"))

    def __check_limit(self, house_index: int, max_indexes: tuple[int, int, int]) -> int:
        return sum(1 for index in max_indexes if index == house_index)

    def __return_last_indexes(self, garbage: list[str]) -> tuple[int, int, int]:
        max_metal_index, max_paper_index, max_glass_index = 0, 0, 0
        max_metal_index = self.__find_last_index(garbage, "M")
        max_paper_index = self.__find_last_index(garbage, "P")
        max_glass_index = self.__find_last_index(garbage, "G")
        return max_metal_index, max_paper_index, max_glass_index

    def __find_last_index(self, garbage: list[str], character: str) -> int:
        max_index = 0
        for index, garbage_description in enumerate(garbage):
            max_index = index if character in garbage_description else max_index
        return max_index


algos = Solution()
print(algos.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
