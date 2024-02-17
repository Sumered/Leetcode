class Solution:
    def longestPalindrome(self, s: str) -> str:
        new_s = "#" + "#".join(s) + "#"
        radius = [0 for _ in range(len(new_s))]
        center, right, max_radius, max_center = 0, 0, 0, 0

        for index in range(1, len(new_s) - 1):
            mirrored_index = 2 * center - index
            if index < right:
                radius[index] = min(right - index, radius[mirrored_index])

            left_index = index - radius[index] - 1
            right_index = index + radius[index] + 1
            while left_index >= 0 and right_index < len(new_s) and new_s[left_index] == new_s[right_index]:
                radius[index] += 1
                left_index = index - radius[index] - 1
                right_index = index + radius[index] + 1

            if index + radius[index] > right:
                right = index + radius[index]
                center = index

            if radius[index] > max_radius:
                max_radius = radius[index]
                max_center = index

        start_pos = (max_center - max_radius) // 2

        return s[start_pos : start_pos + max_radius]
