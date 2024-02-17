class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result: list[int] = []
        for i in range(len(str(low)), len(str(high)) + 1):
            self.__generate(low, high, i, result)
        return result

    def __generate(self, lower: int, upper: int, digits: int, numbers: list[int]) -> None:
        current_number = self.__generate_first_number(digits)
        while self.__is_correct(current_number, digits) and current_number < lower:
            current_number = self.__get_next_number(current_number, digits)
        while self.__is_correct(current_number, digits) and current_number <= upper:
            numbers.append(current_number)
            current_number = self.__get_next_number(current_number, digits)
        return

    def __is_correct(self, number: int, digits: int) -> bool:
        return int(str(number)[0]) + digits <= 10 and len(str(number)) <= digits

    def __get_next_number(self, number: int, digits: int) -> int:
        addition = int("1" * digits)
        return number + addition

    def __generate_first_number(self, digits: int) -> int:
        number = ""
        for i in range(digits):
            number += str(i + 1)
        return int(number)
