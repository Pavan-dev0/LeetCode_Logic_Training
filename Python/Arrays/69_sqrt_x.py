"""Problem: 69 - Sqrt(x)
Difficulty: Easy

Approach:
Utilize the built-in `math.sqrt()` function to compute the square root of the input integer `x` and then truncate the result to its integer part using `int()`.
Note: The problem statement on LeetCode typically requires implementing the function without built-in exponent functions or operators, for which standard solutions use Binary Search or Newton's method. The time complexity below is for this specific built-in function approach.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        import math

        r=math.sqrt(x)
        return int(r)