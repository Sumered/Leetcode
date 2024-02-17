class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies_given = [1 for _ in ratings]

        self.__traverse_list(ratings, candies_given)

        self.__traverse_list_reverse(ratings, candies_given)

        return sum(candies_given)

    def __traverse_list(self, ratings: list[int], candies_given: list[int]) -> None:
        for index in range(len(ratings) - 1):
            if ratings[index] < ratings[index + 1]:
                candies_given[index + 1] = max(candies_given[index + 1], candies_given[index] + 1)

    def __traverse_list_reverse(self, ratings: list[int], candies_given: list[int]) -> None:
        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candies_given[index] = max(candies_given[index], candies_given[index + 1] + 1)
