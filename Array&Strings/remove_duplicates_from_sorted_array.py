class Solution(object):
    # Question: 26

    # 0ms Beats 100%
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeDuplicates(self, nums):
        j = 0
        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1