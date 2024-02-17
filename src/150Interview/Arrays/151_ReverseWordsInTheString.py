class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.__get_words(s)
        words.reverse()
        return " ".join(words)

    def __get_words(self, s: str) -> list[str]:
        words = []
        start_index = 0
        for index, character in enumerate(s + " "):
            if character == " ":
                if start_index != index:
                    words.append(s[start_index:index])
                start_index = index + 1
        return words
