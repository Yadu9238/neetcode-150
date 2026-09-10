from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,t1 = Counter(s),Counter(t)
        return s1==t1