
"""
Problem Name:- Search Insert Position
Problem Number:- 35 
Problem Difficulty :- Easy

"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
    
