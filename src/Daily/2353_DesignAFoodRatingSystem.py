# type: ignore
class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.__food_to_cuisine: dict[str, list[str | int]] = self.__map_food(zip(foods, cuisines))
        self.__cuisines: dict[str, MinTree] = {}

        for cuisine in cuisines:
            if cuisine not in self.__cuisines:
                cuisine_count = cuisines.count(cuisine)
                foods_from_cuisine: list[list[int | str]] = [[ratings[i], foods[i]] for i in range(len(foods)) if cuisines[i] == cuisine]
                self.__cuisines[cuisine] = self.__construct(foods_from_cuisine, cuisine_count)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, index = self.__food_to_cuisine[food]
        real_index = self.__cuisines[cuisine].offset_index(index)
        self.__cuisines[cuisine].tree[real_index] = [-newRating, food]
        self.__cuisines[cuisine].update([-newRating, food], real_index, food)

    def highestRated(self, cuisine: str) -> str:
        return self.__cuisines[cuisine].tree[1][1]

    def __map_food(self, foods_from_cuisine: list[list[str]]) -> dict[str, list[str | int]]:
        food_to_cuisine: dict[str, list[str | int]] = {}
        cuisine_offset = {}

        for food_in_cuisine, cuisine in foods_from_cuisine:
            cuisine_offset[cuisine] = cuisine_offset.get(cuisine, 0) + 1
            food_to_cuisine[food_in_cuisine] = [cuisine, cuisine_offset[cuisine] - 1]
        return food_to_cuisine

    def __construct(self, foods: list[list[int | str]], count: int) -> "MinTree":
        min_tree = MinTree(count)
        for index, food in enumerate(foods):
            food[0] *= -1
            true_index = min_tree.offset_index(index)
            min_tree.update(food, true_index, food[1])

        return min_tree


class MinTree:
    def __init__(self, size: int):
        self.lowest_size = self.__get_lowest_power(size)
        self.tree: list[list[int | str]] = [[int(1e9), ""] for _ in range(self.lowest_size)]

    def __get_lowest_power(self, size: int) -> int:
        power = 1
        while power < size:
            power *= 2
        return power * 2

    def offset_index(self, index: int) -> int:
        return (self.lowest_size // 2) + index

    def update(self, value: list[int | str], index: int, original_name: str) -> None:
        if index == 0:
            return
        if self.tree[index][1] == original_name and index < self.lowest_size // 2:
            self.tree[index] = min(self.tree[index * 2], self.tree[index * 2 + 1])
        else:
            self.tree[index] = min(value, self.tree[index])
        self.update(self.tree[index], index // 2, original_name)

    def get_value(self, current_index: int, left_end: int, right_end: int, left_index: int, right_index: int) -> list[int | str]:
        if left_index == left_end and right_index == right_end:
            return self.tree[current_index]
        middle_point = (left_end + right_end) // 2

        if left_index <= middle_point and right_index <= middle_point:
            return self.get_value(current_index * 2, left_end, middle_point, left_index, right_index)

        if left_index <= middle_point and right_index > middle_point:
            left_min = self.get_value(current_index * 2, left_end, middle_point, left_index, middle_point)
            right_min = self.get_value(current_index * 2 + 1, middle_point + 1, right_end, middle_point + 1, right_index)
            return min(left_min, right_min)

        return self.get_value(current_index * 2 + 1, middle_point + 1, right_end, left_index, right_index)
