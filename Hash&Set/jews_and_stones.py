class Solution:
    # Question: 121

    # 24ms Beats 92.18%
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set_jewels = set(jewels)

        return sum(s in set_jewels for s in stones)