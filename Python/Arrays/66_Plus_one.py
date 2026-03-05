"""
Problem: 66 - Plus One
Difficulty: Easy

Approach:
Traverse the digits array from right to left.

If the current digit is less than 9:
    increment it by 1 and return the array immediately.

If the digit is 9:
    set it to 0 and continue moving left (carry propagation).

If all digits were 9 (example: [9,9,9]):
    the loop finishes and we prepend 1 to the list.

Example:
[1,2,3] -> [1,2,4]
[1,2,9] -> [1,3,0]
[9,9,9] -> [1,0,0,0]

Time Complexity: O(n)
Space Complexity: O(1)
"""


from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0

        return [1]+digits