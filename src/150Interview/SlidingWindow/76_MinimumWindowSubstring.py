class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best_substring = s + "!"
        left_index, right_index = 0, 0
        counts_window: dict[str, int] = {}
        counts_target = self.__count_characters(t)

        while right_index < len(s):
            while right_index < len(s) and not self.__dictionary_containment(counts_window, counts_target):
                counts_window[s[right_index]] = counts_window.get(s[right_index], 0) + 1
                right_index += 1

            if not self.__dictionary_containment(counts_window, counts_target):
                return best_substring if best_substring != s + "!" else ""

            while left_index < right_index:
                if self.__dictionary_containment(counts_window, counts_target):
                    if right_index - left_index < len(best_substring):
                        best_substring = s[left_index:right_index]
                else:
                    break
                counts_window[s[left_index]] -= 1
                left_index += 1

        return best_substring if best_substring != s + "!" else ""

    def __dictionary_containment(self, target_dict: dict[str, int], dict_contained: dict[str, int]) -> bool:
        for character, count in dict_contained.items():
            if character not in target_dict or target_dict[character] < count:
                return False
        return True

    def __count_characters(self, word: str) -> dict[str, int]:
        counts: dict[str, int] = {}
        for character in word:
            counts[character] = counts.get(character, 0) + 1
        return counts


Solution().minWindow(s="ADOBECODEBANC", t="ABC")
