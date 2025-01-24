class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}


        for i in range(len(nums)):
            mydict[nums[i]] = i

        for i in range(len(nums)):
            end = target - nums[i]
            if end in mydict and mydict[end] != i:
                return [i,mydict[end]]