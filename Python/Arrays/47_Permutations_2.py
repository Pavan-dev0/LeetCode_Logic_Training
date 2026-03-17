"""
Problem_Name:- Permutations 2 
Problem Number:- 47
Problem Difficulty:- Medium"""

from typing import List 
import itertools as its


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        all_perm=its.permutations(nums)
        lists=[]
        
        unique_perm=set(all_perm)
        if len(nums)==0:
            return ""
        
        elif len(nums)==1:
            lists.append(nums)
            return lists


        elif len(nums)>1:
            return [list(p) for p in unique_perm]