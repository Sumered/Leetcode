import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        speed_left, speed_right = 1, max(piles)

        while speed_left < speed_right:
            medium = (speed_left + speed_right) // 2
            succeded = self.__eat_bananas(piles, medium, h)
            if succeded:
                speed_right = medium
            else:
                speed_left = medium + 1

        return speed_left

    def __eat_bananas(self, piles: list[int], speed: int, hours: int) -> bool:
        hours_used = 0
        for pile in piles:
            hours_used += math.ceil(pile / speed)
            if hours_used > hours:
                return False
        return True
