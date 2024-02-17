class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        goal_index = (len(nums1) + len(nums2)) // 2
        left, right = 0, len(nums1) - 1

        while True:
            mid = (left + right) // 2
            rest = goal_index - mid - 2

            one_current = nums1[mid] if mid >= 0 else float("-inf")
            one_right = nums1[mid + 1] if mid + 1 < len(nums1) else float("inf")
            two_current = nums2[rest] if rest >= 0 else float("-inf")
            two_right = nums2[rest + 1] if rest + 1 < len(nums2) else float("inf")

            if one_current <= two_right and two_current <= one_right:
                if (len(nums2) + len(nums1)) % 2 == 0:
                    return (max(one_current, two_current) + min(one_right, two_right)) / 2
                return min(one_right, two_right)
            else:
                if one_current < two_current:
                    left = mid + 1
                else:
                    right = mid - 1
