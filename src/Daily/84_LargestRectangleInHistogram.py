class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        biggest_area = 0
        stack: list[tuple[int, int]] = []
        for index, height in enumerate(heights):
            if not stack:
                stack.append((height, index))
            if height >= stack[-1][0]:
                stack.append((height, index))
            else:
                while stack and height < stack[-1][0]:
                    area = self.__handle_stack(stack, index)
                    biggest_area = max(area, biggest_area)
                stack.append((height, index))

        while stack:
            area = self.__handle_stack(stack, len(heights))
            biggest_area = max(area, biggest_area)

        return biggest_area

    def __handle_stack(self, stack: list[tuple[int, int]], index: int) -> int:
        rect = stack.pop()
        area = (index - rect[1]) * rect[0]
        if not stack:
            area += rect[1] * rect[0]
        else:
            area += (rect[1] - stack[-1][1] - 1) * rect[0]

        return area
