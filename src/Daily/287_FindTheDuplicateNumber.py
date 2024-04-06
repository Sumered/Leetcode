class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        second_slow = 0

        while True:
            slow = nums[slow]
            second_slow = nums[second_slow]
            if slow == second_slow:
                break

        return slow
