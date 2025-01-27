class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        counter = Counter(nums)
        for i in counter:
            if counter[i] > len(nums) / 2:
                return i
