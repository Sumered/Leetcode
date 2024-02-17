class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0
        right_index = 0
        word_length = len(s)
        longest_substring = 0
        letters_ocurred: set[str] = set()

        while right_index < word_length:
            character = s[right_index]
            if character in letters_ocurred:
                while character in letters_ocurred:
                    letters_ocurred.remove(s[left_index])
                    left_index += 1

            letters_ocurred.update(character)
            longest_substring = max(longest_substring, len(letters_ocurred))
            right_index += 1

        return longest_substring
