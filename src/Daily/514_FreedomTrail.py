from functools import cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        result = self.__jumping(0, 0, ring, key)

        return result

    @cache
    def __jumping(self, ring_pos: int, key_pos: int, ring: str, key: str) -> int:
        if key_pos >= len(key):
            return 0

        if ring[ring_pos] == key[key_pos]:
            return self.__jumping(ring_pos, key_pos + 1, ring, key) + 1

        left_pos, left_cost = self.__find_pos(ring_pos, key_pos, ring, key, -1)
        right_pos, right_cost = self.__find_pos(ring_pos, key_pos, ring, key, 1)

        left_total_cost = left_cost + 1 + self.__jumping(left_pos, key_pos + 1, ring, key)
        right_total_cost = right_cost + 1 + self.__jumping(right_pos, key_pos + 1, ring, key)

        return min(left_total_cost, right_total_cost)

    def __find_pos(self, ring_pos: int, key_pos: int, ring: str, key: str, direction: int) -> tuple[int, int]:
        total_cost = 0

        while ring[ring_pos] != key[key_pos]:
            total_cost += 1
            ring_pos += direction
            ring_pos = ring_pos % len(ring)

        return ring_pos, total_cost


Solution().findRotateSteps(ring="godding", key="godding")
