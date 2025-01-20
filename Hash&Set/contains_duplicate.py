from typing import List


class Solution:
    # Question: 771

    # 0ms Beats 100%
    # Time Complexity: O(n + m) m being set_jewels
    # Space Complexity: O(m)
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return True
            else:
                set_nums.add(num)
        return False