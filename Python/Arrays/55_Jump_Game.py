from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # step 1 we have to take the len(nums) and loop it 
        # and if the value of the index 0 is the value needed to get skip return false 
        #else if the index is showing the non - 0th  index data go to that 
        # if the value is greater than the index value return false 
        max_reach=0
        for i,num in enumerate(nums):
            if i>max_reach:
                return False

            max_reach=max(max_reach,i+num)
        return True        
            



