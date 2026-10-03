class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        res = []
        for i in strs:
            res.append(str(len(i)))
            res.append("#")
            res.append(i)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        i = 0
        curr = 0
        res = []
        while i <len(s):
            if s[i] == '#':
                num = int(s[curr:i])
                word = s[i+1:i+1+num]
                curr = i+1+num
                res.append(word)
                i=curr
            else:
                i+=1
        return res
