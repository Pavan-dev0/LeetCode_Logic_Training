"""
Problem: 412 - Fizz Buzz
Difficulty: Easy

Approach:
Check divisibility by 15, 3, and 5.

"""

from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lists=[]
        for i in range(1,n+1):
            if i>0:
                if i%3==0 and i%5==0:
                    lists.append("FizzBuzz")
                elif i%3==0 and i%5!=0:
                    lists.append("Fizz")
                elif i%5==0 and i%3!=0:
                    lists.append("Buzz")

                else:
                    lists.append(str(i))
        return lists