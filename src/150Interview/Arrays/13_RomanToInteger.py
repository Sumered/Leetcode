class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        letter_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for index in range(len(s)):
            if index + 1 < len(s) and not self.__is_next_smaller(s[index], s[index + 1], letter_to_int):
                result -= letter_to_int[s[index]]
            else:
                result += letter_to_int[s[index]]
        return result

    def __is_next_smaller(self, character_left: str, character_right: str, letter_to_int: dict[str, int]) -> bool:
        left_value = letter_to_int[character_left]
        right_value = letter_to_int[character_right]
        return left_value >= right_value


algos = Solution()
print(algos.romanToInt("LVIII"))
