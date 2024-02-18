import math


class Solution:
    def minSkips(self, dist: list[int], speed: int, hoursBefore: int) -> int:
        correction = 0.00000001  # because with a lot of floating point operations we get some rounding error

        if sum(dist) / speed > hoursBefore:
            return -1

        n = len(dist)
        skips = [[1e11 for _ in range(n + 1)] for _ in range(n)]
        skips[0][0] = math.ceil(dist[0] / speed)
        skips[0][1] = dist[0] / speed

        for index in range(1, n):
            distance = dist[index]
            skips[index][0] = math.ceil(skips[index - 1][0] + (distance / speed) - correction)

            for skip_count in range(1, n + 1):
                without_skip = math.ceil(skips[index - 1][skip_count] + (distance / speed) - correction)
                with_skip = skips[index - 1][skip_count - 1] + (distance / speed)
                skips[index][skip_count] = min(without_skip, with_skip)

        for skip_count in range(0, n + 1):
            if skips[n - 1][skip_count] <= hoursBefore:
                return skip_count

        return -1


# Explanation:
# So when first looking at problems like this, I like to ask myself, what is condition for saying that there is no solution.
# We can observe that skipping every rest will result in being at destination exactly at sum(dist) / speed. Great, all no solution test cases solved.
# Now my first intuition was to create recurrent function, which will try not skipping, then skipping, and memorizing some results.
# Obviously due to floating point arrival time, memoization of this would result in MLE + TLE probably due to 2^1000 options to check (probably possible to create such test case).
# Now lets observe the most important thing - lets say that we dont care about minimal skips. We care about minimal time to get to destination using 0, 1, 2, 3... n skips.
# So using 0 skips is easy. Now how to get answer for 1 skip?
# Here comes DP. Lets observe another important thing, if we have most optimal solution for 0 skips and 1 skip till position ith, what is the result for position ith for 1 skip?
# Obviously we can either travel to position ith using one skip somewhere before, then we cant use skip at position ith, or we can never use skip before, and use it now.
# The same situation occurs for 2 skips -> either we used both of them before, so we cant now, or we used just 1 skip before and we can use it now.
# So now we know how to get solutions for every skips count. So lets solve this and after that find the smallest amount of skips with which we arrive at destination before time limit.
#
# A really similar problem to this is "best time to buy and sell stock IV", and I really recommend doing whole series of best time to buy and sell stock before.
