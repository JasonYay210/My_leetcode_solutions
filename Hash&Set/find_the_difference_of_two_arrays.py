from typing import List


class Solution:
    # Question: 2217

    # 3ms Beats 94.84%
    # Time Complexity: O(n + m) m is nums2
    # Space Complexity: O(n + m) m is arr2

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1 = []
        arr2 = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        for i in nums1:
            if i not in nums2:
                arr1.append(i)
        for i in nums2:
            if i not in nums1:
                arr2.append(i)
        return [arr1, arr2]