from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r=sorted(nums1+nums2)

        if len(r)%2==0:
            return (r[len(r)//2-1]+r[len(r)//2])/2
        else:
            return r[(len(r)-1)//2]

