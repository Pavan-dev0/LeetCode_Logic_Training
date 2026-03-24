from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lists=[]
        for i in range(len(nums)):
            if target== nums[i]:
                lists.append(i)
                
        if target not in nums:
            return [-1,-1]

        return [lists[0],lists[-1]]