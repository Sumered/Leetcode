class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = str(x)
        for index, character in enumerate(numbers):
            if character != numbers[len(numbers) - index - 1]:
                return False
        return True
