class Solution:
    # Question: 771

    # 0ms Beats 100%
    # Time Complexity: O(n + m) m being set_jewels
    # Space Complexity: O(m)

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)

        return sum(s in set_jewels for s in stones