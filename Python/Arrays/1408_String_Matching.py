""" Problem 1408- String Matching in an Array 
Difficulty: Easy 

Approach:
1.Sort Words by len.
2.For each word check if its a substring of any longer word.
3 Break once found

Time_Complexity:O(n^2*m)
Space_Complexity:O(1)

"""

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result=[]
        n=len(words)
      
        for i in range(n):
            for j in range(n):
                if i!=j and words[i] in words[j]:
                    result.append(words[i])
                    break

        return result
