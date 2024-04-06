class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {char: index for index, char in enumerate(order)}

        return str(sorted(s, key=lambda x: order_dict[x] if x in order_dict else 10000))
