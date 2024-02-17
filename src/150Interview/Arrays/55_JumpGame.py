class Solution:
    def canJump(self, numbers: list[int]) -> bool:
        max_jump_reserve = 0
        for number in numbers[: len(numbers) - 1]:
            max_jump_reserve = max(max_jump_reserve - 1, number)
            if max_jump_reserve == 0:
                return False

        return True
