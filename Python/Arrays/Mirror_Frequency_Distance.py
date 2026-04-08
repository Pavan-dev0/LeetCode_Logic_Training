from collections import Counter
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        def mirror(c):
            if c.isdigit():
                return chr(ord('9')-(ord(c)-ord('0')))
            else:
                return chr(ord('z')-(ord(c)-ord('a')))

        freq=Counter(s)
        visited=set()

        ans=0

        for c in freq:
            if c in visited:
                continue

            m=mirror(c)

            ans+=abs(freq[c]-freq.get(m,0))

            visited.add(c)
            visited.add(m)

        return ans