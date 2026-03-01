"""
Problem: 27 - Remove Element
Difficulty: Easy

Approach:
Filter elements in-place using two pointers (slow & fast).
Overwrite unwanted values while maintaining relative order.

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slows=0

        for forward in range(len(nums)):
            if nums[forward]!=val:
                nums[slows]=nums[forward]
                slows+=1

        return slows
