"""
Problem_Name:- Permutations
Problem_Difficulty:- Easy

Time_Complexity:- O(N*N!)
"""


from typing import List
import itertools 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # minor condition is that if the given length of the number is 1 then it should be 1 
        # if the length of the nums is greater than 1 return the permutation

# Note if the result is coming in the format of the lists in the number format make sure you convert it into lists

        lists=[]
        all_perms=itertools.permutations(nums)
        if len(nums)==0:
            return ""

        elif  len(nums)==1:
            lists.append(nums)
            

        elif len(nums)>1:
            for num in all_perms:
                lists.append(num)

        return lists
