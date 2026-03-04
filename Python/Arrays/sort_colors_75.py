"""
Problem 75: Sort Colors
Difficulty: Medium

Approach: 
Brute Force using the Bubble Sort technique.
1. Iterate through the list n-1 times (outer loop).
2. For each pass, compare adjacent elements.
3. If the element on the right is smaller than the element on the left, swap them.
4. With each pass, the largest remaining element "bubbles" to its correct position.

Time Complexity: O(n^2) - Where n is the number of elements in the list.
Space Complexity: O(1) - The sorting is done in-place without extra memory.
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        for i in range(lens-1):
            for j in range(lens-1-i):
                if nums[j + 1]<nums[j]:
                    nums[j],nums[j + 1]=nums[j + 1],nums[j]