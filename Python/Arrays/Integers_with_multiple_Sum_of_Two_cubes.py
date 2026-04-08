from typing import List

class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        from collections import defaultdict
    
        cube_limit=int(round(n**(1/3)))+2
    
        count=defaultdict(int)
    
        for a in range(1,cube_limit):
            a3=a*a*a
            if a3>n:
                break
    
            for b in range(a,cube_limit):
                b3=b*b*b
                s=a3+b3
    
                if s>n:
                    break
    
                count[s]+=1
    
        result=[]
        for num in count:
            if count[num]>=2:
                result.append(num)
    
        result.sort()
        return result