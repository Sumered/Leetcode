class Solution:
    def frequencySort(self, s: str) -> str:
        character_count: dict[str, int] = {}
        for character in s:
            character_count[character] = character_count.get(character, 0) + 1

        sorted_characters = sorted(character_count.items(), key=lambda item: (-item[1], item[0]))

        result = ""

        for char, count in sorted_characters:
            result += char * count

        return result
