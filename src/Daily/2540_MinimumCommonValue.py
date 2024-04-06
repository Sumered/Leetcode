class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums2_set = set(nums2)
        minimal_element = int(1e10)

        for element in nums1:
            if element in nums2_set:
                minimal_element = min(element, minimal_element)

        return minimal_element if minimal_element != int(1e10) else -1
