import re


class Solution:
    def isPalindrome(self, sentence: str) -> bool:
        sentence = self.__clean_string(sentence)
        left_index, right_index = 0, len(sentence) - 1

        while left_index < right_index:
            if sentence[left_index] != sentence[right_index]:
                return False

            left_index += 1
            right_index -= 1

        return True

    def __clean_string(self, sentence: str) -> str:
        return re.sub(r"\W+", "", sentence.lower()).replace("_", "")
