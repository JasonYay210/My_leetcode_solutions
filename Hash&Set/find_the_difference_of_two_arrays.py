class Solution:
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