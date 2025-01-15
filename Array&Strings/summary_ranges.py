class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ans = []
        num = 0
        while num < len(nums):
            start = nums[num] 
            while num < len(nums)-1 and nums[num] + 1 == nums[num+1]:
                num+=1
            if start != nums[num]:
                ans.append(f"{start}->{nums[num]}")
            else:
                ans.append(f"{start}")
            
            num += 1
        return ans

            