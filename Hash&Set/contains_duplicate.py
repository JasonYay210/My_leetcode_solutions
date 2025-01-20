from typing import List


class Solution:
    # Question: 217

    # 11ms Beats 53.73%
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