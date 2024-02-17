class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        result = 0
        previous_row_count, current_row_count = 0, 0

        for row in bank:
            current_row_count = row.count("1")
            result += current_row_count * previous_row_count

            if current_row_count != 0:
                previous_row_count = current_row_count

        return result
