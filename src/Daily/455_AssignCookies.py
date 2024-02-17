class Solution:
    def findContentChildren(self, greed: list[int], cookies: list[int]) -> int:
        greed.sort()
        cookies.sort()
        child_index, result = 0, 0

        for index in range(len(cookies)):
            if child_index == len(greed):
                return result
            if greed[child_index] <= cookies[index]:
                result += 1
                child_index += 1

        return result
