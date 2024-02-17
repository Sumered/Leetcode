class Solution:
    def isHappy(self, number: int) -> bool:
        already_ocurred: set[int] = set()
        while True:
            if number in already_ocurred:
                return False
            already_ocurred.add(number)
            number = self.__process_number(number)

            if number == 1:
                return True

    def __process_number(self, number: int) -> int:
        processed_number = 0
        while number > 0:
            processed_number += (number % 10) ** 2
            number = number // 10

        return processed_number


algos = Solution()
print(algos.isHappy(19))
