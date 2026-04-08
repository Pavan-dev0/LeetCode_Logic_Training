class Solution:
    def longestPalindrome(self, s: str) -> str:
        lists=[]
        for i in range(len(s)):
            if s[i] not in lists:
                lists.append(s[i])
            else:
                if s[i]==s[0]:
                    lists.append(s[i])
                    break
        
        return "".join(lists)

