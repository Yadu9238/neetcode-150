from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)
        for i in strs:
            ls = [0]*26
            for j in i:
                ls[ord(j)-97] += 1
            di[tuple(ls)].append(i)
            
        
        return [v for k,v in di.items()]
        