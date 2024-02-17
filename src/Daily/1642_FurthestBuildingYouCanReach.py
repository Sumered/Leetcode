# type: ignore
from sortedcontainers import SortedList


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        largest = SortedList(key=lambda x: -x)
        sum_of_rest, previous_height = 0, int(1e9) + 7
        for index, height in enumerate(heights):
            if previous_height >= height:
                previous_height = height
                continue
            difference = height - previous_height

            if len(largest) == ladders:
                if ladders != 0 and largest[-1] < difference:
                    smaller = largest.pop()
                    largest.add(difference)
                    sum_of_rest += smaller
                else:
                    sum_of_rest += difference
                if sum_of_rest > bricks:
                    return index - 1
            else:
                largest.add(difference)

            previous_height = height

        return len(heights) - 1


Solution().furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2)
