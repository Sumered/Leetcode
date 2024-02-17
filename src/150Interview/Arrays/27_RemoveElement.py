class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        val_element_indexes = []
        nums_len = len(nums)

        for iterator in range(nums_len - 1, -1, -1):
            if nums[iterator] == val:
                val_element_indexes.append(iterator)

        answer = nums_len - len(val_element_indexes)
        for iterator in range(nums_len - 1, -1, -1):
            if not val_element_indexes:
                break
            if nums[iterator] != val:
                nums[val_element_indexes.pop()] = nums[iterator]

        return answer


algos = Solution()
array = [3, 2, 2, 3]
algos.removeElement(array, 3)
print(array)
