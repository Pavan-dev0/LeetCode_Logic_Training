"""
Problem: 13 - Roman to Integer
Difficulty: Easy
Approach: Use a hash map for $O(1)$ value lookups. Iterate through the string and compare the current character's value to the next. 
If the current is smaller, subtract it (handling cases like IV or IX); otherwise, add it.Algorithm (Process): 1. Initialize a dictionary 
of Roman symbols and their integer equivalents.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_romans={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total=0
        n=len(s)
        for i in range(n):
            if i+1<n and  dict_romans[s[i]] < dict_romans[s[i+1]]:
                total-=dict_romans[s[i]]
            else:
                total+=dict_romans[s[i]]

        return total