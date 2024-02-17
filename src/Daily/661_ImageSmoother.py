class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        new_img: list[list[int]] = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]

        for row_index in range(len(img)):
            for column_index in range(len(img[0])):
                new_img[row_index][column_index] = self.__smooth(img, row_index, column_index)

        return new_img

    def __smooth(self, img: list[list[int]], row: int, column: int) -> int:
        row_min, row_max = max(0, row - 1), min(len(img) - 1, row + 1)
        column_min, column_max = max(0, column - 1), min(len(img[0]) - 1, column + 1)

        result = 0
        all_cells_count = (row_max - row_min + 1) * (column_max - column_min + 1)
        for x in range(row_min, row_max + 1):
            for y in range(column_min, column_max + 1):
                result += img[x][y]
        return result // all_cells_count


print(Solution().imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
