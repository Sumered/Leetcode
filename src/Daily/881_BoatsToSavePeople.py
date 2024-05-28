class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boats, left, right = 0, 0, len(people) - 1

        while left <= right:
            if people[right] + people[left] <= limit:
                left += 1
            boats += 1
            right -= 1

        return boats
