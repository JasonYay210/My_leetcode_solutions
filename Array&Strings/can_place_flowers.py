from typing import List


class Solution:
    # Question: 605

    # 14ms Beats 17.80%
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        
        while i < len(flowerbed):
            # Check if the current position is empty
            if flowerbed[i] == 0:
                # Check the adjacent positions
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    # Place a flower here
                    flowerbed[i] = 1
                    count += 1
            
            if count >= n:
                return True
            
            i += 1
        
        return count >= n