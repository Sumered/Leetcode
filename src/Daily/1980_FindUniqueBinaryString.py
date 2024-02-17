class Solution:
    def findDifferentBinaryString(self, numbers: list[str]) -> str:
        return self.__recurrent_find_missing_number("", numbers, len(numbers))[0]

    def __recurrent_find_missing_number(self, missing_number: str, numbers: list[str], chars_to_fill: int) -> tuple[str, bool]:
        if chars_to_fill == 0:
            if missing_number not in numbers:
                return missing_number, True
            return missing_number, False

        with_one, succeeded = self.__recurrent_find_missing_number(missing_number + "1", numbers, chars_to_fill - 1)
        if succeeded:
            return with_one, succeeded

        with_zero, succeeded = self.__recurrent_find_missing_number(missing_number + "0", numbers, chars_to_fill - 1)
        if succeeded:
            return with_zero, succeeded

        return missing_number, False
