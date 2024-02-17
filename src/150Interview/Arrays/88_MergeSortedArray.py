class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged_index, nums1_index, nums2_index = m + n - 1, m - 1, n - 1

        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] >= nums2[nums2_index]:
                nums1[merged_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[merged_index] = nums2[nums2_index]
                nums2_index -= 1
            merged_index -= 1

        self.__finalize(nums1, nums2, nums1_index, nums2_index, merged_index)

    def __finalize(self, nums1: list[int], nums2: list[int], nums1_index: int, nums2_index: int, merged_index: int) -> None:
        while nums1_index >= 0 or nums2_index >= 0:
            if nums1_index < 0:
                nums1[merged_index] = nums2[nums2_index]
                nums2_index -= 1

            elif nums2_index < 0:
                nums1[merged_index] = nums1[nums1_index]
                nums1_index -= 1
            merged_index -= 1
