class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first, second = int(4e9 + 7), int(4e9 + 7)
        for number in nums:
            if number <= first:
                first = number
            elif number <= second:
                second = number
            else:
                return True
        return False
