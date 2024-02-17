class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest_product = self.__get_largest_product(nums)
        nums.reverse()
        largest_product = max(largest_product, self.__get_largest_product(nums))

        return largest_product

    def __get_largest_product(self, nums: list[int]) -> int:
        current_product, largest_product = 1, -int(8e9)

        for num in nums:
            current_product *= num
            largest_product = max(largest_product, current_product)
            if current_product == 0:
                current_product = 1

        return largest_product
